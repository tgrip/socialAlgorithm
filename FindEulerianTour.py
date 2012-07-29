
__author__ = 'Theo'

# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]
def get_degree(tour):
    degree = {}
    for x, y in tour:
        degree[x] = degree.get(x, 0) + 1
        degree[y] = degree.get(y, 0) + 1
    return degree

def find_eulerian_tour(graph):
    # your code here
    degree = get_degree(graph)
    highDegreeNumber = max(degree, key=degree.get)
    element = filter(lambda el: el[0] == highDegreeNumber, graph)[0]
    result = [highDegreeNumber]
    last = element[1]
    visited = []
    while element:
        visited.append(element)
        result.append(last)
        (element, last) = findInGraph(graph, last, visited)
#        print 'next element we search for', element, last
        #print next
    return result

def findInGraph(graph, startNode, visited):
    nextToVisit = []
    for index, node in enumerate(graph):
        if node not in visited:
            if startNode in (node[0], node[1]):
                nextToVisit.append(node)
    allVisitedElements = []
    for tuple in visited:
        allVisitedElements += list(tuple)
    minCount = 999
    nextElement = 0
    nextVal = 0
    for element in nextToVisit:
        val = element[0] if element[1] == startNode else element[1]
        count = allVisitedElements.count(val)
        if not count:
            return element, val
        if count < minCount:
            minCount = count
            nextElement = element
            nextVal = val
    return nextElement, nextVal


print find_eulerian_tour([(1, 2), (2, 3), (3, 1)])
print
print
print 'next tour'
print find_eulerian_tour([(0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6), (3, 7), (5, 9), (2, 4), (0, 4), (2, 5),
    (3, 6), (8, 9)])