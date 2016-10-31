# coding: utf-8
import re
import networkx as nx 
import json

print "Loading json file..."
with open(r'./IMDb_data/IMDb2006-2015.json') as f:
    movie_dict = json.load(f)
print "Finished loading."
print "Building graph..."
G = nx.Graph()
i = 0
report_rate = 5000
while movie_dict.has_key(str(i)):
    if i % report_rate == 0:
        print "Working on movie#:", str(i), "~", str(i+report_rate-1)
    try:
        actors = movie_dict[str(i)]["Actors"].split(', ')
        for n in range(len(actors)):
            name1 = actors[n]
            for name2 in actors[n+1:]:
                if G.has_edge(name1, name2):
                    G[name1][name2]['weight'] += 1
                else:
                    G.add_edge(name1, name2,weight=1)
        i += 1
    except KeyError:
        i += 1
print "Finished building graph..."
print "Outputing to file: \"collgraph.edgelist\"..."
i = 0
while (i < 100000):
    i += 1
f = open('collgraph.edgelist','w')
actors = sorted(G.nodes())
for n in range(len(actors)):
    name1 = actors[n]
    print "Working on neighbors of:", name1
    for name2 in G.neighbors(name1):
        if name1 < name2:
            f.write((name1+","+name2+","+str(G[name1][name2]['weight'])+'\n').encode("UTF-8"))
print "Finished outputing :)"
