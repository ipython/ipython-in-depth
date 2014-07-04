# -*- coding: utf-8 -*-
import time

def format_time(dt):
    if dt < 1e-6:
        return u"%.3g ns" % (dt * 1e9)
    elif dt < 1e-3:
        return u"%.3g µs" % (dt * 1e6)
    elif dt < 1:
        return u"%.3g ms" % (dt * 1e3)
    else:
        return "%.3g s" % dt

def tic(line):
    global t0
    t0 = time.time()

def toc(line):
    global t0
    print (format_time(time.time() - t0))

ip = get_ipython()
ip.register_magic_function(tic)
ip.register_magic_function(toc)
