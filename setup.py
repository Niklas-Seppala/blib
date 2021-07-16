from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='blib',
    version='0.0.2',
    description='Package for drawing images of M@B Bannerlord banners from community created banner codes.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['blib'],
    url='https://github.com/Niklas-Seppala/blib',
    author='Niklas Seppälä',
    install_requires = [
        'numpy',
        'pillow'
    ],
    package_dir={'': 'src'},
    classifiers=[
          'Intended Audience :: Developers',
          'Programming Language :: Python',
          ],
)