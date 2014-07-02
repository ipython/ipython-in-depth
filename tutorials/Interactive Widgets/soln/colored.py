from IPython.html.widgets import *
w = HTMLWidget(value="Hello world!")
w.set_css({
    'background': 'red',
    'color': 'yellow',
})
w