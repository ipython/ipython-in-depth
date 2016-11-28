# Title

IPython & Jupyter in depth: high productivity interactive python

# Category

Python Libraries

# Python Level

Intermediate

# Domain Level

Introductory

# Description

IPython and Jupyter provide tools for interactive computing that are widely
used in scientific computing, but can benefit any Python developer.

We will show how to use IPython in different ways, as: an interactive shell, a
graphical console, a network-aware VM in GUIs, a web-based notebook with code,
graphics and rich HTML. We will demonstrate how to deploy a custom environment
with Docker that not only contain multiple Python kernels as well as a couple
of other languages.

# Audience

Programmers interested in using Python interactively, especially in data
analysis environments.

# Objectives

At the end of this tutorial, attendees will have an understanding of the
overall design of Jupyter (and IPython) as a suite of applications they can use
and combine in multiple ways in the course of their development work with
Python and other languages. They will learn:

* Tricks from the IPython machinery that are useful in everyday development,

* What the high-level applications in Jupyter, the web-based notebooks can do
  and how they can be used.

* How the overall picture of IPython and Jupyter fits together, so that they
  can better use its components for the problem at hand.

# Detailed Abstract

IPython started in 2001 simply as a better interactive Python shell. Over the
last decade it has grown into a powerful set of interlocking tools that
maximize developer productivity in Python while working interactively.

Today, Jupyter consists of an IPython kernel that executes user code, provides
many features for introspection and namespace manipulation, and tools to
control this kernel either in-process or out-of-process thanks to a well
specified communications protocol implemented over ZeroMQ. This architecture
allows the core features to be accessed via a variety of clients, each
providing unique functionality tuned to a specific use case:

* An interactive, terminal-based shell with capabilities beyond the default
  Python interactive interpreter (this is the classic application opened by the
  `ipython` command that most users are familiar with).

* A [web-based notebook](http://jupyter.org/) that can execute
  code and also contain rich text and figures, mathematical equations and
  arbitrary HTML. This notebook presents a document-like view with cells where
  code is executed but that can be edited in-place, reordered, mixed with
  explanatory text and figures, etc. The notebook provides an interactive
  experience that combines live code and results with literate documentation
  and the rich media that modern browsers can display:

    ![Notebook screenshot](http://jupyter.org/assets/jupyterpreview.png)

  The notebooks also allow for code in multiple language allowing to mix Python
  with Cython, C, R and other languages to access features hard to obain from
  Python.

These tools also increasingly work with languages other than Python, and we are
renaming the language independent frontend components to *Jupyter* in order to
make this clearer. The Python kernel we provide and the original terminal-based
shell will continue to be called *IPython*.

In this hands-on, in-depth tutorial, we will briefly describe IPython's
architecture and will then show how to use the above tools for a highly
productive workflow in Python.

# Outline

**IPython: Interactivity beyond Python**

- Introducing the IPython Notebook as an interactive environment.
- Beyond Python: magic commands, shell access, object introspection, variable caching.
- Development workflow: integrating IPython with scripts via the `%run` command.
- Tools for typical development tasks: timing, profiling, debugging.

**Back to the terminal(s)**

- Demo and discussion of the last added features of the command line interpreter.
- `IPython.embed`: a useful 'microscope' into your own scripts.
- Control the namespace of your GUI codes with an IPython kernel.
- Customizing IPython with profiles.

**The IPython/Jupyter Notebook**

- Basic concepts: the server, the dashboard, your notebooks.
- A notebook as a rich document: text, code, results and multimedia.
- The IPython display protocol: `__repr__` for more than just text.
- Converting notebooks to other formats for sharing, blogging and publication.
- Sharing your notebooks: [nbviewer](http://nbviewer.ipython.org).

**Last section**

- Deploying with docker (locally or in the cloud).
- have the attendees deploy a image that contain the latest development versions.
- show how to write various extensions, and multi language integration.

# More info

For full details about IPython including documentation, previous presentations
and videos of talks, please see [the project website](http://ipython.org).

The materials for this tutorial are
[available on a github repository](https://github.com/ipython/ipython-in-depth).


# Additional Notes

Versions of this tutorial have been presented at PyCon 2012, 2014, and 2015. It
has been well received so far, and we would like to do keep teaching about
IPython and Jupyter!
