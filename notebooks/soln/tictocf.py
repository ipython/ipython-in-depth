def tic(line):
    global t0
    t0 = time.time()

def toc(line):
    global t0
    print "%.3g s" % (time.time() - t0)

ip = get_ipython()
ip.register_magic_function(tic)
ip.register_magic_function(toc)
