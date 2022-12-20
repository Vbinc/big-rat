from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf8") as readme_file:
    readme = readme_file.read()

setup(
    name="bigrat",
    version="1.0.3",
    author="Talgat The Random",
    packages=["bigrat"],
    package_dir={"bigrat": "src"},
    author_email="eureq631@gmail.com",
    description="A package to save trading data",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Vbinc/big-rat",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)