import itertools

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G


file = open('marvel.txt')

G = {}
books = set([])
i = 0
for line in file:
    (hero, book) = line.split('\t')
    make_link(G, hero, book)
    books.add(book)

heroConections = {}
for book in books:
        heroesInBook = G[book].keys()
        for heroPair in itertools.combinations(heroesInBook, 2):
            oldVal = heroConections.get(heroPair, 0)
            heroConections[heroPair] = oldVal + 1

for heroes in sorted(heroConections, key=heroConections.get, reverse=True):
    if i < 5:
        print heroes, heroConections[heroes]
    i +=1



