import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="python-steamgriddb",
    version="1.0.5",
    author="Zebco",
    author_email="zebco1382@gmail.com",
    description="A Python wrapper for SteamGridDB's API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ZebcoWeb/python-steamgriddb",
    packages=setuptools.find_packages(),
    license="MIT",
    keywords=['steamgriddb', 'steamgrid', 'steam', 'grid', 'db', 'api', 'wrapper'],
    install_requires=['requests'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
