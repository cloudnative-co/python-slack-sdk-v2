from setuptools import setup, find_packages

setup(
    name="Slack",
    version="0.9.0",
    description="Slack SDK for Python 3.6",
    author="sebastian",
    author_email="seba@cloudnative.co.jp",
    packages=find_packages("lib/python"),
    package_dir={'': "lib/python"},
    install_requires=[
    ],
    entry_points={
        "console_scripts": [
        ]
    },
)
