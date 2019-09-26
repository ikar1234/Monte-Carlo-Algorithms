"""
Ukkonen's algorithm for approximate pattern matching takes approximately O(p^2) space, where p is pattern length.
Moreover, the original algorithm doesn't work with scores.
I will try to design a Metropolis Hastings optimization algorithm, better known as Simulated Annealing, for finding
the best scoring hit.
"""
import numpy as np
from Bio import pairwise2
from collections import namedtuple


def mh(text: str, pattern: str, n: int = 100, temp=2.0, beta=0.9):
    """
    @:param n : number of operations
    :return: List of starting positions
    """
    t = len(text)
    p = len(pattern)
    # initial position
    k = np.random.randint(low=0, high=t-p)
    init_score = pairwise2.align.globalxx(text[k:k+p], pattern)[0][2]
    Match = namedtuple('Match', ['position', 'score'])
    m = Match({k}, init_score)
    for _ in range(n):
        # generate candidate position
        k = np.random.randint(low=0, high=t - p)
        score = pairwise2.align.globalxx(text[k:k + p], pattern)[0][2]
        delta = init_score-score
        # acceptance probability
        prob = np.exp(-delta/temp)
        acc = np.random.random(1) < prob
        if delta < 0 or acc:
            if init_score==score:
                m[0].add(k)
            else:
                init_score = score
                m = Match({k}, init_score)
            temp *= beta

    return m


# test data
with open('Drosophila.txt','r') as f:
    txt = f.read()
    pat = "AGGAAATTGTATATACTTTGTTCATTTTTGACTGTGATATTTTGTTTTTCCAGTATTGTT"
    print(mh(txt,pat,n=400))



