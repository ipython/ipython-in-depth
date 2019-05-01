## Instruction and what to install (+15min ~ 0:15)

Quick instruction on how to get instructions and install required packages, get data... Fallback on online hosting for users if can't get to work on laptop.
(We'll continue installation during next section)

## Jupyter & IPython, overview of Ecosystem and new features (+25 min ~ 0:40)

- What are the different pieces, how to get help after the tutorial. 
  - Jupyter
  - JupyterHub
  - Notebook interfaces. 
  - Kernels
  - Extensions (difference between kernel, front-endand server extension, we'll only explore IPython kernel extension later in the tutorial)
  - Binder
- Moving toward Python 3 only, already he case for many pieces
- Difference between notebook and JupyterLab
- Overview what's New in JupyterLab, what's the difference with Classic Notebook.
   - Complete compatibility. You can install both at the same time. 
   - Same file format, same protocol...
- Online hosted platforms
   - Azure, Coclac, Colab, ...
- Other frontends
   - Nteract Vs Code, Atom, 
- Whats new in Python, and how IPython/Jupyter make best use of it (will detail in later sections)


## IPython: Interactivity beyond Python (+35min ~ 1:15)

- Beyond Python: 
      - magic commands, shell access, object introspection.
      - integration with top-level async code in Python 3.6+
      - superhelp `?` / `??`
      - system command `!`
      - Tab completion
- Tools for typical development tasks: timing, profiling, debugging.

We will leave 1 to 2 minutes hands-on for simple subjects like object
introspection and variable caching.


BREAK

## Back to the terminal(s) (+15min ~ 1:30)

- Demo and discussion of the last added features of the command line interpreter.
- `IPython.embed`: a useful 'microscope' into your own scripts.
- Customizing IPython with profiles.

We'll leave 5-10 minutes at the end of this section for user to play
with multiple features of IPython.

## Notebook/JupyterLab a tour of the GUI (+40min ~ 2:10)

- Couple of exercise to get user acclimated to JupyterLab and notebook Interfaces, keyboard shortcut. 
- Plan a couple of advance written exercises showing-off advance features for user already familiar with new interface. 
- Basic concepts: the server, the dashboard, your notebooks.
- A notebook as a rich document: text, code, results and multimedia.
- Sharing your notebooks: [nbviewer](http://nbviewer.ipython.org), MyBinder.org
- Converting notebooks to other formats for sharing, blogging and publication.

We'll interleave this presentation with few minutes breaks and try to ask user to achieve a specific state before showing them how to achieve it.

## JupyterLab, IPython exercises (+50min ~3:00)

In this section we'll have user customize their own code to make full use of the Jupyter and IPython capabilities. 

 - The IPython display protocol: `__repr__` for more than just text.
    - make full use of the display protocol to get a visualisation. 
 - Discuss and work with widgets. 
    - How widgets can bring interactivity to visualisation and analysis. 
- Create an IPython extension, and register magics. 
   - This should show the basic of cross-language integration. 
 - Make use of magic to run a cross language analysis. 


    
## Conclusion 

Further resource and conclusion (if time permit)


---------------

# Outline

**These notes are for the presenters.**

For the last two years the Jupyter team has been working on the new Jupyter
frontend: JupyterLab. While JupyterLab does of course allow the use of Jupyter
Notebooks, it goes beyond the classic Jupyter Notebook by providing a flexible
and extensible web application with a set of reusable components. Users can
arrange multiple notebooks, text editors, terminals, output areas, and custom
components using tabs and collapsible sidebars. These components are carefully
designed to enable the user to use them together or separately (for example, a
user can send code from a file to a console with a keystroke, or can pop out an
output from a notebook to work with it alone).

JupyterLab is based on a flexible application plugin system provided by
PhosphorJS that makes it easy to customize existing components or extend it
with new components. For example, users can install or write third-party
plugins to view custom file formats, such as GeoJSON, interact with external
services, such as Dask or Apache Spark, or display their data in effective and
useful ways, such as interactive maps, tables, or plots.

In this tutorial we’ll walk users thought the best way to make use of
JupyterLab, how to transition from the “classic” Jupyter Notebook frontend to
JupyterLab, and how to make the best use of the new powerful features of
JupyterLab.


You (should) be provided with red and green sticky notes. If you have any
question and concern or need help, stick the red sticky note visible on back of
your laptop's screen. A helper will come see you, or the speaker will take time
to get questions.

If all is fine, or we're too slow for you, stick the green sticky note to the
back of your laptop screen.

At each break, write a thing you understood of liked on the green sticky note,
a thing you did not like or found hard on the red one. When exiting the room,
stick them to the door frame. Make sure to get new sticky notes for the next
section.

This can serve as a quick read through summary of what we talked about (with
links) and a rough timeline if you want to follow up on the video later.

## Overview of JupyterLab

###  8-8:10 (10 min) - introduction

Today this tutorial will be presented to you by  Matthias
Bussonnier, two long standing members of the Jupyter Project. We have a number
of helpers in the room. Attendees should have been given red/green
sticky notes.

By now you should have installed JupyterLab following the instructions in the
readme. For this tutorial, we are standardizing on a conda-based python
distribution (miniconda or Anaconda). We may not be able to help with
installation issues if you are using a different python distribution.

JupyterLab is close to be release as a 1.0, only a few changges are expected
between now and final release. We will show you what can be done, but
can still improve the usability quite a bit. When trying to do any task in the
exercise try to think first:
- How would I do that
- Then try to do the task.
    - Note what was intuitive, and what surprised you.
    - Tell it to us (via post it or issues)
- Feel free to interrupt with questions and clarification


- There will likely be a binder available, but do not rely on the conference
    wifi.

### 9:10 (+15min)
 - Introduction to JupyterLab (slides)

- Respond to FAQ:
  - Why JupyterLab ?
  - Can you get Lab and notebook at the same time: YES
  - No difference in file format; Notebooks files are the same

### 9:25-9:45 (20 min): Tour of The User Interface
  - Following outline from https://github.com/jupyterlab/jupyterlab-demo/tree/master/narrative or https://gist.github.com/jasongrout/3039b5909734b1abf4544a8df68a8ace

###  9:45-10:05 (20 min): Exercise 1 (and help installation issues if needed):

Look into the Exercise 1 folder, and follow the instruction in `Exercise-1.md`

### 10:05-10:15 (10 min): break 10min + sticky notes

Write one good thing on the green sticky note, one bad on the red one.

### 10:15-10:20 (5 min) : Q.A. 5 min

## Workflows around executing code

###  10:20-10:30 (10 min): Minor Notebook UI interface difference - review from Exercise 1

  1. Arranging tabs through dragging
  2. How to author markdown and equations
  3. Collapsible cells
  4. drag cells, inside notebook and between views of files.
  5. Enable scrolling on outputs
  6. creating new view of outputs
  7. javascript rendering restrictions (removed in the next beta)


###  10:30-10:55 (15 min) Exercise 2

- binding multiple documents to the same kernel
    - New Console for Notebook
    - Markdown file + console workflow
    - Python code file + console workflow
    - Open a notebook in classic notebook, modify, save and reopen in Lab.


###  10:55-11:00 (15 min): Attaching kernels to multiple documents

  1. Executing code in a markdown file using an attached console.
  2. Developing libraries with notebook and Python files attached to same kernel
  3. Reloading modules?
  4. Create terminal, work with terminal next to code file and console. Maybe using ipython in terminal.
  5. Attaching a code console to the same kernel as a notebook.



###  11:10-11:25 (15min)  break 10 min + sticky notes + Q.A 5min


## Customizing JupyterLab

###  11:25-11:35 (10min)

  1. Changing editor settings
  2. Changing theme
  3. Json config system overview
  4. Changing keyboard shortcuts

### Exercise 3 11:35-11:50 (15 min)
    1. change a keyboard shortcut
      1. Assign existing shortcut to new action.
      2. Assign new Keyboard shortcut to an existing action.
    2. add a keyboard shortcut (restart and run all)
    3. change an editor setting

## Extensions (11:50-11:30, 35 min)

1. Everything is an extension - show the package.json
2. Installing/listing/enabling/disabling plugins. `jupyter lab build`
3. `--core-mode`
4. Exercise 5 - writing your own extension

## What's new (11:30-11:40)

JupyterLab 0.33 prerelease out:
- Workspaces
- Extension manager
- Console show outputs
- Open in new browser tab
- Longer tabs
- Many, many upgrades

Extensions in the works:
- Keyboard shortcut editor
- Status bar
- Real-time collaboration


## Mention JupyterLab in a multiuser environment: point to jupyterlab docs
## Mention sprints!
## 11:40-12:00 QA, Question
