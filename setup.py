from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='wishful_controller',
    version='0.1.0',
    packages=find_packages(),
    url='http://www.wishful-project.eu/software',
    license='',
    author='Piotr Gawlowicz, Mikolaj Chwalisz',
    author_email='{gawlowicz, chwalisz}@tkn.tu-berlin.de',
    description='Unified Programming Interfaces (UPIs) Framework',
    long_description='Implementation of a wireless controller using the unified programming interfaces (UPIs) of the Wishful project.',
    keywords='wireless control',
    install_requires=['pyzmq', 'gevent', 'decorator', 'dill']
)
