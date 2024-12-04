import json
import networkx as nx
import matplotlib.pyplot as plt

with open('The_Match_Team.json', 'r') as file:
    data = json.load(file)
# Print the data
# print(data)

import networkx as nx
G = nx.DiGraph()
# Create nodes
counter = 0
edge_count=0
for element in data:
    G.add_nodes_from([(counter, element)])
    counter += 1


donor_recipient_compatibility = {'O': ['O', 'A', 'B', 'AB'], 'A': ['A', 'AB'], 'B':['B', 'AB'], 'AB':['AB']}

# Create edges (relations)
for node in G.nodes:
    donors = G.nodes[node]['Donor']
    for donor in donors:
        for vertex in G.nodes:
            if node == vertex: continue
            recipient = G.nodes[vertex]['Recipient']
            if recipient not in donor_recipient_compatibility[donor]: continue
            G.add_edge(node, vertex)    
            edge_count += 1   

print('edge count:', edge_count)
# print('edges:', G.edges)   

# Find cycles of length 3
potential_cycle_3 = []
H = G.to_undirected()
for (u,v) in H.edges:
    for k in nx.common_neighbors(H, u, v):
        potential_cycle_3.append((u,v,k))       
# print("potential_cycle_3:", potential_cycle_3)        
        
cycle_3 = [] 
c3=0
for (u,v,k) in potential_cycle_3:
    if (u,v) in G.edges and (v,k) in G.edges and (k,u) in G.edges:
        cycle_3.append((u,v,k,u))
    if (v,u) in G.edges and (u,k) in G.edges and (k,v) in G.edges: 
        cycle_3.append((v,u,k,v))
    c3=c3+1
print("cycle_3:", c3) 

# Find cycles of length 2
count_2=0
cycle_2 = []
for (i,j) in G.edges:
    G.edges[(i,j)]["visited"] = False

for (i,j) in G.edges:
    if G.edges[(i,j)]["visited"] == True: continue
    if (j,i) in G.edges:
        cycle_2.append((i,j,i))
        G.edges[(j,i)]["visited"] = True
        count_2 = count_2+1   
# print("cycles of length 2:", cycle_2)ls
print(count_2)

# Find cycles of length 2

cycle_2 = []
c=0
for (u,v) in H.edges:
    if (u,v) in G.edges and (v,u) in G.edges:
        cycle_2.append((u,v,u))
        c=c+1    
# print("cycles of length 2:", cycle_2)
print(c)

# Let's find a maximum matching
import gurobipy as gp
from gurobipy import GRB

# Create model object
m = gp.Model()

# Create variable for each edge
x = m.addVars(G.edges, vtype=GRB.BINARY)

# Objective function: maximize number of edges
m.setObjective(gp.quicksum(x[e] for e in G.edges), GRB.MAXIMIZE)

# The number of incomming arcs to each vertex is at most one
m.addConstrs(gp.quicksum(x[(u,v)] for u in G.neighbors(v) if (u,v) in G.edges) <= 1 for v in G.nodes)

# The number of incomming arcs should be equal to the number of outgoing arcs
m.addConstrs(gp.quicksum(x[(u,v)] for u in G.neighbors(v) if (u,v) in G.edges) == gp.quicksum(x[(v,u)] for u in G.neighbors(v) if (v,u) in G.edges) for v in G.nodes)

# Solve
m.optimize()
