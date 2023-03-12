from setuptools import find_packages,setup
from typing import List

HYPN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]: 
    '''
    this funtion will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]
        if HYPN_E_DOT in requirements:
            requirements.remove(HYPN_E_DOT)

    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Sanskar',
    author_email='asanskar24@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'), 
)