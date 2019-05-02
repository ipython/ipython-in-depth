class MyCircle(object):

    def __init__(self, center=(0.0,0.0), radius=1.0, color='blue'):
        self.center = center
        self.radius = radius
        self.color = color

    def _repr_html_(self):
        return "&#x25CB; (<b>html</b>)"

    # Let's ignore that for now due to a bug in JupyterLab
    # def _repr_svg_(self):
    #     return """<svg width="100px" height="100px">
    #        <circle cx="50" cy="50" r="20" stroke="black" stroke-width="1" fill="blue"/>
    #     </svg>"""
    
    def _repr_latex_(self):
        return r"$\bigcirc \LaTeX$"
