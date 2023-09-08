"""setup"""
from setuptools import find_packages, setup

setup(
    name="demo",
    version="0.0.1",
    author="asgordeev",
    description="Aligning and processing images",
    python_requires=">=3.8",
    packages=find_packages(exclude=(".github", "docs", "examples", "tests")),
)
