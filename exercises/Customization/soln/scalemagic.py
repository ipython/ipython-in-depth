def scale_magic(line, cell):
    """run a cell block with a variety of input values"""
    name, values = parse_magic_line(line)
    ns = get_ipython().user_ns
    for v in values:
        assignment = "%s=%r" % (name, v)
        print(assignment)
        ns[name] = v
        sys.stdout.flush()
        %tic
        exec(cell, ns)
        %toc

ip = get_ipython()
ip.register_magic_function(scale_magic, "cell", "scale")
