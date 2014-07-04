class ItalicStr(str):
    def _repr_html_(self):
        return '<i>%s</i>' % self
    
ItalicStr('Hello World')