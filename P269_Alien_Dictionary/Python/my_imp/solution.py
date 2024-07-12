from typing import Optional, List, Tuple
import math
from numpy.linalg import matrix_power
import numpy as np

from collections import deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # BFS | Time: O(C) | Space: O(1) or O(U+min(U^2, N)),
        # C is the total number of character across all words,
        # U is the number of unique characters,
        # and N is the number of word in words.

        adj_list = {c:[] for word in words for c in word}
        in_degree = {c:0 for word in words for c in word}

        #Step1. Extract relationship of words into graph (adj_list).
        for word0, word1 in zip(words, words[1:]):
            for index, (c, d) in enumerate(zip(word0, word1)):
                if c != d:
                    if d not in adj_list[c]:
                        adj_list[c].append(d)
                        in_degree[d] += 1
                    break
                else:
                    if index == len(word0)-1 or index == len(word1)-1:
                        if len(word1) < len(word0):
                            return ""

        #Step2. Repeatedly take off nodes with indegree of 0.
        # O(V+E), V = U, E = min(U^2, N-1)
        output = []
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        while queue:
            c = queue.popleft()
            output.append(c)
            for d in adj_list[c]:
                in_degree[d] -= 1
                if in_degree[d] == 0:
                    queue.append(d)

        #Step3. If not all letters are in output, then there is a cycle -> no valid ordering.
        if len(output) < len(in_degree):
            return ""


        #Step4. Convert the ordering we found into a string and return it.
        return "".join(output)


class OptSolution:
    def alienOrder(self, words: List[str]) -> str:
        # UnionFind | Time: O(m*n) | Space: O(m*n), n is the height of heights, and m is
        # the width of heights.
        pass


























