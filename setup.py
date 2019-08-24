from setuptools import setup, find_packages

with open("README.md", "r") as readme_content:
    readme = readme_content.read()

setup(
    name="decorpy",
    version="0.1",
    author="Alexandre Zajac",
    author_email="work@alexandrezajac.com",
    description="A package exposing a collection of ready-to-use python decorators.",
    long_description=readme,
    keywords=["decorator", "timer", "debug", "typing"],
    long_description_content_type="text/markdown",
    url="https://github.com/alexZajac/decorpy",
    packages=find_packages(),
    download_url="https://github.com/alexZajac/decorpy/archive/v_01.tar.gz",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
)
