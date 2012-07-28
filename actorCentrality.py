__author__ = 'Theo'

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def centrality(G, v):
    open = [v]
    distanceFromStart = {}
    distanceFromStart[v] = 0
    while open:
        current = open.pop(0)
        for neighbor in G[current]:
            if neighbor not in distanceFromStart:
                distanceFromStart[neighbor] = distanceFromStart[current] + 1
                open.append(neighbor)
#    print distanceFromStart
    result = float(sum(distanceFromStart.values())) / len(distanceFromStart)
#    print result
    return result

file = open('imdb.tsv')

i = 0
G = {}
actors = set([])
for line in file:
   (actor, movie, year) = line.split('\t')
   fullMovie = movie + year
   make_link(G, actor, fullMovie)
   actors.add(actor)

print len(actors)

actorCentral = {}
for actor in actors:
    central = centrality(G, actor)
    actorCentral[actor] = central
    print actor

print 'actors with centrality'
for actor in sorted(actorCentral, key=actorCentral.get):
    i += 1
    if i < 20:
        print actor, actorCentral[actor]
    if i == 20:
        print actor, actorCentral[actor]