from setuptools import setup, find_packages

def get_requirements(filepath):
    requirements = []
    with open(filepath,"r") as f:
        requirements = f.readlines()
        requirements = [req.replace("\n","") for req in requirements]
    return requirements
setup(
    name= "Project",
    version= "0.1",
    author= "Shahzad Ahmad",
    author_email="shahzad136@gmail.com",
    packages= find_packages(),
    install_requires = get_requirements("requirements.txt")
)