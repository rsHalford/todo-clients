#!/usr/bin/env python
from setuptools import setup

todos_classifiers=[
    'Environment :: Console',
    'Intended Audience :: End Users/Desktop',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Natural Language :: English',
    'Operating System :: Unix',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python',
    'Topic :: Utilities'
]

with open('README.md', 'r') as fp:
    todos_long_description = fp.read()

setup(
    name='todos',
    description='List, add, update and delete your todo list from the command-line.',
    keywords='todo list client terminal command-line',
    author='Richard Halford',
    author_email='richard@xhalford.com',
    url='https://www.github.com/rsHalford/todo-clients/tree/main/python-client',
    version='1.0.0',
    licence='GNU GPLv3',
    long_description=todos_long_description,
    long_description_content_type='text/markdown',
    packages=['todos'],
    install_requires=['requests'],
    python_requires='>=3',
    classifiers=todos_classifiers,
    entry_points={
        'console_scripts': [
            'todos = todos:main',
        ],},
)
