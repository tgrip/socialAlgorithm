#
# Write `max`
#

def max(L):
    # return the maximum value in L
    max = L[0]
    for i in range(1, len(L)):
        if L[i] > max:
            max = L[i]
    return max

def test():
    L = [1, 2, 3, 4]
    assert 4 == max(L)
    L = [3, 6, 10, 9, 3]
    assert 10 == max(L)

test()