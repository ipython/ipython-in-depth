"""A simple embedding of an IPython kernel.
"""
#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

import sys

from IPython.lib.kernel import connect_qtconsole
from IPython.kernel.zmq.kernelapp import IPKernelApp

#-----------------------------------------------------------------------------
# Functions and classes
#-----------------------------------------------------------------------------
class SimpleKernelApp(object):
    """A minimal object that uses an IPython kernel and has a few methods
    to manipulate a namespace and open Qt consoles tied to the kernel.
    """

    def __init__(self, gui):
        # Start IPython kernel with GUI event loop support
        self.ipkernel = IPKernelApp.instance()
        self.ipkernel.initialize(['python', '--gui=%s' % gui,
                                  #'--log-level=10'  # for debugging
                                  ])

        # To create and track active qt consoles
        self.consoles = []
        
        # This application will also act on the shell user namespace
        self.namespace = self.ipkernel.shell.user_ns
        # Keys present at startup so we don't print the entire pylab/numpy
        # namespace when the user clicks the 'namespace' button
        self._init_keys = set(self.namespace.keys())

        # Example: a variable that will be seen by the user in the shell, and
        # that the GUI modifies (the 'Counter++' button increments it):
        self.namespace['app_counter'] = 0

    def print_namespace(self, evt=None):
        print("\n***Variables in User namespace***")
        for k, v in self.namespace.iteritems():
            if k not in self._init_keys and not k.startswith('_'):
                print('%s -> %r' % (k, v))
        sys.stdout.flush()

    def new_qt_console(self, evt=None):
        """start a new qtconsole connected to our kernel"""
        return connect_qtconsole(self.ipkernel.connection_file, 
                                 profile=self.ipkernel.profile)

    def count(self, evt=None):
        self.namespace['app_counter'] += 1

    def cleanup_consoles(self, evt=None):
        for c in self.consoles:
            c.kill()

    def start(self):
        self.ipkernel.start()
