import matplotlib.pyplot as plt
import networkx as nx

"""
How to create an Undirected Graph using Python | NetworkX Tutorial Part 01
"""

# import numpy as np
# import random

# seed = 0
# networkx used random module and numpy package
# random.seed(seed)
# np.random.seed(seed)

G = nx.Graph()

# G.add_edge("A", "C")
# G.add_edge("B", "C")
# G.add_edge("B", "D")
# G.add_edge("C", "D")
# G.add_edge("D", "E")

G.add_edge("A", "C")
G.add_edge("B", "C")
G.add_edge("B", "D")
G.add_edge("C", "D")
G.add_edge("D", "E")

pos = {  # Position of the nodes
    "A": (1, 5),
    "B": (4.5, 6.6),
    "C": (3.6, 1.4),
    "D": (5.8, 3.5),
    "E": (7.9, 3.6)
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
