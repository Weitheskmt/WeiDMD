from setuptools import setup, find_packages

meta = {}
with open("weidmd/meta.py") as fp:
    exec(fp.read(), meta)

# Package meta-data.
NAME = meta["__title__"]
DESCRIPTION = "Wei's Dynamic Mode Decomposition."
URL = "https://github.com/Weitheskmt/WeiDMD"
MAIL = meta["__mail__"]
AUTHOR = meta["__author__"]
VERSION = meta["__version__"]
KEYWORDS = "dynamic-mode-decomposition dmd"

REQUIRED = ["numpy<2", "scipy", "matplotlib", "scikit-learn"]

EXTRAS = {
    "docs": ["Sphinx>=1.4", "sphinx_rtd_theme"],
    "test": ["pytest", "pytest-cov", "pytest-mock", "ezyrb>=v1.2.1.post2205"],
}

LDESCRIPTION = (
    "Simulating dynamics of open quantum systems is sometimes a significant challenge, "
    "despite the availability of various exact or approximate methods.\n"
    "Particularly when dealing with complex systems, "
    "the huge computational cost will largely limit the applicability of these methods.\n"
    "WeiDMD is a Python package that uses Dynamic Mode Decomposition for "
    "a data-driven model simplification based on spatiotemporal coherent "
    "structures.\n"
    "whether the external field is involved or not, "
    "the DMD can give accurate prediction of the result compared with the traditional propagations, "
    "and simultaneously reduce the required computational cost.\n"
)

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LDESCRIPTION,
    author=AUTHOR,
    author_email=MAIL,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    keywords=KEYWORDS,
    url=URL,
    license="MIT",
    packages=find_packages(),
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    zip_safe=False,
)
