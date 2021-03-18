from setuptools import setup, find_packages

setup(
    name="gcd",
    install_requires="pluggy>=0.3,<1.0",
    entry_points={"console_scripts": ["gcd=gcd.host:main"]},
    packages=find_packages(),
)
