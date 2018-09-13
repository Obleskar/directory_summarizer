import setuptools

with open("README.md", "r") as infile:
    long_description = infile.read()

setuptools.setup(
    name="directory_summarizer",
    version="0.0.1",
    author="Benjamin Deuson",
    author_email="benjamindeuson@gmail.com",
    description="Command line package for generating directory tree summaries with file counts.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)