# SciPy 2018 JupyterLab tutorial. 

This repository contain material and instructions to follow the "Getting started with JupyterLab" tutorial during SciPy 2018.

# Installation instructions

We'd like attendees to read the following section and install the required
software ahead of time. We'll run through the tutorial by assuming that the
wireless connection may be unreliable.

Do not rely on cloud hosting to follow this tutorial. If possible comes to the
tutorial with a computer where you have administrative privileges.

We'll assume you are using an Anaconda python distribution. Yo can come with a
non anaconda python distribution we'll do our best to help you, but
non-anaconda installations will not be a priority during the tutorial. 

## install steps:

1. You can install either the full [anaconda distribution](https://www.continuum.io/downloads) (very extensive, but large) or [miniconda](https://conda.io/miniconda.html) (much smaller, only essential packages).

2. Create a conda environment:

```
$ conda config --add channels conda-forge
$ conda create -n jupyterlab-2018 notebook jupyterlab pandas nodejs bqplot ipyvolume pythreejs --yes

# Mac/Linux:
$ source activate jupyterlab-2018

# Windows:
$ activate jupyterlab-2018

# to use widgets
$ jupyter labextension install @jupyter-widgets/jupyterlab-manager 
$ jupyter labextension install jupyter-threejs ipyvolume

```

If you open multiple terminal windows make sure to activate the environment in each of them.


## Tutorial materials

To get the tutorial materials, clone this repository. **Please plan to update the materials shortly before the tutorial.**

```
git clone https://github.com/jupyter/scipy2018-jupyterLab-tutorial
```

update :
```
$ cd scipy2018-jupyterLab-tutorial
$ git pull
```

Feel free to send Pull request to update the material if things are unclear.



