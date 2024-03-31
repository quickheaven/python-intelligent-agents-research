from pomegranate.distributions import Categorical
from pomegranate.distributions import ConditionalCategorical
from pomegranate.bayesian_network import BayesianNetwork
import numpy
import torch


# pit01 = Categorical([[0.8, 0.2]])


class Predicate():
    def __init__(self, prob: float):
        self.p = prob

    def toList(self):
        return [1 - self.p, self.p]

    def toCategorical(self):
        return Categorical([self.toList()])


# pit01 = Predicate(0.2).toCategorical()
# pit02 = Predicate(0.2).toCategorical()
# pit03 = Predicate(0.2).toCategorical()
# pit04 = Predicate(0.2).toCategorical()

pit01 = Categorical([[0.8, 0.2]])
pit02 = Categorical([[0.8, 0.2]])
pit03 = Categorical([[0.8, 0.2]])
pit04 = Categorical([[0.8, 0.2]])
"""
breeze = ConditionalCategorical([[
    [
        [[1.0, 0.0], [0.0, 1.0]],
        [[0.0, 1.0], [0.0, 1.0]]
    ],
    [
        [[1.0, 0.0], [0.0, 1.0]],
        [[0.0, 1.0], [0.0, 1.0]]
    ]
]])
variables = [pit01, pit02, pit03, breeze]
edges = [(pit01, breeze), (pit02, breeze), (pit03, breeze)]

"""
breeze = ConditionalCategorical([[
    [
        [
            [[1.0, 0.0], [0.0, 1.0]],
            [[0.0, 1.0], [0.0, 1.0]]
        ],
        [
            [[1.0, 0.0], [0.0, 1.0]],
            [[0.0, 1.0], [0.0, 1.0]]
        ]
    ],
    [
        [
            [[1.0, 0.0], [0.0, 1.0]],
            [[0.0, 1.0], [0.0, 1.0]]
        ],
        [
            [[1.0, 0.0], [0.0, 1.0]],
            [[0.0, 1.0], [0.0, 1.0]]
        ]
    ]
]])

variables = [pit01, pit02, pit03, pit04, breeze]
edges = [(pit01, breeze), (pit02, breeze), (pit03, breeze), (pit04, breeze)]

print('variables shape', numpy.array(variables).shape)
print('edges shape', numpy.array(edges).shape)

pits_model = BayesianNetwork(variables, edges)
"""
X = torch.tensor([[-1, -1, -1, 0],  # pit12?, pit21?, breeze11 is false
                  [-1, -1, -1, 1],  # pit12?, pit21?, breeze11 is true
                  [-1, -1, -1, -1],  # pit12?, pit21?, breeze11?
                  [1, -1, -1, -1]  # pit12 is true, pit21?, breeze11?
                  ])
"""
X = torch.tensor([[-1, -1, -1, -1, 0],  # pit12?, pit21?, breeze11 is false
                  [-1, -1, -1, -1, 1],  # pit12?, pit21?, breeze11 is true
                  [-1, -1, -1, -1, -1],  # pit12?, pit21?, breeze11?
                  [1, -1, -1, -1, -1]  # pit12 is true, pit21?, breeze11?
                  ])
print(X.shape)

X_masked = torch.masked.MaskedTensor(X, mask=X >= 0)

result = pits_model.predict_proba(X_masked)

# [-1, -1, -1, -1, 0]
# IndexError: tuple index out of range

# ValueError: X.shape[1] must match the number of marginals. --> Pag d match ung
# [-1, -1, -1, 0]


print(f"The predict_proba result {result}")

