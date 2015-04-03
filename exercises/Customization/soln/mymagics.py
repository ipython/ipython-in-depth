# -*- encoding: utf-8 -*-

import io
import os
import time

import IPython.nbformat as nbf

class TicToc(object):
    def __init__(self):
        self.tic()

    def tic(self, line=''):
        self.t0 = time.time()

    def toc(self, line=''):
        print(self.format_time(time.time() - self.t0))

    def format_time(self, dt):
        if dt < 1e-6:
            return u"%.3g ns" % (dt * 1e9)
        elif dt < 1e-3:
            return u"%.3g µs" % (dt * 1e6)
        elif dt < 1:
            return u"%.3g ms" % (dt * 1e3)
        else:
            return "%.3g s" % dt


def load_notebook(filename):
    """load a notebook object from a filename"""
    if not os.path.exists(filename) and not filename.endswith(".ipynb"):
        filename = filename + ".ipynb"
    with io.open(filename) as f:
        return nbf.read(f, as_version=4)

def nbrun(line):
    """given a filename, execute the notebook in IPython"""
    nb = load_notebook(line)
    ip = get_ipython()
    for cell in nb.cells:
        if cell.cell_type == 'code':
            ip.run_cell(cell.source, silent=True)
    
def load_ipython_extension(ip):
    tictoc = TicToc()
    ip.register_magic_function(tictoc.tic)
    ip.register_magic_function(tictoc.toc)
    ip.register_magic_function(nbrun)
    ip.user_ns['load_notebook'] = load_notebook
    
