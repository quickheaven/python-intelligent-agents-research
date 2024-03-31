from pomegranate.distributions import Categorical
from pomegranate.distributions import ConditionalCategorical
from pomegranate.bayesian_network import BayesianNetwork

stop_light = Categorical([[0.50, 0.45, 0.05]])

pit12 = Categorical([[0.8, 0.2]])


class Predicate():
    def __init__(self, prob: float):
        self.p = prob

    def toList(self):
        return [1 - self.p, self.p]

    def toCategorical(self):
        return Categorical([self.toList()])


pit12 = Predicate(0.2).toCategorical()
pit21 = Predicate(0.2).toCategorical()

print(pit21)
print(pit21.probs[0][0])
print(pit21.probs[0][1])


breeze11 = ConditionalCategorical([[
    [[1.0, 0.0], [0.0, 1.0]],
    [[0.0, 1.0], [0.0, 1.0]]
]])

cases = []
for p12 in [False, True]:
    c = []
    for p21 in [False, True]:
        case = p12 or p21
        if case:
            p = 1.0
        else:
            p = 0.0
        c.append(Predicate(p).toList())
    cases.append(c)

print(cases)
print(breeze11.probs)

import numpy

breeze11 = ConditionalCategorical([
    cases
])

variables = [pit12, pit21, breeze11]
edges = [(pit12, breeze11), (pit21, breeze11)]

print('variables shape', numpy.array(variables).shape)
print('edges shape', numpy.array(edges).shape)

pits_model = BayesianNetwork(variables, edges)

import torch

X = torch.tensor([[-1, -1, 0],  # pit12?, pit21?, breeze11 is false
                  [-1, -1, 1],  # pit12?, pit21?, breeze11 is true
                  [-1, -1, -1],  # pit12?, pit21?, breeze11?
                  [1, -1, -1]  # pit12 is true, pit21?, breeze11?
                  ])

X_masked = torch.masked.MaskedTensor(X, mask= X >= 0)
print(X_masked.shape)

result = pits_model.predict_proba(X_masked)


