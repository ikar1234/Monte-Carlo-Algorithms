"""
Implementation of Simulated Annealing applied to the TSP problem
"""
import numpy as np

mat = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0],
                [7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0],
                [8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0],
                [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0],
                [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0],
                [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0],
                [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
                ])


class Permutation:
    __slots__ = ['perm', 'n', 'matrix', 'temp', 'beta']

    def __init__(self, perm=None, matrix=mat, temp=2.0, beta=0.9):
        if perm is None:
            perm = list(range(1, 10))

        if matrix.shape[0] != len(perm):
            raise ValueError(f"Matrix and permutation not compatible: {matrix.shape[0]} != {len(perm)}")
        self.perm = perm
        self.n = len(perm)  # permutation length
        self.matrix = matrix
        self.temp = temp    # initial temperature
        self.beta = beta    # cooling parameter

    def gen_perm(self):
        """
        Change the order of 2 random numbers in the permutation
        :return: altered permutation/ new permutation
        """
        a, b = np.random.randint(low=0, high=self.n, size=2)
        new_perm = self.perm.copy()
        new_perm[a], new_perm[b] = new_perm[b], new_perm[a]
        return Permutation(perm=new_perm, matrix=self.matrix, temp=self.temp, beta=self.beta)

    def m(self, i, j):
        # since we have a lower triangular matrix
        return self.matrix[max(i, j), min(i, j)]

    def perm_cost(self):
        # compute cost of a permutation
        cost = [self.m(self.perm[i]-1, self.perm[i - 1]-1) for i in range(1, self.n)]
        return sum(cost)

    def rel_change(self, other):
        if not isinstance(other, Permutation):
            raise AttributeError('Operation not supported for other classes')
        return other.perm_cost() - self.perm_cost()

    def mutate(self):
        # Change the state
        new_perm = self.gen_perm()
        delta = self.rel_change(new_perm)
        a = np.random.random(1)
        prob = np.exp(-delta / self.temp)   # acceptance probability
        acc = a < prob
        if delta < 0 or acc:
            self.perm = new_perm.perm
            self.temp *= self.beta

    def __len__(self):
        return self.n

    def __str__(self):
        return self.perm


p = Permutation([13,1,12,2,11,3,10,4,9,5,8,6,7])
print(f'Cost:{p.perm_cost()}')
for _ in range(1000):
    p.mutate()
print(f'New cost:{p.perm_cost()}')
