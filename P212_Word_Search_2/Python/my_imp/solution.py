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

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Time: O(M(4*3^(L-1))) | Space: O(M)
        # Where M is the number of cells in the board.
        # L is the maximum length of words.
        # https://leetcode.com/problems/word-search-ii/editorial/

        trie = {}
        for word in words:
            node = trie
            for letter in word:
                # retrieve the next node; If not found, create a empty node.
                node = node.setdefault(letter, {})
            # mark the existence of a word in trie node
            node[WORD_KEY] = word

        rowNum = len(board)
        colNum = len(board[0])

        matchedWords = []

        def backtracking(row, col, parent):

            letter = board[row][col]
            currNode = parent[letter]

            # check if we find a match of word
            word_match = currNode.pop(WORD_KEY, False)
            if word_match:
                # also we removed the matched word to avoid duplicates,
                #   as well as avoiding using set() for results.
                matchedWords.append(word_match)

            # Before the EXPLORATION, mark the cell as visited
            board[row][col] = "#"

            # Explore the neighbors in 4 directions, i.e. up, right, down, left
            for rowOffset, colOffset in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = row + rowOffset, col + colOffset
                if (
                    newRow < 0
                    or newRow >= rowNum
                    or newCol < 0
                    or newCol >= colNum
                ):
                    continue
                if not board[newRow][newCol] in currNode:
                    continue
                backtracking(newRow, newCol, currNode)

            # End of EXPLORATION, we restore the cell
            board[row][col] = letter

            # Optimization: incrementally remove the matched leaf node in Trie.
            if not currNode:
                parent.pop(letter)

        for row in range(rowNum):
            for col in range(colNum):
                # starting from each of the cells
                if board[row][col] in trie:
                    backtracking(row, col, trie)

        return matchedWords