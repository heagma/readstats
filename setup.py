from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='readstats',
   version='1.0',
   description='Get different statistics from Goodreads',
   license="MIT",
   long_description=long_description,
   author='HeAgMa',
   author_email='heagma@live.com',
   url="https://gitlab.com/heagma/readstats",
   packages=['readstats'],
   install_requires=['requests', 'beautifulsoup'], #external packages as dependencies
)
