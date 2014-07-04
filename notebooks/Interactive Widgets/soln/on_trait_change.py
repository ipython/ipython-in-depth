from IPython.html.widgets import *
w = TextWidget()
def handle_submit(name, new):
    print(new)
w.on_trait_change(handle_submit, 'value')
w