def plot_scale_magic(line, cell):
    """run a cell block with a variety of input values,

    and plot the result.
    """
    name, values = parse_magic_line(line)
    ns = get_ipython().user_ns
    times = []
    for v in values:
        assignment = "%s=%r" % (name, v)
        print assignment
        ns[name] = v
        sys.stdout.flush()
        tic = time.time()
        exec cell in ns
        toc = time.time()
        dt = toc - tic
        times.append(dt)
        print "%.3f ms" % (1000 * dt)
        sys.stdout.flush()
    plot_scale(values, times, name)

ip.register_magic_function(plot_scale_magic, "cell", "plotscale")