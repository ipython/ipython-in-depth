# To parallelize every call with map, you just need to get a list for each argument.
# You can use `itertools.product` + `zip` to get this:


import itertools

product = list(itertools.product(widths, heights))
# [(1, 6), (1, 7), (2, 6), (2, 7), (3, 6), (3, 7)]

# So we have a "list of pairs", 
# but what we really want is a single list for each argument, i.e. a "pair of lists".
# This is exactly what the slightly weird `zip(*product)` syntax gets us:

allwidths, allheights = zip(*itertools.product(widths, heights))

print " widths", allwidths
print "heights", allheights

# Now we just map our function onto those two lists, to parallelize nested for loops:

ar = lview.map_async(area, allwidths, allheights)
