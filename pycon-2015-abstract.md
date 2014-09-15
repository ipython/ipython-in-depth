IPython started in 2001 simply as a better interactive Python shell. Over the
last decade it has grown into a powerful set of interlocking tools that
maximize developer productivity in Python while working interactively.

Today, IPython consists of a kernel that executes the user code and provides
many features for introspection and namespace manipulation, and tools to control
this kernel either in-process or out-of-process thanks to a well-specified
communications protocol implemented over ZeroMQ. This architecture allows the
core features to be accessed via a variety of clients, each providing unique
functionality tuned to a specific use case:

- An interactive, terminal-based shell with capabilities beyond the default
Python interactive interpreter (this is the classic application opened by the
`ipython` command that most users are familiar with).

- A [graphical, Qt-based console](http://ipython.org/ipython-doc/stable/interactive/qtconsole.html)
that provides the look and feel of a terminal, but adds support for inline
figures, graphical calltips, a persistent session that can survive crashes of
the kernel process, and more. A user-based review of some of these features can
be found here.

- A [web-based notebook](http://ipython.org/notebook.html) that can execute
code and also contain rich text and figures, mathematical equations and
arbitrary HTML. This notebook presents a document-like view with cells where
code is executed but that can be edited in-place, reordered, mixed with
explanatory text and figures, etc. The notebook provides an interactive
experience that combines live code and results with literate documentation and
the rich media that modern browsers can display:

![Notebook screenshot](http://i.imgur.com/eo2SqS9.png)

- A high-performance, low-latency system for [parallel computing](http://ipython.org/ipython-doc/stable/parallel/parallel_intro.html)
that supports the control of a cluster of IPython engines communicating over
ZeroMQ, with optimizations that minimize unnecessary copying of large objects
(especially numpy arrays). These engines can be controlled interactively while
developing and doing exploratory work, or can run in batch mode either on a
local machine or in a large cluster/supercomputing environment via a batch
scheduler.

These tools also increasingly work with languages other than Python, and we are
renaming the language independent frontend components to *Jupyter* in order to
make this clearer. The Python kernel we provide and the original terminal-based
shell will continue to be called *IPython*.

In this hands-on, in-depth tutorial, we will briefly describe IPython's
architecture and will then show how to use the above tools for a highly
productive workflow in Python.