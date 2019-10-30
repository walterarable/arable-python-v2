from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().split('\n')

setup(
   name='arable-python',
   version='1.0',
   description='A useful module for making calls to arable api v2',
   author='Walter Jove',
   author_email='walter.jove@arable.com',
   url="https://github.com/walterarable/arable-python-v2",
   packages=['arable-python'],  #same as name
   install_requires=requirements, #external packages as dependencies
   scripts=[
            'scripts/cool',
            'scripts/skype',
           ]
)