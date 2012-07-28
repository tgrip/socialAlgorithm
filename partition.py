#
# Write partition to return a new array with 
# all values less then `v` to the left 
# and all values greater then `v` to the right
#

def partition(L, v):
    P = []
    # your code here
    pos = rank(L, v)
    L.remove(v)
    P.extend(L[:pos])
    P.append(v)
    P.extend(L[pos:])
    return P

def rank(L, v):
    pos = 0
    for val in L:
        if val < v:
            pos += 1
    return pos

L = [2, 5, 4, 8, 6, 9]
print partition(L, 6)
L = [1, 2, 3, 4]
#print partition(L, 5)