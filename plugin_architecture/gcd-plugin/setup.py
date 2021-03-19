from setuptools import setup

setup(
    name="gcd-plugin",
    install_requires="gcd",
    entry_points={"gcd": ["feedback = gcd_plugin"]},
    py_modules=["gcd_plugin"],
)
