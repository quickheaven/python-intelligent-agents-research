import matplotlib.pyplot as plt
import networkx as nx

"""
Get Node Degree and Node Neighbors in Python | NetworkX Tutorial Part 04
"""

G = nx.Graph()
G.graph["Name"] = "My Graph"

G.add_nodes_from([
    ("A", {"Age": 19, "Gender": "F"}),
    ("B", {"Age": 18, "Gender": "M"}),
    ("C", {"Age": 22, "Gender": "M"}),
    ("D", {"Age": 21, "Gender": "M"}),
    ("E", {"Age": 20, "Gender": "F"})
])

G.add_edges_from([
    ("A", "C", {"weight": 1}),
    ("B", "C", {"weight": 0.5}),
    ("B", "D", {"weight": 0.6}),
    ("C", "D", {"weight": 0.8}),
    ("D", "E", {"weight": 1})
])

pos = {  # Position of the nodes
    "A": (1, 5),
    "B": (4.5, 6.6),
    "C": (3.6, 1.4),
    "D": (5.8, 3.5),
    "E": (7.9, 3.6)
}

# Nodes
for node in G.nodes(data=True):
    print(node)

# Edges
for edge in G.edges(data=True):
    print(edge)

print(f"#Nodes: {G.number_of_nodes()}")
print(f"#Edges: {G.number_of_edges()}")

# Calculate each degree (number of edges connected to node) of each node.
for node in G.nodes:
    print(f"Degree ({node})={G.degree(node)}")

# Calculate neighbors of the node.
for node in G.nodes:
    neighbor_list = [n for n in G.neighbors(node)]  # List of comprehension
    print(f"Neighbor({node})={neighbor_list}")
