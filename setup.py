#setup .py file I will be able to develop my ml application as a package and so we can deploy easily so other can use

from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT ='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requiremnts

    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements
setup(
    name = 'mlproject',
    version = '0.0.1',
    author='Sheriff',
    author_email='mohdsheriff27021996@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    ##how setup.py file will able to know how amny packages need to be install by in src which act as whole package because of __init__.py
    
)
