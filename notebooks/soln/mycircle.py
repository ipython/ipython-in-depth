class MyCircle(object):
    
    def _repr_html_(self):
        return "&#x25CB;"

    def _repr_svg_(self):
        return """<svg width=100px height=100px>
           <circle cx="50" cy="50" r="20" stroke="black" stroke-width="1" fill="white"/>
        </svg>"""
    
    def _repr_latex_(self):
        return r"$\bigcirc$"

    def _repr_javascript_(self):
        return "alert('I am a circle!');"