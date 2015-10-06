from setuptools import setup
from setuptools import find_packages

setup(
    name='GeobricksTRMM',
    version='0.1.1',
    author='Simone Murzilli; Guido Barbaglia',
    author_email='geobrickspy@gmail.com',
    packages=find_packages(),
    license='LICENSE.txt',
    long_description=open('README.md').read(),
    description='TRMM plug-in for Geobricks downloader.',
    install_requires=[
        'watchdog', 'flask', 'flask-cors'
    ],
    url='http://pypi.python.org/pypi/GeobricksTRMM/'
)
