import matplotlib.pyplot as plt
import networkx as nx

"""
How to Draw Attributed Graph in Python | NetworkX Tutorial Part 05
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

# pos_node_attributes = {
#     "A": (-0.2, 5),
#     "B": (4.5, 7.5),
#     "C": (2.4, 1.4),
#     "D": (5.8, 2.5),
#     "E": (9.1, 3.6)
# }

# Build the position node attributes using loop instead of hard coding.
pos_node_attributes = {}
for node, (x, y) in pos.items():
    pos_node_attributes[node] = (x, y - 0.9)

# for n, d in G.nodes(data=True):
#     print(n)
#     print(d)

node_labels = {n: (d["Age"], d["Gender"]) for n, d in G.nodes(data=True)}

# for u, v, d in G.edges(data=True):
#    print(u, v)
#    print(d)

edge_labels = {(u, v): d["weight"] for u, v, d in G.edges(data=True)}

nx.draw_networkx(G, pos=pos, with_labels=True,
                 node_color="red", node_size=3000,
                 font_color="white", font_size="20", font_family="Times New Roman", font_weight="bold",
                 edge_color="lightgray",
                 width=5)

nx.draw_networkx_labels(G, pos=pos_node_attributes, labels=node_labels,
                        font_color="black", font_size="12", font_family="Times New Roman",
                        font_weight="bold", )
nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels, label_pos=0.5)

plt.margins(0.2)
plt.show()
