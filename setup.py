import sys
from setuptools import setup

VERSION = '2.0.0'

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 4)

if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write("Current version of python is lower than what is required (required=%s.%s)" % REQUIRED_PYTHON)


with open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(
  name='gen-pptx-from-simple-text',
  python_requires='>=3.4',
  version=VERSION,
  author='Suku John George',
  author_email='sukujgrg@gmail.com',
  url='https://github.com/sukujgrg/gen-pptx-from-simple-text',
  description='CLI to generate powerpoint slides from simple text file[s].',
  long_description=long_description,
  long_description_content_type='text/markdown',
  license='MIT',
  entry_points={
    'console_scripts': [
      'pptx=src:cli',
    ],
  },
  packages=setuptools.find_packages(),
  install_requires=[
    'click==7.*',
    'python-pptx==0.6.*'
  ],
  classifiers=[
    'Programming Language :: Python :: 3',
    'Operating System :: OS Independent'
  ]
)
