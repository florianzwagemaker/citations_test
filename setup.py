from setuptools import find_packages, setup

from citations_test import __version__

setup(
    name="Citations_test",
    description="A test package for citations",
    author="Florian Zwagemaker",
    license="MIT",
    version=__version__,
    packages=find_packages(),
    python_requires=">=3.7",
    entry_points={"console_scripts": ["citations_test=citations_test.__main__:main"]},
    zip_safe=False,
)
