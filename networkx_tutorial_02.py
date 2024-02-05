import matplotlib.pyplot as plt
import networkx as nx

"""
How to add nodes and edges to a graph in Python | NetworkX Tutorial Part 02
"""

G = nx.Graph()

# More simple ways to add nodes and edges.

# Option 1:
# G.add_nodes_from(["A", "B", "C", "D", "E"])
# G.add_edges_from([("A", "C"), ("B", "C"), ("B", "D"), ("C", "D"), ("D", "E")])

# Option 2:
# G.add_nodes_from("ABCDE")
# G.add_edges_from(["AC", "BC", "BD", "CD", "DE"])

# pos = {  # Position of the nodes
#    "A": (1, 5),
#    "B": (4.5, 6.6),
#    "C": (3.6, 1.4),
#    "D": (5.8, 3.5),
#    "E": (7.9, 3.6)
# }

# ### Used numbers as nodes.
G.add_nodes_from([1, 2, 3, 4, 5])
G.add_edges_from([(1, 3), (2, 3), (2, 4), (3, 4), (4, 5)])

pos = {  # Position of the nodes
    1: (1, 5),
    2: (4.5, 6.6),
    3: (3.6, 1.4),
    4: (5.8, 3.5),
    5: (7.9, 3.6)
}

# Drawing Process
nx.draw_networkx(G, pos=pos,
                 node_color="red", node_size=3000, with_labels=True,
                 font_color="white", font_size="20", font_family="Times New Roman",
                 font_weight="bold",
                 width=5  # For the edge
                 )
plt.margins(0.2)
plt.show()
