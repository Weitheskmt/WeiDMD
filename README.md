<p align="center">
  <a href="http://pydmd.github.io/PyDMD/" target="_blank" >
    <img alt="Python Dynamic Mode Decomposition" src="readme/logo_weidmd.png" width="400" />
  </a>
</p>
<p align="center">
    <a href="https://github.com/Weitheskmt/WeiDMD/blob/main/LICENSE" target="_blank">
        <img alt="Software License" src="https://img.shields.io/badge/license-MIT-brightgreen.svg?style=for-the-badge">
    </a>
    <a href="https://pypi.org/project/weidmd/"  target="_blank">
        <img alt="PyPI version" src="https://img.shields.io/pypi/v/weidmd?style=for-the-badge">
    </a>
</p>

## Table of contents
* [Description](#description)
* [Dependencies and installation](#dependencies-and-installation)
* [Examples and Tutorials](#examples-and-tutorials)
* [Using PyDMD](#using-pydmd)
* [Awards](#awards)
* [References](#references)
* [Developers and contributors](#developers-and-contributors)
* [Funding](#funding)

## Description

**WeiDMD** is a Python package designed for **Dynamic Mode Decomposition (DMD)**, a data-driven method used for analyzing and extracting spatiotemporal coherent structures from time-varying datasets. It provides a comprehensive and user-friendly interface for performing DMD analysis, making it a valuable tool for researchers, engineers, and data scientists working in various fields.

With WeiDMD, users can easily decompose complex, high-dimensional datasets into a set of coherent spatial and temporal modes, capturing the underlying dynamics and extracting important features. See the [**Examples**](#examples-and-tutorials) section below and the [**Tutorials**](tutorials/README.md) to have an idea of the potential of this package. Also see the diagram below for a summary of all available tools and functionalities. Currently in-progress contributions are represented by semi-transparent boxes.

<p align="center">
    <img src="readme/pydmd_capabilities.svg" width="1000" />
</p>

## Dependencies and installation

### Installing via PIP
PyDMD is available on [PyPI](https://pypi.org/project/weidmd), therefore you can install the latest released version with:
```bash
> pip install weidmd
```

### Installing from source
To install the bleeding edge version, clone this repository with:
```bash
> git clone https://github.com/Weitheskmt/WeiDMD
```

and then install the package in [development mode](https://setuptools.pypa.io/en/latest/userguide/development_mode.html):
```bash
> pip install -e .
```

### Dependencies
The core features of **PyDMD** depend on `numpy` and `scipy`. In order to use the plotting functionalities you will also need `matplotlib`.

## Examples and Tutorials
You can quickly know how to use the package in the [tutorials](tutorials/fast_use/test.ipynb).

## Using WeiDMD
To perform DMD, simply begin by initializing a WeiDMD module that implements your DMD method of choice. Here, we demonstrate how a user might build a customized WeiDMD model. Models may then be fitted by calling the `fit()` method and passing in the necessary data.
```python3
from weidmd import WeiDMD

# Build a Wei's DMD (WeiDMD) model.
DMD = WeiDMD(
    time=t,  # time series time = (m,) numpy array of times of data collection
    kernel=K,  # kernel K = (n, m) numpy array of time-varying snapshot data
    num_snapshots=2000,  # the number of snapshots, and default is len(K)
    nskip=1,  # K[:num_snapshots][::nskip]
)

# Fit the DMD model and display a summary of the DMD results.
DMD.fit(
  tf=1200, # end of predicted time
  name=None, # Can be defaulted and None will not store DMD results. Setting any string, such as' k1 ', will result in DMD_ The results folder found the corresponding saved file for 'k1'
  d='default', # It can be defaulted and empirical values will be used. If the effect is poor, it can be considered as an adjustment.)
```
## References

To implement the various versions of the DMD algorithm we follow these works:
* **Wei's DMD:** Wei Liu, Zi-Hao Chen, Yu Su, Yao Wang, and Wenjie Dou. *Predicting rate kernels via dynamic mode decomposition*. The Journal of Chemical Physics 159, no. 14 (2023). [[DOI](https://doi.org/10.1063/5.0170512)] [[bibitem](readme/refs/citations-20231031T120359.bibtex)]
