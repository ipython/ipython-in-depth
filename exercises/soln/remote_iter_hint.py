from IPython.display import display

t_minus = range(10,0,-1)

def lazy_iterator(name):
    seq = eval(name)
    it = iter(seq)
    while True:
        try:
            yield it.next()
        # this looks silly locally, but it will be useful for the remote version:
        except StopIteration:
            raise StopIteration

lzit = lazy_iterator('t_minus')
display(lzit)
list(lzit)