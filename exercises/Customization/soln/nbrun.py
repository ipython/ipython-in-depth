def nbrun(line):
    """given a filename, execute the notebook in IPython"""
    nb = load_notebook(line)
    ip = get_ipython()
    for cell in nb.cells:
        if cell.cell_type == 'code':
            ip.run_cell(cell.source, silent=True)
    
get_ipython().register_magic_function(nbrun)
