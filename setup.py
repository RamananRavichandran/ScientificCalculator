""" setup file to create egg"""
from setuptools import setup, find_packages

setup(
    name="ScientificCalculator",
    version='1.13',
    packages=find_packages(),
    entry_points={'setuptools.installation': ['eggsecutable = src.main.main:main']},
    data_files=[('.', ["__main__.py", 'setup.py', 'requirements.txt'])],
)
