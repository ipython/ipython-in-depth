# IPython in depth tutorial

Try it out on Binder! [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/ipython/ipython-in-depth/master?filepath=binder%2FIndex.ipynb)

In its current form, this tutorial is meant to be executed with Jupyter notebook
5.0, using IPython 6.0 or newer on Python 3, the latest IPython version
compatible with Python 2 is IPython 5.x that may not have the exact same
behavior and all the features presented in this tutorial.


You can find our installation instructions [for
IPython](https://ipython.org/install.html) and [Jupyter
notebook](https://jupyter.readthedocs.io/en/latest/install.html)

To get the tutorial, checkout the `ipython-in-depth` repo:

    git clone https://github.com/ipython/ipython-in-depth

Or [download current
master](https://github.com/ipython/ipython-in-depth/zipball/master) and unzip
it.

At the command line, you can do this with (depending on whether your system uses
wget or curl):

    wget https://github.com/ipython/ipython-in-depth/zipball/master -O ipython-in-depth.zip

or

    curl -L https://github.com/ipython/ipython-in-depth/zipball/master -o ipython-in-depth.zip

And then:

    unzip ipython-in-depth.zip

Change directory inside the directory newly created:

    cd ipython-in-depth

You can then start the Jupyter notebook server at a terminal with:

    jupyter notebook


## Docker images

The tutorial do reference a couple of docker images that are quite heavy
(several GB). Please do not download them on conference wifi. You may want to
populate the Docker Cache you may want to use the following command ahead of
time:

  $ docker pull jupyter/datascience-notebook

The image contains a installation of the Jupyter notebook with R, Julia,
Python2, Python3 and a couple of libraries for each language.
