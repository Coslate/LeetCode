#! /usr/bin/env python3

from solution import *

def main():
    print(f"//Case1:")
    print(f"//------Original-------//")
    wordDictionary = WordDictionary();
    print(f"//------Checked-------//")
    wordDictionary.addWord("bad")
    wordDictionary.addWord("dad")
    wordDictionary.addWord("mad")
    search_pad = wordDictionary.search("pad")# return False
    search_bad = wordDictionary.search("bad")# return True
    search_ad = wordDictionary.search(".ad")# return True
    search_b = wordDictionary.search("b..")# return True

    print(f"search_pad = {search_pad}")
    print(f"search_bad = {search_bad}")
    print(f"search_ad = {search_ad}")
    print(f"search_b = {search_b}")
    print(f"")
    print(f"")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
