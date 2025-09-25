from setuptools import find_packages, setup


def read_requirements(path: str) -> list[str]:
    with open(path) as f:
        return f.read().splitlines()


setup(
    name="library",
    version="0.1.0",
    description="A simple library using OOP in Python",
    author="Libonati Diego Martin",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.10",
    install_requires=read_requirements("requirements.txt"),
    extras_require={
        "dev": read_requirements("requirements.test.txt"),
    },
    entry_points={
        "console_scripts": [
            "library=library.library:main",
        ],
    },
)
