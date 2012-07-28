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

def find_eulerian_tour(graph):
    # your code here
    result = []
    element = graph.pop(0)
    last = element[1]
    while element:
        result.append(element)
        #last = lastNumber(result)
        (element, last) = findInGraph(graph, last, result)
        print 'next element we search for', element, last
        #print next
    return result

def findInGraph(graph, startNode, visited):
    nextToVisit = []
    for index, node in enumerate(graph):
        if node not in visited:
            if startNode == node[0]:
                nextElement = graph.pop(index)
                return nextElement, nextElement[1]
            if startNode == node[1]:
                nextElement = graph.pop(index)
                return nextElement, nextElement[0]
    return 0, 0

def lastNumber(visited):
    last = visited[-1]
    print 'letzter', last
    if len(visited) == 1:
        return last[1]
    vorletzter = visited[-2]
    print 'vorletzter', vorletzter
    if vorletzter[1] == last[0]:
        return last[1]
    else:
        return last[0]

print find_eulerian_tour([(1, 2), (2, 3), (3, 1)])
print
print
print 'next tour'
print find_eulerian_tour([(0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6), (3, 7), (5, 9), (2, 4), (0, 4), (2, 5),
    (3, 6), (8, 9)])