from ipywidgets import *
w = Text()
def handle_submit(sender):
    print(sender.value)
    sender.value = ''
w.on_submit(handle_submit)
w
