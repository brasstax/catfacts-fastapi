"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="catfacts-fastapi",
    version="20220611.7",
    description="Cat facts provided by FastAPI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brasstax/catfacts-fastapi",
    author="Brass Tax",
    author_email="brasstax@users.noreply.github.com",
    classifiers=[ 
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: REST APIs",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7, <4",
    install_requires=["fastapi", "uvicorn", "gunicorn", "databases[sqlite]"], 
    extras_require={
        "dev": ["black"],
        "test": ["pytest"],
    },
    entry_points = {
        "console_scripts": [
            "init-catfacts=catfacts_fastapi.utils:init_catfacts"
        ],
    },
)
