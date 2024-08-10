from setuptools import setup, find_packages

setup(
    name = "test-automation",
    version = "1.0",
    author = "Raphael Nyangenya",
    author_email = "raphaelnyangenya@gmail.com",
    description = ("TechnoBrain Hackathon"),
    packages=find_packages(),
    package_dir={"": "src"}
)