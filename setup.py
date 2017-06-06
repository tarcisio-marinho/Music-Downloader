from setuptools import setup, find_packages
from os import path

base = path.abspath(path.dirname(__file__))

with open(path.join(base, 'README.rst')) as f:
    readme = f.read()

# with open(path.join(base, 'LICENSE')) as f:
#     license = f.read()

with open(path.join(base, 'requirements.txt')) as f:
    requirements = f.read().splitlines()

setup(
    name='music_downloader',
    version='0.1.12.dev',
    author=u'Tarcisio marinho',
    author_email='tarcisio_marinho09@hotmail.com',
    keywords='music download script python',
    url='https://github.com/tarcisio-marinho/Music-Downloader',
    data_files = [('', ['requirements.txt'])],
    description='Baixe músicas de um jeito simples',
    license='GNU General Public License v2.0',
    long_description=readme,
    packages=find_packages(exclude=['tests']),
    install_requires=requirements,
    maintainer='Tarcisio marinho, André Santos',
    maintainer_email='tarcisio_marinho09@hotmail.com, andreztz@gmail.com '

)
