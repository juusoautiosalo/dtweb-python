from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

setup(
    name='dtweb',
    version='0.0.1',
    author='Juuso Autiosalo',
    author_email="juuso.autiosalo@iki.fi",
    description='Python library for accessing the Digital Twin Web',
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/juusoautiosalo/dtweb-python",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license='MIT',
    packages=find_packages(),
    install_requires=['requests'],
    python_requires='>=3.8',
)
