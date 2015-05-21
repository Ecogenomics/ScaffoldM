from distutils.core import setup

setup(
    name='scaffoldm',
    version='1.0.0',
    author='Alexander Baker',
    author_email='alexander.baker@uq.edu.au',
    packages=['scaffoldm'],
    scripts=['bin/scaffoldm'],
    license='GPLv3',
    description='scaffoldm',
    long_description=open('README.md').read(),
    install_requires=[],
)

