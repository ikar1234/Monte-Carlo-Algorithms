"""
Ukkonen's algorithm for approximate pattern matching takes space proportional to the length of the text and the pattern.
Also it doesn't work with scores(?).
I will try to design a Metropolis Hastings optimization algorithm for finding the best scoring hit.
"""
import numpy as np
from matplotlib import pyplot as plt
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
    k = np.random.randint(low=0,high=t-p)
    init_score = pairwise2.align.globalxx(text[k:k+p], pattern)[0][2]
    Max = namedtuple('Max', ['position', 'score'])
    m = Max(k, init_score)
    for _ in range(n):
        # generate candidate position
        k = np.random.randint(low=0, high=t - p)
        score = pairwise2.align.globalxx(text[k:k + p], pattern)[0][2]
        delta = init_score-score
        a = np.random.random(1)
        # acceptance probability
        prob = np.exp(-delta/temp)
        acc = a < prob
        if delta < 0 or acc:
            init_score = score
            m = Max(k,init_score)
            temp *= beta

    return m


# test data
with open('Drosophila.txt','r') as f:
    txt = f.read()
    pat = "AGGAAATTGTATATACTTTGTTCATTTTTGACTGTGATATTTTGTTTTTCCAGTATTGTT"
    print(mh(txt,pat,n=400))



