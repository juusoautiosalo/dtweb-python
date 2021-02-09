from setuptools import find_packages, setup

setup(
    name='dtweb',
    packages=find_packages(),
    version='0.0.1',
    description='Python library for accessing the Digital Twin Web',
    author='Juuso Autiosalo',
    license='MIT',
    install_requires=['requests'],
)
