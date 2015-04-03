def sort_string(s, reverse=False):
    s = reversed(sorted(s)) if reverse else sorted(s)
    print(''.join(s))

interact(sort_string, s='Hi', reverse=False);
