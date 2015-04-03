from IPython.html.widgets import *
from IPython.display import display
from IPython.utils.traitlets import link
code = Textarea(description="Source:", value="Cool math: $\\frac{F}{m}=a$")
preview = Latex()
display(code, preview)
mylink = link((code, 'value'), (preview, 'value'))
