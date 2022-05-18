from setuptools import setup, find_packages

setup(
    name='adsai',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='An example python package',    
    install_requires=['pandas'],    
    author='Erik',
    author_email='myemail@example.com'
)