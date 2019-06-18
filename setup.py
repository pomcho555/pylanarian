# -*- coding: utf-8 -*-
from setuptools import setup

import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    with open('README.md') as f:
        readme = f.read()
except IOError:
    readme = ''

if sys.version_info < (3, 5):
    raise NotImplementedError("Sorry, you need at least Python 3.5+ to use yomogi.")


setup(name='pylanarian',
      version='0.1.0',
      description='An animated graph and real time plotting package.',
      long_description=readme,
      url='http://github.com/pomcho555/pylanarian',
      author='pomcho555',
      author_email='',
      license='MIT',
      packages=['pylanarian'],
      install_requires=[
          'matplotlib'
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False,)