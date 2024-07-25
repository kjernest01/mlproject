# find all packages
from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]

        # a singular line of requirements.txt contains HYPEN_E_DOT which is an indication to build setup.py as well
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT) # removing HYPEN_E_DOT since it is not a library that needs to be installed
    
    return requirements


# project metadata
setup(
    name='mlproject',
    version='0.0.1',
    author='Jonathan',
    author_email='kjernest01@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt') # auto installation of needed libraries
)