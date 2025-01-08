#! /usr/bin/env python3

from solution import *

def main():
    print(f"//Case1:")
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words = ["oath","pea","eat","rain"]
    ans = Solution().findWords(board=board, words=words)
    print(f"ans = {ans}")
    print(f"//Case2:")
    board = [["a","b"],["c","d"]]
    words = ["abcb"]
    ans = Solution().findWords(board=board, words=words)
    print(f"ans = {ans}")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
