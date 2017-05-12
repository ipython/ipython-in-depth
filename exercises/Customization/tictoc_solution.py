import datetime
import time

@register_line_magic
def tictoc(line):
    tic = datetime.datetime.now()
    exec(compile(line, '<dummy>', 'exec'), globals())
    toc = datetime.datetime.now()
    return (toc-tic).total_seconds()
    