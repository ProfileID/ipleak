from setuptools import setup, find_packages
import pypandoc

with open("./requirements.txt") as f:
    required = f.read().splitlines()

long_description = pypandoc.convert("./README.md", "rst")

setup(name='ipleak',
      version='0.1',
      description='Python Tool to check your VPN.',
      long_description=long_description,
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
