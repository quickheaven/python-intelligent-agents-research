import matplotlib.pyplot as plt
import networkx as nx

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


source_node = "A"
target_node = "D"
shortest_path = nx.astar_path(G, source_node, target_node)
print(shortest_path)

nx.draw_networkx(G, pos=pos,
                 node_color="red", node_size=3000, with_labels=True,
                 font_color="white", font_size="20", font_family="Times New Roman",
                 font_weight="bold",
                 width=5
                 )
plt.margins(0.2)
plt.show()
