from ipywidgets import *
from IPython.display import display
w = RadioButtons(options={"Left": 0, "Center": 1, "Right": 2}, description="Alignment:")
display(w)

print(w.value)
w.value = 1
