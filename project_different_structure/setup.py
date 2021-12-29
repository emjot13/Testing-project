from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

setup(
    version='2.0.0',
    author='Mateusz Jarzembiński',
    packages=find_packages(),
    python_requires='>=3.8, <4',
    install_requires=['nose2', 'assertpy', 'pytest', 'setuptools', 'parameterized', 'pyhamcrest'],
    extras_require={
        'test': ['coverage']
    },
)
