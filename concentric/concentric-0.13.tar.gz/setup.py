#!/usr/bin/env python

# Support setuptools only, distutils has a divergent and more annoying API and
# few folks will lack setuptools.
from setuptools import setup
from importlib.resources import open_text
# Version info -- read without importing
_locals = {}

exec(open_text('concentric', '_version.py').read(), None, _locals)
version = _locals['__version__']

# PyYAML ships a split Python 2/3 codebase. Unfortunately, some pip versions
# attempt to interpret both halves of PyYAML, yielding SyntaxErrors. Thus, we
# exclude whichever appears inappropriate for the installing interpreter.
exclude = ["*.yaml2", 'test']

# Frankenstein long_description: version-specific changelog note + README
with open('README.rst') as f:
    long_description = f.read()

extras = {}
all_extras = set()
for x in [ 'db2i', 'hp3000', 'mssql', 'mysql', 'netsuite', 'oracle', 'postgres', 'redshift', 'snowflake', 'dev', 'db2i_native', 'vertica', ]:
    filename = f'{x}.txt'
    with open(filename, 'r') as f:
        st = f.read()
    rg = st.split()
    extras[x] = rg
    if x != 'dev':
        all_extras |= set(rg)
all_extras = list(all_extras)
all_extras.sort()
extras['all'] = all_extras


setup(
    name='concentric',
    version=version,
    description='a simple connection manager for connecting to various rdbms (mostly legacy)',
    license='BSD',
    long_description=long_description,
    author='Preetam Shingavi',
    author_email='p.shingavi@yahoo.com',
    url='https://bitbucket.org/dbuy/concentric',
    packages=[
        'concentric',
    ],
    package_data=dict(concentric=['*.yml']),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'waddle',
        'raft',
        'sqlalchemy',
    ],
    extras_require=extras,
)
