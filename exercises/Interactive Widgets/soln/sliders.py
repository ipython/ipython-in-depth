from IPython.html.widgets import *
from IPython.display import display
sliders = [FloatSlider(description=str(i), orientation="vertical", value=50.) for i in range(10)]
container = HBox(children=sliders)
display(container)
