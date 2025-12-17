# setup.py is used to package your Python project so it can be installed, reused, and deployed easily.
# ie building our project as a distributable package itself.

from setuptools import setup, find_packages

def get_requirements(file_path: str):
    """
    Reads requirements.txt and returns a list of dependencies
    """
    requirements = []
    with open(file_path) as file:
        requirements = file.read().splitlines()

        # remove empty lines and comments
        requirements = [
            req for req in requirements
            if req and not req.startswith("-e")
        ]

    return requirements

setup(
    name="student_placement_readiness_analyzer",
    version="0.1.0",
    author="Your Name",
    packages=find_packages(),  # Auto-detect folders with __init__.py and think them as packages and includes them
    install_requires=get_requirements("requirements.txt"),  # Specifies the dependencies required for this package to work properly
)
