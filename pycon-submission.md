# Title

IPython & Jupyter in depth: high productivity interactive and parallel python

# Category

Python Libraries

# Python Level

Intermediate

# Domain Level

Intermediate

# Description

IPython and Jupyter provide tools for interactive and parallel computing that are widely
used in scientific computing, but can benefit any Python developer.

We will show how to use IPython in different ways, as: an interactive shell,
a graphical console, a network-aware VM in GUIs, a web-based
notebook with code, graphics and rich HTML, and a high-level framework for
parallel computing.

# Audience 

Programmers interested in using Python interactively, especially in data
analysis environments.

# Objectives

At the end of this tutorial, attendees will have an understanding of the overall design of Jupyter as a suite of applications they can use and combine in multiple ways in the course of their development work with Python and other languages. They will learn:

* Tricks from the IPython machinery that are useful in everyday development,

* What the high-level applications in Jupyter, the web-based notebooks and the graphical Qt console, can do and how they can be used.

* How the IPython's architecture forms a natural foundation for high-level parallel computing with low latency and high throughput.

* How the overall picture of IPython and Jupyter fits together, so that they can better use its components for the problem at hand.
  
# Detailed Abstract

IPython started in 2001 simply as a better interactive Python shell. Over the last decade it has grown into a powerful set of interlocking tools that maximize developer productivity in Python while working interactively.

Today, Jupyter consists of an IPython kernel that executes user code, provides many features for introspection and namespace manipulation, and tools to control this kernel either in-process or out-of-process thanks to a well specified communications protocol implemented over ZeroMQ. This architecture allows the core features to be accessed via a variety of clients, each providing unique functionality tuned to a specific use case:

* An interactive, terminal-based shell with capabilities beyond the default Python interactive interpreter (this is the classic application opened by the `ipython` command that most users are familiar with).

* A [graphical, Qt-based console](http://ipython.org/ipython-doc/stable/interactive/qtconsole.html) that provides the look and feel of a terminal, but adds support for inline figures, graphical calltips, a persistent session that can survive crashes of the kernel process, and more. A user-based review of some of these features can be found [here](http://stronginference.com/weblog/2011/7/15/innovations-in-ipython.html).

* A [web-based notebook](http://ipython.org/notebook.html) that can execute code and also contain rich text and figures, mathematical equations and arbitrary HTML. This notebook presents a document-like view with cells where code is executed but that can be edited in-place, reordered, mixed with explanatory text and figures, etc. The notebook provides an interactive experience that combines live code and results with literate documentation and the rich media that modern browsers can display:

![Notebook screenshot](http://i.imgur.com/eo2SqS9.png)

* A high-performance, low-latency system for [parallel computing](http://ipython.org/ipython-doc/stable/parallel/parallel_intro.html) that supports the control of a cluster of IPython engines communicating over ZeroMQ, with optimizations that minimize unnecessary copying of large objects (especially numpy arrays). These engines can be controlled interactively while developing and doing exploratory work, or can run in batch mode either on a local machine or in a large cluster/supercomputing environment via a batch scheduler.

These tools also increasingly work with languages other than Python, and we are renaming the language independent frontend components to *Jupyter* in order to make this clearer. The Python kernel we provide and the original terminal-based shell will continue to be called *IPython*.

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

- The text and Qt-based consoles.
- `IPython.embed`: a useful 'microscope' into your own scripts.
- Control the namespace of your GUI codes with an IPython kernel.
- Customizing IPython with profiles.

**The IPython/Jupyter Notebook**

- Basic concepts: the server, the dashboard, your notebooks.
- A notebook as a rich document: text, code, results and multimedia.
- The IPython display protocol: `__repr__` on acid.
- Converting notebooks to other formats for sharing, blogging and publication.
- Sharing your notebooks: [nbviewer](http://nbviewer.ipython.org).

**A brief introduction to `IPython.parallel`** 

- Basic architecture: the concept of an "interactive IPython cluster".
- Direct execution of code across engines in a cluster.
- Dynamic load-balancing of tasks.
- IPython engines in the cloud (illustrated with Rackspace Compute instances).

# More info

For full details about IPython including documentation, previous presentations
and videos of talks, please see [the project website](http://ipython.org).

The materials for this tutorial are
[available on a github repository](https://github.com/ipython/ipython-in-depth).


# Additional Notes

This is essentially a repeat of a tutorial Fernando Perez gave at Pycon 2014.
It was apparently a big success and he was asked to do it again. However, since Fernando cannot
make it to this Pycon, he has asked us to do it. We are both core members of
the IPython development team.
