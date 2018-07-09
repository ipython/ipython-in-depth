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

###  0-0:10 (10 min) - introduction

Today this tutorial will be presented to you by Jason Grout, and Matthias
Bussonnier, two long standing members of the Jupyter Project. We have a number
of helpers in the room. Attendees should have been given red/green
sticky notes.

By now you should have installed JupyterLab following the instructions in the
readme. For this tutorial, we are standardizing on a conda-based python
distribution (miniconda or Anaconda). We may not be able to help with
installation issues if you are using a different python distribution.

JupyterLab is in beta and that first time impression
are critical to usability of JupyterLab. We will show you what can be done, but
can still improve the usability quite a bit. When trying to do any task in the
exercise try to think first:
- How would I do that
- Then try to do the task.
    - Note what was intuitive, and what surprised you.
    - Tell it to us (via post it or issues)
- Feel free to interrupt with questions and clarification


- There will likely be a binder available, but do not rely on the conference
    wifi.

###  JASON 0:10-0:25 (15min) - Standard slides covering background of notebook and JupyterLab. These are from the jupyterlab-demo repo
    - Respond to FAQ:
      - Why JupyterLab ?
      - Can you get Lab and notebook at the same time: YES
      - No difference in file format; Notebooks files are the same
###  JASON 0:25-0:45 (20 min): Tour of The User Interface
- if it does not work, hop on binder if it works
  - Point to documentation, follow the naming conventions, maybe follow that outline
  - various existing default panel, and layout, file browser, support of multiple file types, multiple file viewers for single file
  - dragging ui
  - Command palette
  - Important shortcuts
  - Can follow the outline in the pydata seattle talk or scipy 2017 lightning talk (see https://github.com/jupyterlab/jupyterlab-demo/tree/master/narrative)

###  MATTHIAS 0:45-1:05 (20 min): Exercise 1 (and help installation issues if needed):

Look into the Exercise 1 folder, and follow the instruction in `Exercise-1.md`

### 1:05-1:15 (10 min): break 10min + sticky notes

Write one good thing on the green sticky note, one bad on the red one.

### 1:15-1:20 (5 min) : Q.A. 5 min

## Workflows around executing code

###  MATTHIAS 1:20-1:30 (10 min): Minor Notebook UI interface difference - review from Exercise 1

  1. Arranging tabs through dragging
  2. How to author markdown and equations
  3. Collapsible cells
  4. drag cells, inside notebook and between views of files.
  5. Enable scrolling on outputs
  6. creating new view of outputs
  7. javascript rendering restrictions

###  MATTHIAS 1:30-1:45 (15 min): Attaching kernels to multiple documents

  1. Executing code in a markdown file using an attached console.
  2. Developing libraries with notebook and Python files attached to same kernel
  3. Reloading modules?
  4. Create terminal, work with terminal next to code file and console. Maybe using ipython in terminal.
  5. Attaching a code console to the same kernel as a notebook.


###  MATTHIAS 1:45-2:10 (15 min) Exercise 2

- binding multiple documents to the same kernel
    - New Console for Notebook
    - Markdown file + console workflow
    - Python code file + console workflow
    - Open a notebook in classic notebook, modify, save and reopen in Lab.

###  2:10-2:25 (15min)  break 10 min + sticky notes + Q.A 5min


## Customizing JupyterLab

###  MATTHIAS 2:25-2:35 (5min)

  1. Changing editor settings
  2. Changing theme
  3. Json config system overview
  4. Changing keyboard shortcuts

### Exercise 3 2:35-2:50 (15 min)
    1. change a keyboard shortcut
      1. Assign existing shortcut to new action.
      2. Assign new Keyboard shortcut to an existing action.
    2. add a keyboard shortcut (restart and run all)
    3. change an editor setting 

## 2:50-3:15 (25min) - Workflows around Widgets (Jason)

  1. Introduction to widgets and libraries like bqplot, ipyvolume, pythreejs, etc.
  2. Mirroring widget output
  3. Exercise 4:
    1. Making sure widgets works:
    2. Interact
    3. Simple slider + Graph 
    4. bqplot graph controlling another graph

## Going further (3:15-3:50, 35 min) :

  1. Extending JupyterLab – scratching the surface
    - everything is plugin
    - installing a plugin, example
      - renderer : https://github.com/jupyterlab/jupyter-renderers
      - Plotly could be a fun one (https://github.com/plotly/jupyterlab-chart-editor)
    - high-level walkthrough of what happens when a plugin is installed/enabled
      - requires npm
      - recompiling js
      - --core-mode
      - enabling/disabling extensions
    - getting started bootstrapping custom plugin
      - Walkthrough of theme plugin
      - Walkthrough of simple mimetype rendering plugin
    - Exercise 4:
      - Modifying and installing theme plugin
      - and/or
      - Modifying and installing mimetype plugin. Certificate of accomplishment plugin?
    - Point to cookie Cutter.
## Mention JupyterLab in a multiuser environment: point to jupyterlab docs
## Mention sprints!
## 3:50-4:00 QA, Question
