# IPython in depth tutorial

In its current form, this tutorial is meant to be executed with IPython 2.0 or
newer.  You can find our installation instructions [here](http://ipython.org/install.html).

If you prefer using pip, you can also run:

	pip install --upgrade ipython[notebook]

which should give you all the necessary dependencies.


To get the tutorial, checkout the `ipython-in-depth` repo:

    git clone https://github.com/ipython/ipython-in-depth

Or just
[download current master](https://github.com/ipython/ipython-in-depth/zipball/master)
and unzip it.

At the command line, you can do this with (depending on whether your system
uses wget or curl):

    wget https://github.com/ipython/ipython-in-depth/zipball/master -O ipython-in-depth.zip

or

    curl -L https://github.com/ipython/ipython-in-depth/zipball/master -o ipython-in-depth.zip

And then:

	unzip ipython-in-depth.zip

You can then start the IPython notebook server at a terminal with:

    ipython notebook
