import matplotlib.pyplot as plt
import networkx as nx

import numpy as np
import random

seed = 0
# networkx used random module and numpy package
random.seed(seed)
np.random.seed(seed)

G = nx.Graph()
G.graph["Name"] = "My Graph"

G.add_nodes_from(
    [
        ((0, 0), {'orientation': 'East'}),
        ((0, 1), {'orientation': 'East'}),
        ((1, 0), {'orientation': 'North'}),
        ((2, 0), {'orientation': 'North'}),
        ((3, 0), {'orientation': 'North'}),
        ((2, 0), {'orientation': 'South'}),
        ((1, 0), {'orientation': 'South'}),
        ((1, 1), {'orientation': 'East'}),
        ((2, 1), {'orientation': 'North'}),
        ((2, 2), {'orientation': 'East'}),
        ((2, 3), {'orientation': 'East'}),
        ((2, 3), {'orientation': 'South'}),
        ((1, 3), {'orientation': 'South'}),
        ((0, 2), {'orientation': 'West'}),
        ((0, 2), {'orientation': 'West'}),
        ((0, 1), {'orientation': 'West'})
    ])

G.add_edges_from([
    ((0, 0), (0, 1)),
    ((0, 0), (1, 0)),
    ((1, 0), (2, 0)),
    ((2, 0), (3, 0)),
    ((3, 0), (2, 0)),
    ((2, 0), (1, 0)),
    ((1, 0), (1, 1)),
    ((1, 1), (2, 1)),
    ((2, 1), (2, 2)),
    ((2, 2), (2, 3)),
    ((2, 3), (1, 3)),
    ((1, 3), (0, 3)),
    ((0, 3), (0, 2)),
    #
    ((0, 2), (0, 1)),
    ((0, 1), (0, 0))
])


# pos = {  # Position of the nodes
#     "A": (1, 5),
#     "B": (4.5, 6.6),
#     "C": (3.6, 1.4),
#     "D": (5.8, 3.5),
#     "E": (7.9, 3.6)
# }

# https://datascienceparichay.com/article/manhattan-distance-python/
# Option 1
def get_manhattan_distance_v1(a, b):
    (x1, y1) = a
    (x2, y2) = b
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2)
    print('({},{}) distance: {}'.format(a, b, distance))
    return distance

# Option 2
def get_manhattan_distance_v2(p, q):
    # sum of absolute difference between coordinates
    distance1 = 0
    for p_i, q_i in zip(p, q):
        distance1 += abs(p_i - q_i)
    print('({},{}) distance: {}'.format(p, q, distance1))
    return distance1

# Option 3
from scipy.spatial import distance
# distance.cityblock

source_node = (1, 3)
target_node = (0, 0)
shortest_path = nx.astar_path(G, source_node, target_node, heuristic=distance.cityblock)
print(shortest_path)

nx.draw_networkx(G,  # pos=pos,
                 node_color="red", node_size=3000, with_labels=True,
                 font_color="white", font_size="20", font_family="Times New Roman",
                 font_weight="bold",
                 width=5
                 )
plt.margins(0.2)
plt.show()


