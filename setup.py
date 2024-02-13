import os

import pkg_resources
from setuptools import setup, find_packages

setup(
    name="image-captioning-clip",
    py_modules=["image-captioning-clip"],
    version="1.0",
    description="",
    packages=find_packages(),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ],
    include_package_data=True
)
