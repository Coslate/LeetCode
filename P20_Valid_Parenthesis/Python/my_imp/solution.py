from typing import Optional, List, Tuple, Dict, Deque, Set, Self
import collections
import math
from numpy.linalg import matrix_power
import numpy as np
import heapq


class Solution:
    def isValid(self, s: str) -> bool:
        # String | Frequency Counter | Time: O(n) | Space: O(n),
        # Where n is the size of input s.

        #Step0. Initialize a stack.
        self_stack = []

        #Step1. Initialize a set of open bracket: {, [, (, and a map of corresponding close bracket.
        open_bracket = set(['{', '[', '('])
        close_bracket: Dict[str, str] = {'{':'}', '[':']', '(':')'}

        #Step2. Iterate over all char in s. 
        #If the char is in open_bracket set, insert into the stack.
        #Else if the char is the close bracket and match, then pop the stack.
        #Else return False.
        for c in s:
            if c in open_bracket:
                self_stack.append(c)
            elif self_stack and c == close_bracket[self_stack[-1]]:
                self_stack.pop()
            else:
                return False

        #Step3. Return True if stack is empty, else return False.
        return False if self_stack else True

class OptSolution:
    def isValid(self, s: str) -> bool:
        # String | Frequency Counter | Time: O(kn) | Space: O(kn),
        pass

