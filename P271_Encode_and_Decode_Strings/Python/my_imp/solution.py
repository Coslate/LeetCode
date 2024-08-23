from typing import Optional, List, Tuple, Dict, Deque, Set, Self
import collections
import math
from numpy.linalg import matrix_power
import numpy as np
import heapq


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        # Chunked Transfer Encoding | O(n) | O(k)
        # n is the totoal length of all characters over strs.
        # k is the number of string in strs.

        encoded_str = ""
        for string in strs:
            encoded_str += str(len(string)) + '/:' + string

        return encoded_str

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        # Chunked Transfer Decoding | O(n) | O(k)
        # n is the totoal length of all characters over strs.
        # k is the number of string in strs.
        i = 0
        recovered_str_array = []
        while i < len(s):
            delim = s.find('/:', i)
            length = int(s[i:delim])
            sub_string = s[delim+2 : delim+2+length]
            recovered_str_array.append(sub_string)
            i = delim+2+length

        return recovered_str_array






