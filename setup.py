# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="enlarge-mason-nystrom", # the name that you will install via pip
    version="1.0",
    author="Mason Nystrom",
    author_email="masonnystrom@gmail.com",
    description="function that enlarges a number",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/masonnystrom/my-lambdata",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)