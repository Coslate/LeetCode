#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()

    print(f"//Case1:")
    print(f"//------Original-------//")
    trie = Trie()
    print(f"//------Checked-------//")
    trie.insert("apple")
    search_apple = trie.search("apple")   # return True
    search_app = trie.search("app")     # return False
    startWithapp = trie.startsWith("app") # return True
    trie.insert("app")
    search_app2 = trie.search("app")     # return True    

    print(f"search_apple = {search_apple}")
    print(f"search_app = {search_app}")
    print(f"startWithapp = {startWithapp}")
    print(f"search_app2 = {search_app2}")
    print(f"")
    print(f"")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
