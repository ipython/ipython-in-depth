def pdot(v, A, B):
    v['B'] = B # push B everywhere
    v.scatter('A', A) # scatter A
    v.execute('C=A.dot(B)') # compute the dot-product
    return v.gather('C', block=True) # gather the resulting sub-arrays
