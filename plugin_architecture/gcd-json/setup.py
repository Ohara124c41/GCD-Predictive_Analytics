from setuptools import setup

setup(
    name="gcd-json",
    install_requires="gcd",
    entry_points={"gcd": ["xform = gcd_json"]},
    py_modules=["gcd_json"],
)
