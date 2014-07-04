from IPython.html.widgets import *
from IPython.display import display
from IPython.utils.traitlets import link
code = TextareaWidget(description="Source:", value="Cool math: $\\frac{F}{m}=a$")
preview = LatexWidget()
display(code, preview)
mylink = link((code, 'value'), (preview, 'value'))