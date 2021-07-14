from setuptools import setup

setup(
    name='blib',
    version='0.0.1',
    description='Package for drawing M@B Bannerlord banners from banner codes',
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