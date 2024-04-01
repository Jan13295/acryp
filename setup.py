import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "acryp",
    version = "0.0.1",
    author = "Jan",
    author_email = "jan091@gmx.at",
    description = "a new encoding and decoding principle",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/Jan13295/acryp",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.6"
)