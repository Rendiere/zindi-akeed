import os

from setuptools import setup, find_packages


def readme():
    """
    Utility function to read the README file.
    Used for the long_description.  It's nice, because now 1) we have a top level
    README file and 2) it's easier to type in the README file than to put a raw
    string in below ...
    :return: String
    """
    return open(os.path.join(os.path.dirname(__file__), 'README.md')).read()


setup(
    name='zindi-akeed-recommendation',
    version='0.1.0',
    url='',
    license='',
    author='Renier Botha',
    author_email='r.botha91@gmail.com',
    description='Python Boilerplate contains all the boilerplate you need to participate in a Zindi competition',
    python_requires='>=3',
    long_description=readme(),
)
