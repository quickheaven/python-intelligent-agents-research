import matplotlib.pyplot as plt
import networkx as nx

"""
How to add attributes to Nodes, Edges and Graph in Python | NetworkX Tutorial Part 03
"""

G = nx.Graph()

G.graph["Name"] = "My Graph"

# Option 1:
# G.add_node("A", Age=19, Gender="F")
# G.add_node("B", Age=18, Gender="M")
# G.add_node("C", Age=22, Gender="M")
# G.add_node("D", Age=21, Gender="M")
# G.add_node("E", Age=20, Gender="F")

# Option 2:
G.add_nodes_from([
    ("A", {"Age": 19, "Gender": "F"}),
    ("B", {"Age": 18, "Gender": "M"}),
    ("C", {"Age": 22, "Gender": "M"}),
    ("D", {"Age": 21, "Gender": "M"}),
    ("E", {"Age": 20, "Gender": "F"})
])

# Option 1:
# G.add_edge("A", "C", weight=1)
# G.add_edge("B", "C", weight=0.5)
# G.add_edge("B", "D", weight=0.6)
# G.add_edge("C", "D", weight=0.8)
# G.add_edge("D", "E", weight=1)

# Option 2:
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

# Access nodes and edges
print(G.nodes["A"])
print(G.edges[("A", "C")])

# Access graph feature
print(G.graph)

#
print(G.nodes["C"])
print(G.edges[("C", "D")])

# Drawing Process
nx.draw_networkx(G, pos=pos,
                 node_color="red", node_size=3000, with_labels=True,
                 font_color="white", font_size="20", font_family="Times New Roman",
                 font_weight="bold",
                 width=5  # For the edge
                 )
plt.margins(0.2)
plt.show()
