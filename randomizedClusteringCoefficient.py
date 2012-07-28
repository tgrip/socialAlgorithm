#
# Modify `expected_c`
# to return the expected value of C[w,x],
# where C[w,x] is the clustering coefficient
# given w and x - two randomly choosen neighbors of v
#
import itertools

def expected_C(G, v):
    neighbors = G[v].keys()
    degree = len(neighbors)
    if degree == 1: return 0.0
    else: return sum(1.0 for w in neighbors for x in neighbors if x in G[w])/(degree*(degree-1))

def expected_C2(G,v):
    # G[v].keys() is the set of neighbors of v
    neighbors = G[v].keys()
    degree = len(neighbors)
    if degree == 1: return 0.0
    expected = 0.0
    valEveryNode = 2.0 / (degree * (degree -1))
    for (w, x) in itertools.combinations(neighbors, 2):
        if x in G[w].keys():
            expected += valEveryNode
    # x in G[w][x] if x and w are connected in the graph (C[w,x])
    return expected

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def clustering_coefficient(G,v):
    neighbors = G[v].keys()
    if len(neighbors) == 1: return 0.0
    links = 0.0
    for w in neighbors:
        for u in neighbors:
            if u in G[w]: links += 0.5
    return 2.0*links/(len(neighbors)*(len(neighbors)-1))

flights = [(1,2),(1,3),(2,3),(2,6),(2,4),(2,5),(3,6),(4,5)]
G = {}
for (x,y) in flights: make_link(G,x,y)

for v in [1,2,3,4,5,6]:
    print v
    print expected_C(G,v)
    print clustering_coefficient(G,v)

G1 =  {1: {2: 1, 3: 1}, 2: {1: 1, 3: 1, 4: 1, 5: 1, 6: 1}, 3: {1: 1, 2: 1, 6: 1}, 4: {2: 1, 5: 1}, 5: {2: 1, 4: 1}, 6: {2: 1, 3: 1}}
for v in [1,2,3,4,5,6]:
    print v
    print expected_C(G1,v)
    print clustering_coefficient(G1,v)


