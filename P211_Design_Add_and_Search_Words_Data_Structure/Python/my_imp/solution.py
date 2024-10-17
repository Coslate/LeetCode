from typing import Optional, List, Tuple, Dict, Deque, Set, Self, TypeVar
import collections
import math
import numpy as np
import heapq

char = TypeVar("char", bound=str)

class Trie:
    class TrieNode:
        def __init__(self):
            self._children= {}
            self._isEnd = False
        
        @property
        def isEnd(self) -> bool:
            return self._isEnd
        
        @property
        def children(self) -> Dict[char, 'TrieNode']:
            return self._children

        @isEnd.setter
        def isEnd(self, value: bool) -> None:
            self._isEnd = value

        def put(self, ch: char, node: 'TrieNode') -> None:
            self._children[ch] = node

        def get(self, ch: char) -> 'TrieNode':
            return self._children[ch]
        
        def containsKey(self, ch: char) -> bool:
            return True if ch in self._children else False


    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word: str) -> None:
        # Time: O(n) | Space: O(n)
        # Where n is the length of word
        node = self.root
        for i in range(len(word)):
            if not node.containsKey(word[i]):
                node.put(word[i], self.TrieNode())
            node = node.get(word[i])
        node.isEnd = True
    
    def searchNode(self, word: str, root: Optional[TrieNode], prefix=False) -> bool:
        # Time: O(M) | Space: O(M)
        # Where M is n, the length of word, in best case, no '.' in word.
        # M is 26^n in worst case: all the char in word is '.'
        # To support '.' that match any word.
        node = root

        for i in range(len(word)):
            if node.containsKey(word[i]):
                node = node.get(word[i])
            else:
                # if current char is '.'
                # check all the possible nodes in current level
                if word[i] == '.':
                    result = False
                    for each_child_char in node.children:
                        result = result or self.searchNode(word[i+1 : ], node.children[each_child_char], prefix=prefix)
                    return result
                # else, no match is found.
                return False
        return node.isEnd if not prefix else True

    def search(self, word: str) -> bool:
        return self.searchNode(word, self.root)

    def startsWith(self, prefix: str) -> bool:
        return self.searchNode(prefix, self.root, prefix=True)

class WordDictionary:
    def __init__(self):
        self._trie_ds = Trie()

    def addWord(self, word: str) -> None:
        self._trie_ds.insert(word)

    def search(self, word: str) -> bool:        
        return self._trie_ds.search(word)

