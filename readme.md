# SciPy 2018 JupyterLab tutorial.

This repository contain material and instructions to follow the "Getting started with JupyterLab" tutorial during SciPy 2018.

During the tutorial, feel free to get on the `jupyterlab` channel of https://scipy2018.slack.com/ for help and updates.

# Installation

Please read the following section and install the required software ahead of
time. We may ask you to update versions of the software more closely to the
tutorial date.

Please do not rely on cloud hosting to follow this tutorial, as the network
connection may be unreliable. If possible, come to the tutorial with a computer
where you have administrative privileges.

For this tutorial, we are standardizing on a conda-based python distribution
(miniconda or Anaconda). We may not be able to help with installation issues if
you are using a different python distribution.

## Software installation

1. Install either the full [anaconda
   distribution](https://www.anaconda.com/download/) (very large, includes lots
   of conda packages by default) or
   [miniconda](https://conda.io/miniconda.html) (much smaller, with only
   essential packages by default, but any conda package can be installed).

2. To get the tutorial materials, clone this repository. **Please plan to update the materials shortly before the tutorial.**

    ```
    git clone https://github.com/jupyterlab/scipy2018-jupyterlab-tutorial
    ```

    To update the materials:
    ```
    cd scipy2018-jupyterlab-tutorial
    git pull
    ```

    Feel free to open an issue or send a pull request to update these materials if things are unclear.

3. Set up your environment.

    Create a conda environment:

    ```
    conda create -n scipy18jlab -c conda-forge --override-channels --yes python=3.6 pip cookiecutter=1.6 notebook=5.5 pandas=0.23 nodejs=9.11 jupyterlab bqplot ipyvolume pythreejs
    ```

    (You could instead create the environment from the supplied environment file with `conda env create -f scipy2018-jupyterlab-tutorial/environment.yml`)

    Activate the conda environment:

    ```
    conda activate scipy18jlab
    ```

    Install extra JupyterLab extensions:

    ```
    jupyter labextension install @jupyter-widgets/jupyterlab-manager jupyter-threejs ipyvolume bqplot @jupyterlab/geojson-extension @jupyterlab/fasta-extension
    ```

If you open multiple terminal windows make sure to activate the environment in each of them. Your terminal prompt should be preceded by the name of the current environment, for example:
```
(scipy18jlab) ~/scipy2018-jupyterlab-tutorial $
```


## Starting JupyterLab

Enter the following command in a new terminal window to start JupyterLab.

```
$ jupyter lab
```

## Removing environment

You can delete the environment by using the following in a terminal prompt.

```
conda env remove --name scipy18jlab --yes
```

This will **not** delete any data, but only the conda environement named `scipy18jlab` .

# Optional packages

We are demonstrating a few packages not installed in the above lists. These are
optional, and not required for the exercises in this tutorial.

To install these, first activate the tutorial environment:

```
conda activate scipy18jlab
```

Then install the python packages:
```
conda install -c conda-forge --override-channels --yes ipyleaflet ipympl
pip install sidecar
```

and install the JupyterLab extensions:
```
jupyter labextension install jupyterlab-toc jupyter-leaflet @jupyter-widgets/jupyterlab-sidecar jupyterlab-drawio
```

# Troubleshooting

If you experience an out-of-memory error, you can increase the memory available:
```
NODE_OPTIONS=--max_old_space_size=4096 jupyter lab build
```
or
```
NODE_OPTIONS=--max_old_space_size=4096 jupyter labextension install ...
```
This increases the available memory for the build process to 4Gb.
