For the last two years the Jupyter team has been working on the new Jupyter frontend: JupyterLab. While JupyterLab does of course allow the use of Jupyter Notebooks, it goes beyond the classic Jupyter Notebook by providing a flexible and extensible web application with a set of reusable components. Users can arrange multiple notebooks, text editors, terminals, output areas, and custom components using tabs and collapsible sidebars. These components are carefully designed to enable the user to use them together or separately (for example, a user can send code from a file to a console with a keystroke, or can pop out an output from a notebook to work with it alone).

JupyterLab is based on a flexible application plugin system provided by PhosphorJS that makes it easy to customize existing components or extend it with new components. For example, users can install or write third-party plugins to view custom file formats, such as GeoJSON, interact with external services, such as Dask or Apache Spark, or display their data in effective and useful ways, such as interactive maps, tables, or plots.

In this tutorial we’ll walk users thought the best way to make use of JupyterLab, how to transition from the “classic” Jupyter Notebook frontend to JupyterLab, and how to make the best use of the new powerful features of JupyterLab.

  

Outline. 

// Sticky notes red/green

1.  Overview of JupyterLab

  0-0:10 (10 min) - introduction of who we are, and others in the room that can help, and rough outline of schedule, explaining of red/green sticky notes, quick installation notes or binder instructions
  - We will be using Conda and provide the necessary commands to get everything working. (as an example, see the instructions in the ipywidgets tutorial readme:https://github.com/mwcraig/scipy2017-jupyter-widgets-tutorial) 
  - If you are not using Conda, we’ll be here to help you but will not make your case a priority.
  - There will be a binder available, but do not rely on the conference wifi.
  - hopefully should be done before tutorial
  - If there are improvements to JupyterLab that you observe, or is something is confusing to you, please write it down and tell us at the break.
  MATTHIAS 0:10-0:25 (15min) - Standard slides covering background of notebook and JupyterLab. These are from the jupyterlab-demo repo
    - Respond to FAQ:
      - Why JupyterLab ?
      - Can you get Lab and notebook at the same time: YES
      - No difference in file format; Notebooks files are the same
  JASON? 0:25-0:45 (20 min): Tour of The User Interface
  - if it does not work, hop on binder.
  - Point to documentation, follow the naming conventions, maybe follow that outline
  - various existing default panel, and layout, file browser, support of multiple file types, multiple file viewers for single file
  - Command palette
  - Important shortcuts
  - Dragging ui
  - Inspector
  - Can follow the outline in the pydata seattle talk or scipy 2017 lightning talk (see https://github.com/jupyterlab/jupyterlab-demo/tree/master/narrative)
  0:45-1:05 (20 min): Exercise (and help installation issues if needed):
    Keep in mind, if something is not intuitive, or not in the place you expected it, write it down, and give it to us at the break.
  - Create a new python 3 notebook. 
    - Create a markdown cell. 
      - Write some markdown with Bold, italic and Math. 
    - Create a code cell and evaluate it.
      - Try importing Pandas, 
      - use `pandas?` to get the help on the pandas library.
      - try `pandas.D<tab>` to get tab completion on the pandas library. 
        - note that it can take a few second the first time the library get inspected to get result. 
        - Complete to `DataFrame(` place the cursor after the pen bracket and press `Shift-Tab` to get quick help. 
        - To always see the info about the current function you can open the inspector via the Cmd-I/Ctrl-I or via the command palette. 
        - Change the inspector layout to be side-by-side with the notebook.
        - use panda’s `read_csv`  to load `'demo/data/iris.csv'` into a dataframe, display this dataframe
    - Move a cell by dragging
    - Collapse and expand an input and output
    - Enable output scrolling in a cell that has lots of output
    - “Create new view for output” in the context menu of an output. Execute the cell again to see the mirrored output update
    - Open the inspector and place it side-by-side with the notebook. Type a command to see the help pop up.
    - Open a long notebook. Do “New View into File” from the tab context menu. Scroll down to the bottom of the notebook in one frame, and drag a cell from the top of the file to the bottom by dragging between the two windows.
  - Create a new python notebook and put it side by side with the first one. Copy a cell by dragging a cell from the first notebook to this notebook.
  - get several notebooks/python/data files opens next to each other to prepare next session
    - open the `demo/data/iris.csv` and other data files in separate windows.
    - You can duplicate one of the file and use right-click to open both in a viewer an editor. See how modification in one is reflected immediately in the Other.
  - Creating new document/notebook/terminal/console
  - Refresh to see the interface stays
  - (Maybe introduce workspaces?)
  - arranging things side-by-side. Come up with specific layouts they have to get
  - single-document mode
  - Use keyboard shortcuts to use command palette
  - Open same notebook in classic notebook
  - Opening document with several viewers. Live markdown rendering.
  - CSV viewing
  - Json/GeoJson.
  1:05-1:15 (10 min): break 10min + sticky notes
  1:15-1:20 (5 min) : Q.A. 5 min .
2. Workflows around executing code
  1:20-1:30 (10 min): Minor Notebook UI interface difference
  1. How to author markdown and equations
  2. Collapsible cells
  3. drag cells
  4. javascript rendering restrictions
  5. creating new view of outputs
  1:30-1:55 (25 min): Attaching kernels to multiple documents
    1. R-markdown like workflow
    2. Developing libraries with notebook and Python files attached to same kernel
  1:55-2:10 (15 min) Exercise
  - binding multiple documents to the same kernel (Section II)
    - New Console for Notebook
    - R-Markdown workflow.
    - Python code file + console workflow
    - Open in classic notebook, modify, save and reopen in Lab.
  2:10-2:25 (15min)  break 10 min + sticky notes + Q.A 5min
3. Customizing JupyterLab
  2:25-2:50 (35min)
  1. Changing editor settings
  2. Changing theme
  3. Json config system over
  4. Changing keyboard shortcuts
  5. Exercise (10 min)
    1. change a keyboard shortcut
      1. Assign existing shortcut to new action.
      2. Assign new Keyboard shortcut to an existing action.
    2. add a keyboard shortcut (restart and run all)
    3. change an editor setting 
4. 2:50-3:15 (25min) - Workflows around Widgets
  1. Introduction to widgets and libraries like bqplot, ipyvolume, pythreejs, etc.
  2. Mirroring widget output
  3. Exercise:
    1. Making sure widgets works:
    2. Interact
    3. Simple slider + Graph 
    4. bqplot graph controlling another graph
5. Going further (3:15-3:50, 35 min) :
  1. Extending JupyterLab – scratching the surface
    - everything is plugin
    - installing a plugin, example
      - Plotly could be a fun one (https://github.com/plotly/jupyterlab-chart-editor)
    - high-level walkthrough of what happens when a plugin is installed/enabled
      - requires npm
      - recompiling js
      - --core-mode
      - enabling/disabling extensions
    - getting started bootstrapping custom plugin
      - Walkthrough of theme plugin
      - Walkthrough of simple mimetype rendering plugin
    - Exercise:
      - Modifying and installing theme plugin
      - and/or
      - Modifying and installing mimetype plugin
    - Point to cookie Cutter.
6. Mention JupyterLab in a multiuser environment: point to jupyterlab docs
7. Mention sprints!
8. 3:50-4:00 QA, Question
