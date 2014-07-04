import os
from distutils.dir_util import copy_tree

IPYTHON_PATH = os.path.join("..", "ipython")

def update():
    """Pull the latest documentation from the neighboring /ipython directory.

    This will update the tutorial/example notebooks inside this directory with
    the notebooks in the local IPython repository.  Any changes pulled from
    the ipython directory will overwrite the old contents in this directory.
    This script does not run `git remote update` or `git checkout master` in the
    ipython repository, instead you are responsible for that."""
    destination = os.path.join('examples')
    source = os.path.join(IPYTHON_PATH, 'examples')
    copy_tree(source, destination)
