from setuptools import setup, find_packages
from os import path

with open("./requirements.txt") as f:
    required = f.read().splitlines()

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='ipleak',
      version='0.2.1',
      description='Python Tool to check your VPN.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='profileid',
      author_email='profileid@protonmail.com',
      url="https://github.com/ProfileID/ipleak",
      license='MIT',
      packages=['ipleak'],
      install_requires=required,
      entry_points={
          "console_scripts": ["ipleak = ipleak.__main__:main"]
      },
      classifiers=[
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8'
      ]
      )
