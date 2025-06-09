# Exemplo de setup.py
from setuptools import setup, find_packages

setup(
    name='ClientesDanielEduardodoCarmo',  # Nome do pacote
    version='0.1.0',
    author='Daniel Eduardo do Carmo',
    description='Pacote de exemplo com classe Cliente',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    python_requires='>=3.6',
)