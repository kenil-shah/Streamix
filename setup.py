from setuptools import setup, find_packages

def get_requirements(filename):
    with open(filename) as f:
        requirements = f.read().splitlines()
    return requirements

setup(name='Streamix',
      version='1.0',
      description='CSC 510: Software Engineering Project Phase1',
      author='Kenil Shah',
      author_email='kshah9@ncsu.edu',
      license="MIT",
      packages=find_packages(),
      python_requires=">=3.6",
      install_requires = get_requirements("requirements.txt"),
      include_package_data=True,
     )
