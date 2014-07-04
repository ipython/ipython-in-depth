from IPython.html.widgets import *
from IPython.display import display
sliders = [FloatSliderWidget(description=str(i), orientation="vertical", value=50.) for i in range(10)]
container = ContainerWidget(children=sliders)
display(container)
container.remove_class('vbox')
container.add_class('hbox')