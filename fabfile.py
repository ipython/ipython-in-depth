from __future__ import print_function
import yaml
import os
import shutil

IPYTHON_PATH = os.path.join("..", "ipython")

def _recursive_copy(tree, path=''):
    if isinstance(tree, (str, unicode)):
        old_file = os.path.join('notebooks', path, tree)
        new_file = os.path.join(IPYTHON_PATH, 'examples', path, tree)
        if os.path.isfile(new_file):
            shutil.copy(new_file, old_file)
            print('Copied "{0}" to "{1}".'.format(new_file, old_file))
        else:
            print('File "{0}" not found, your whitelist.yml is probably incorrect or old.'.format(new_file))
    elif isinstance(tree, (list, tuple)):
        return [_recursive_copy(v, path) for v in tree]
    else:
        return [_recursive_copy(v, os.path.join(path, k)) for k, v in tree.items()]


def update():
    """Pull the latest documentation from the neighboring /ipython directory.

    This will update the tutorial/example notebooks inside this directory with
    the notebooks listed in the whitelist.yml file.  Any changes pulled from
    the ipython directory will overwrite the old contents in this directory.
    This script does not run `git remote update` or `git checkout master` in the
    ipython repository, instead you are responsible for that."""
    with open('whitelist.yml', 'r') as f:
        _recursive_copy(yaml.load(f))
