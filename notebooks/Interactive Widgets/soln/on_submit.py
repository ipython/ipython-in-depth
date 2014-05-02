from IPython.html.widgets import *
w = TextWidget()
def handle_submit(sender):
    print(sender.value)
w.on_submit(handle_submit)
w
