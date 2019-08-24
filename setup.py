from setuptools import setup, find_packages

with open("README.md", "r") as readme_content:
    readme = readme_content.read()

setup(
    name="decorpy",
    version="0.0.1",
    author="Alexandre Zajac",
    author_email="work@alexandrezajac.com",
    description="A package exposing a collection of ready-to-use python decorators",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/alexZajac/decorpy",
    packages=find_packages()
)
