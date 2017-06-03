from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='music_downloader',
    version='0.1.0.dev',
    description='Baixe músicas de um jeito simples',
    long_description=readme,
    author=u'Tarcisio marinho',
    author_email='tarcisio_marinho09@hotmail.com',
    url='https://github.com/tarcisio-marinho/Music-Downloader',
    license=license,
    packages=find_packages(exclude=['tests']),
    install_requires=['requests', 'bs4', 'lxml']
)
