import setuptools
import os
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gignatov-awesomecalculator", # Replace with your own username
    version= "1.0.0",
    author="Gleb Ignatov",
    author_email="gignatov6034@github.com",
    description="An awesome calculator package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gignatov6034/awesomecalculator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)