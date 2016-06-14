from ipywidgets import *
from IPython.display import display
from traitlets import link
code = Textarea(description="Source:", value="Cool math: $\\frac{F}{m}=a$")
preview = Latex()
display(code, preview)
mylink = link((code, 'value'), (preview, 'value'))
