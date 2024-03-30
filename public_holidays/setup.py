from setuptools import find_packages, setup

setup(
    name="public_holidays",
    packages=find_packages(exclude=["public_holidays_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
