# -*- coding: utf-8 -*-
import time

class TicToc(object):
    def __init__(self):
        self.tic()

    def tic(self, line=''):
        self.t0 = time.time()

    def toc(self, line=''):
        print self.format_time(time.time() - self.t0)

    def format_time(self, dt):
        if dt < 1e-6:
            return u"%.3g ns" % (dt * 1e9)
        elif dt < 1e-3:
            return u"%.3g µs" % (dt * 1e6)
        elif dt < 1:
            return u"%.3g ms" % (dt * 1e3)
        else:
            return "%.3g s" % dt

tictoc = TicToc()

ip = get_ipython()
ip.register_magic_function(tictoc.tic)
ip.register_magic_function(tictoc.toc)
