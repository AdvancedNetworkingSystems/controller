import logging
import time
import sys
import zmq.green as zmq
import uuid
import datetime
import gevent
from gevent import Greenlet
from gevent.event import AsyncResult
try:
   import cPickle as pickle
except:
   import pickle

from controller_module import *
import wishful_framework as msgs
import upis_builder
from transport_channel import TransportChannel
from node_manager import NodeManager
from module_manager import ModuleManager

__author__ = "Piotr Gawlowicz, Mikolaj Chwalisz"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, chwalisz}@tkn.tu-berlin.de"

#TODO: improve hello sending, add scheduler + timeout mechanism for node removal, 

class Controller(Greenlet):
    def __init__(self, dl, ul):
        Greenlet.__init__(self)
        self.log = logging.getLogger("{module}.{name}".format(
            module=self.__class__.__module__, name=self.__class__.__name__))

        self.uuid = str(uuid.uuid4())
        self.config = None

        self.default_callback = None
        self.callbacks = {}
        self.newNodeCallback = None
        self.nodeExitCallback = None
        self.call_id_gen = 0

        self.moduleManager = ModuleManager(self)
        self.nodeManager = NodeManager(self)

        self.transport = TransportChannel(ul, dl)
        self.transport.subscribe_to(self.uuid)
        self.transport.set_recv_callback(self.process_msgs)

        #UPIs
        builder = upis_builder.UpiBuilder(self)
        self.radio = builder.create_radio()
        self.net = builder.create_net()
        self.mgmt = builder.create_mgmt()

        #function call context
        self._scope = None
        self._iface = None
        self._exec_time = None
        self._delay = None
        self._timeout = None
        self._blocking = False
        self._callback = None
        #container for blocking calls
        self._asyncResults = {}

    def stop(self):
        self.running = False
        self.log.debug("Nofity EXIT to all modules")
        self.moduleManager.exit()
        self.transport.stop()

    def _run(self):
        self.log.debug("Controller starts".format())

        self.log.debug("Nofity START to all modules")
        self.moduleManager.start()

        self.running = True
        while self.running:
            self.transport.start()

    def group(self, group):
        self._scope = group
        return self       

    def node(self, node):
        self._scope = node
        return self        

    def nodes(self, nodelist):
        self._scope = nodelist
        return self

    def iface(self, iface):
        self._iface = iface
        return self

    def exec_time(self, exec_time):
        self._exec_time = exec_time
        return self

    def delay(self, delay):
        self._delay = delay
        return self

    def timeout(self, value):
        self._timeout = value
        return self

    def blocking(self, value=False):
        self._blocking = value
        return self

    def callback(self, callback):
        self._callback = callback
        return self


    def _clear_call_context(self):
        self._scope = None
        self._iface = None
        self._exec_time = None
        self._delay = None
        self._timeout = None
        self._blocking = False
        self._callback = None


    def add_module(self, moduleName, pyModuleName, className, kwargs):
        self.moduleManager.add_module(moduleName, pyModuleName, className, kwargs)


    def add_upi_module(self, upi, pyModuleName, className, importAs):
        self.log.debug("Adding new UPI module: {}:{}:{}".format(moduleName, className, importAs))
        upiModule = self.moduleManager.add_upi_module(upi, pyModuleName, className)
        setattr(self, importAs, upiModule)


    def load_config(self, config):
        self.log.debug("Config: {}".format(config))

        #load modules
        moduleDesc = config['modules']
        for m_name, m_params in moduleDesc.iteritems():
            kwargs = {}
            if 'kwargs' in m_params:
                kwargs = m_params['kwargs']

            self.add_module(m_name, m_params['module'], m_params['class_name'],kwargs)


    def new_node_callback(self, **options):
        def decorator(callback):
            self.nodeManager.newNodeCallback = callback
            return callback
        return decorator


    def node_exit_callback(self, **options):
        def decorator(callback):
            self.nodeManager.nodeExitCallback = callback
            return callback
        return decorator


    def add_callback(self, function, **options):
        def decorator(callback):
            self.log.debug("Register callback for: ", function.__name__)
            self.callbacks[function.__name__] = callback
            return callback
        return decorator


    def set_default_callback(self, **options):
        def decorator(callback):
            self.log.debug("Setting default callback")
            self.default_callback = callback
            return callback
        return decorator


    #TODO: move to new module
    def rule(self, event, filters=None, match=None, action=None, permanence=None, callback=None):

        assert event
        rule = msgs.RuleDesc()
        fmodule = event[0].__module__.split('.')
        fmodule = fmodule[len(fmodule)-1]
        rule.event.type = fmodule
        rule.event.func_name = event[0].__name__
        rule.event.repeat_interval = pickle.dumps(event[1])

        if filters:
            #TODO: filters
            rule.filter.filter_type = "MOV_AVG"
            rule.filter.filter_window_type = "TIME"
            rule.filter.filter_window_size = "10"

        if match:
            rule.match.condition = match[0]
            rule.match.value = pickle.dumps(match[1])

        if action:
            af_module = action[0].__module__.split('.')
            af_module = af_module[len(af_module)-1]
            rule.action.type = af_module
            rule.action.func_name = action[0].__name__
            rule.action.args = pickle.dumps(action[1])

        if permanence:
            rule.permanence = msgs.RuleDesc.TRANSIENT
        
        if callback:
            rule.callback = callback.__name__

        self.send_rule(rule)
        return self

    #TODO: move to new module
    def send_rule(self, rule):
        self.log.debug("Controller sends rule to agent".format())
        
        assert self._scope
        
        dest = self._scope
        cmdDesc = msgs.CmdDesc()
        cmdDesc.type = msgs.get_msg_type(msgs.RuleDesc)
        cmdDesc.func_name = msgs.get_msg_type(msgs.RuleDesc)
        msgContainer = [dest, cmdDesc.SerializeToString(), rule.SerializeToString()]
        self.transport.send_downlink_msg(msgContainer)


    def generate_call_id(self):
        self.call_id_gen = self.call_id_gen + 1
        return self.call_id_gen


    def send_cmd(self, upi_type, fname, *args, **kwargs):
        self.log.debug("Controller calls {}.{} with args:{}, kwargs:{}".format(upi_type, fname, args, kwargs))
        
        #TODO: add assert, blocking and callback cannot be at the same time

        dest = self._scope 
        callId = str(self.generate_call_id())

        #if dest in self.nodeManager.nodes:
        cmdDesc = msgs.CmdDesc()
        cmdDesc.type = upi_type
        cmdDesc.func_name = fname
        cmdDesc.call_id = callId

        if self._iface:
            cmdDesc.interface = self._iface

        if self._blocking:
            self._asyncResults[callId] = AsyncResult()       

        #TODO: support timeout, on controller and agent sides?

        if self._delay:
            cmdDesc.exec_time = str(datetime.datetime.now() + datetime.timedelta(seconds=self._delay))

        if self._exec_time:
            cmdDesc.exec_time = str(self._exec_time)

        self.log.debug("Controller sends message: {}:{}:{}".format(dest, cmdDesc.type, cmdDesc.func_name))
        msgContainer = []
        msgContainer.append(str(dest))
        cmdDesc.serialization_type = msgs.CmdDesc.PICKLE
        msgContainer.append(cmdDesc.SerializeToString())
        
        #Serialize kwargs (they contrain args)
        serialized_kwargs = pickle.dumps(kwargs)
        msgContainer.append(serialized_kwargs)

        self.transport.send_downlink_msg(msgContainer)

        if self._callback:
            self.callbacks[callId] = self._callback

        if callId and self._blocking:
            self._blocking = False
            response = self._asyncResults[callId].get()
            del self._asyncResults[callId]
            self._clear_call_context()
            return response

        self._clear_call_context()
        return callId


    def process_msgs(self, msgContainer):
        dest = msgContainer[0]
        cmdDesc = msgContainer[1]
        msg = msgContainer[2]

        self.log.debug("Controller received message: {} from agent".format(cmdDesc.type))

        if cmdDesc.type == msgs.get_msg_type(msgs.NewNodeMsg):
            self.nodeManager.add_node(msgContainer)

        elif cmdDesc.type == msgs.get_msg_type(msgs.HelloMsg):
            self.nodeManager.serve_hello_msg(msgContainer)

        elif cmdDesc.type == msgs.get_msg_type(msgs.NodeExitMsg):
            self.nodeManager.remove_node(msgContainer)

        else:
            self.log.debug("Controller received message: {}:{} from agent".format(cmdDesc.type, cmdDesc.func_name))

            callId = cmdDesc.call_id
            if callId in self._asyncResults:
                self._asyncResults[callId].set(msg)
            else:
                if cmdDesc.call_id in self.callbacks:
                    self.callbacks[cmdDesc.call_id](dest, self.nodeManager.get_node_by_id(cmdDesc.caller_id), msg)
                    del self.callbacks[cmdDesc.call_id]
                elif cmdDesc.func_name in self.callbacks:
                    self.callbacks[cmdDesc.func_name](dest, self.nodeManager.get_node_by_id(cmdDesc.caller_id), msg)
                elif self.default_callback:
                    self.default_callback(dest, self.nodeManager.get_node_by_id(cmdDesc.caller_id), cmdDesc.func_name, msg)
                else:
                    self.log.debug("Response to: {}:{} not served".format(cmdDesc.type, cmdDesc.func_name))