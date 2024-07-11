from setuptools import setup, find_packages

# Add install requirements
setup(
    author="Sondos Aabed",
    description="A package for converting imperial lengths and weights.",
    name="impyrial",
    packages=find_packages(include=["impyrial", "impyrial.*"]),
    version="0.1.0",
    install_requires=['numpy>=1.10', 'pandas'],
    python_requires="==3.6.*",
)
