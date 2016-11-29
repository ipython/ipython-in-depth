Authors/Presenter. 

- Matthias Bussonnier: bussonniermatthias AT gmail.com , Core Developer of IPython/Jupyter.
- Mike Bright: pycon AT mjbright.net,  Solution Architect at HPE OpenNFV Lab Grenoble, long time IPython and Jupyter User and Contributor.
- Min RK: benjaminrk AT gmail.com Core Developer of IPython/Jupyter

Notes: Box on the Pycon Proposal website are

- Description
- Audience
- Outline
- Additional Notes

# Title

IPython and Jupyter in Depth: High productivity, interactive Python

# Category

Python Libraries

# Python Level

Intermediate

# Domain Level

Introductory

# Description

IPython and Jupyter provide tools for interactive computing that are widely
used in scientific computing, education, and data science, but can benefit any
Python developer.

You will learn how to use IPython in different ways, as:

- an interactive shell,
- a graphical console,
- a network-aware VM (Virtual machine) in GUIs,
- a web-based notebook combining code, graphics and rich HTML.

We will demonstrate how to deploy a custom environment
with Docker that not only contains multiple Python kernels but also a couple
of other languages.

# Audience

Programmers interested in using Python interactively, especially in data
analysis environments. Prior knowledge of Python is best. Some prior knowledge
of Python is helpful. Some experience with Docker would be helpful but not
required for the last quarter of the tutorial.

# Objectives

At the end of this tutorial, attendees will have an understanding of the
overall design of Jupyter (and IPython) as a suite of applications they can use
and combine in multiple ways in the course of their development work with
Python and other programming languages. They will learn:

* Tricks from the IPython machinery that are useful in everyday development,

* What high-level applications in Jupyter, the web-based notebooks, can do and
  how these applications can be used.

* How to use IPython and Jupyter together so that they can be best used for the
  problem at hand.

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
  `ipython` command that many users have worked with)

* A [web-based notebook](http://jupyter.org/) that can execute
  code and also contain rich text and figures, mathematical equations and
  arbitrary HTML. This notebook presents a document-like view with cells where
  code is executed but that can be edited in-place, reordered, mixed with
  explanatory text and figures, etc. The notebook provides an interactive
  experience that combines live code and results with literate documentation
  and the rich media that modern browsers can display:

    ![Notebook screenshot](http://jupyter.org/assets/jupyterpreview.png)

  The notebooks also allow for code in multiple languages allowing to mix Python
  with Cython, C, R and other programming languages to access features hard to obain from
  Python.

These tools also increasingly work with languages other than Python, and we
renamed the language independent frontend components to *Jupyter* in order to
make this clearer. The Python kernel we provide and the original terminal-based
shell will continue to be called *IPython*.

In this hands-on, in-depth tutorial, we will briefly describe IPython's
architecture and will then show how to use the above tools for a highly
productive workflow in Python.

# Outline

Note to reviewers: Each section will take 1/4 of the teaching time, taking into
account the scheduled snack break. Each section will provide takeaway slides
and notebooks for the attendee. There will be hands-on time of 5-10 minutes
during each section for attendees to try out concepts.

**IPython: Interactivity beyond Python**

- Introducing the IPython Notebook as an interactive environment.
- Beyond Python: magic commands, shell access, object introspection, variable caching.
- Development workflow: integrating IPython with scripts via the `%run` command.
- Tools for typical development tasks: timing, profiling, debugging.

We will leave 1 to 2 minutes hands-on for simple subjects like object
introspection and variable caching. We'll give a couple of 5 minutes hands-on
exercises for profiling and debugging.

**Back to the terminal(s)**

- Demo and discussion of the last added features of the command line interpreter.
- `IPython.embed`: a useful 'microscope' into your own scripts.
- Control the namespace of your GUI codes with an IPython kernel.
- Customizing IPython with profiles.

We'll leave 5-10 minutes at the end of this section for user to play
with multiple profiles and embeded IPython.

**The IPython/Jupyter Notebook**

- Basic concepts: the server, the dashboard, your notebooks.
- A notebook as a rich document: text, code, results and multimedia.
- The IPython display protocol: `__repr__` for more than just text.
- Converting notebooks to other formats for sharing, blogging and publication.
- Sharing your notebooks: [nbviewer](http://nbviewer.ipython.org).

We'll leave 10 minutes for user to create a custom representation for an object
of their choice and publish their notebook online on nbviewer.

**Cloud hosting and multilanguage**

- Deploying with docker (locally or in the cloud).
- have the attendees deploy a image that contains the latest development versions.
- show how to write various extensions, and multi language integration.
- introduce JupyterHub and its use for groups


# More info

For full details about IPython including documentation, previous presentations
and videos of talks, please see [the project website](http://ipython.org).

The materials for this tutorial are
[available on a github repository](https://github.com/ipython/ipython-in-depth).


# Additional Notes

Versions of this tutorial have been presented at PyCon 2012, 2014, 2015 and also EuroPython 2016. It
has been well received so far, and we would like to keep teaching about
IPython and Jupyter!

https://www.youtube.com/watch?v=XFw1JVXKJss (2012)
https://www.youtube.com/watch?v=bP8ydKBCZiY (2013)
https://www.youtube.com/watch?v=05fA_DXgW-Y (2015)
