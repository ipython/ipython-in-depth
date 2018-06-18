# SciPy 2018 JupyterLab tutorial.

This repository contain material and instructions to follow the "Getting started with JupyterLab" tutorial during SciPy 2018.

# Installation

We'd like attendees to read the following section and install the required
software ahead of time. We may ask you to update versions of the software more
closely to the tutorial date.

Please do not rely on cloud hosting to follow this tutorial, as the network
connection may be unreliable. If possible, come to the tutorial with a computer
where you have administrative privileges.

We'll assume you are using an Anaconda Python distribution (such as Anaconda or
miniconda). If you choose to work with a different Python distribution, we'll do
our best to help you, but you may have to solve any difficulties on your own.

## Software installation

1. Install either the full [anaconda distribution](https://www.continuum.io/downloads) (very extensive, but large) or [miniconda](https://conda.io/miniconda.html) (much smaller, only essential packages).

2. Create a conda environment:

```
$ conda create -c conda-forge -n scipy18jlab notebook jupyterlab pandas nodejs bqplot ipyvolume pythreejs --yes

$ conda activate scipy18jlab

# to use widgets
$ jupyter labextension install @jupyter-widgets/jupyterlab-manager jupyter-threejs ipyvolume
```

If you open multiple terminal windows make sure to activate the environment in each of them.


## Tutorial materials

To get the tutorial materials, clone this repository. **Please plan to update the materials shortly before the tutorial.**

```
git clone https://github.com/jupyterlab/scipy2018-jupyterLab-tutorial
```

To update the materials:
```
$ cd scipy2018-jupyterLab-tutorial
$ git pull
```

Feel free to open an issue or send a pull request to update these materials if things are unclear.
