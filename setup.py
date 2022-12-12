from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf8") as readme_file:
    readme = readme_file.read()

setup(
    name="big-rat",
    version="0.0.6",
    author="Talgat The Random",
    author_email="eureq631@gmail.com",
    description="A package to save trading data",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Vbinc/big-rat",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)