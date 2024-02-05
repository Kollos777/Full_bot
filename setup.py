from setuptools import setup

setup(
   name='Personal_assistant',
   version='0.2',
   description='Personal assistant',
   url="https://github.com/Dimon4444eg/Personal-assistant-CLI",
   author='Dmitriy Kylishov',
   author_email='kylishovdimka@ukr.net',
   license='MIT',
   packages=['Personal_assistant'],
   install_requires=[],
   entry_points={
       'console_scripts': [
           'Personal_assistant=Personal_assistant.main:main'
       ]
   }
)
