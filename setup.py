from setuptools import find_packages, setup
from typing import List

def get_packages(file_path:str) -> List[str]:

    requirements = []
    with open(file_path,'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [requirement.replace('\n','') for requirement in requirements]
    if '-e .' in requirements:
        requirements.remove('-e .')
    return requirements


setup (
    name='mlproject',
    version='0.0.1',
    author='Anik',
    author_email='banerjee.anik32@gmail.com',
    packages=find_packages(),
    install_requires = get_packages('requirements.txt')
)