__author__ = 'Theo'

def clique(n):
    print "in a clique.."
    for i in range(n):
        for j in range(i):
            print i, " is friends with ", j

def count(n):
    # Your code here to count the units of time
    # it takes to execute clique

    sequence = range(n)
    print sequence
    return n + 2 + sum(range(n))

result = count(5)
print result
#assert 16 == result
result = count(4)
print result