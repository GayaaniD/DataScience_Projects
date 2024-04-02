from setuptools import find_packages,setup # findpackages will automatically findout all the packages available in the entire ml application in the directory we have actually created
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return list of requirements
    '''
    HYPEN_E_DOT='-e .'
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


''' Whenever we are creating packages, we really need to write the name of the application,version (we can update the versions based on chnages in package),author,author_email,packages,install_requires(mention the require libraries that we want to install) --> so we can treat these as meta data '''
setup(
    name='mlproject',
    version='0.0.1',
    author='Gayaani',
    author_email='gayani.parames@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)