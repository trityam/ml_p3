from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    to get all the libraries from the requirements.txt
    '''
    req=[]
    with open(file_path)as file_obj:
        req=file_obj.readlines()
        req=[i.replace("/n","") for i in req]

    return req





setup(
    name="ml project",
    version="0.0.3",
    author="aman",
    author_email="satyam.tripathi246@gmail.com",
    packages=find_packages(),
    requires=get_requirements("requirements.txt")

)