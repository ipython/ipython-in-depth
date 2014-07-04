from IPython.html.widgets import *
from IPython.display import display
w = RadioButtonsWidget(values={"Left": 0, "Center": 1, "Right": 2}, description="Alignment:")
display(w)

print(w.value)
w.value = 1
