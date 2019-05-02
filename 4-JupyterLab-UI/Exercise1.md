# Exercises 1

Remove all the sticky notes from your screen :-) and attempt the following.
These are _guidelines_, feel free to err on the side of workflow and
options that suits _you_ if you find them best.

Keep in mind, if something is not intuitive, or not in the place you expected
it, write it down (for example on the red sticky note), and give it to us at the
break.

## View this file as rendered markdown.

Right-click on the `Exercise1.md` file and open it as rendered markdown.

## Layout

Create a new notebook.

Arrange the notebook and rendered markdown side-by-side. Then arrange them, one on top and one on bottom. Then arrange them in a single panel with two tabs. Then split them out again to side-by-side.

## Notebook operations

- Change the first cell to markdown, and write some markdown with
    - Bold
    - italic
    - [Math](https://math.meta.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference) (inlne and formulas): `$f(x) =  a.x^2+b.x+c$`, `$$x_\pm = \frac{-b \pm \sqrt(b^2-4ac)}{2a}$$`
    - Code (triple backtick fences ` ``` `, or indented 4 spaces)
- Create a code cell and evaluate it, printing "Hello PyCon"
    - Experiment with the run shortcuts `Ctrl-Enter`, `Shift-Enter`, and `Alt-Enter` and note the differences between them (see the Run menu for help).
    - try importing `pandas`
    - evaluate `pandas?` to get the help on the pandas library.
    - try `pandas.D<tab>` to get tab completion on the pandas library. Note that completions can take a few second the first time the library get inspected to get result.
    - Complete to `pandas.DataFrame(` place the cursor after the open bracket and press `Shift-Tab` to get quick help.
    - To always see the info about the current function you can open the inspector via the command palette.
        - Use the command palette the find the Keyboard shortcut to open the inspector.
        - Move the inspector tab somewhere so that you can see both it and the notebook.
        - Type `pandas.read_csv(` to see the inspector display function help.
    - Use panda’s `read_csv` to load `'../data/iris.csv'` into a dataframe, display this dataframe
    - open `'../data/iris.csv'` as a standalone CSV file.
    - use `%matpltolib inline` to allow inline graphs, 
    - make a scatter plot of `sepal_length` vs `sepal_width`.


# More advanced notebooks

- Move a cell by dragging.
- Use the View menu, or click the blue bar, to collapse and expand an input and an output.
- Use the context menu to enable scrolling in a cell that has lots of output.
- Try “Create new view for output” in the context menu of an output. Modify and execute the cell again to see the mirrored output update (will learn more in section 2).
- Learn the various keyboard shortcuts through the menu and the command palette.
- Learn more about kernel functionality (more on that in the exercise solution).
