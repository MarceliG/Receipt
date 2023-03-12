from setuptools import find_packages, setup

requirements = {
    "install": [
        "tox >= 4.4.5",
    ],
    "ut": [
        "pytest >= 6.2.5",
    ],
    "style": [
        "black >= 22.10.0",
        "flake8 >= 4.0.0",
        "isort >= 5.10.0",
        "mypy >= 1.0.0",
    ],
}

setup(
    name="Receipt",
    version="0.0.1",
    packages=find_packages(),
    install_requires=requirements["install"],
    extras_require={
        "ut": requirements["ut"],
        "style": requirements["style"],
    },
)