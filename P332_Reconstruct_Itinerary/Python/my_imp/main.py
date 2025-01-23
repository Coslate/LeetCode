#! /usr/bin/env python3

from solution import *

def main():
    print(f"//Case1:")
    tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    print(f"ans = {Solution().findItinerary(tickets)}")

    print(f"//Case2:")
    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    print(f"ans = {Solution().findItinerary(tickets)}")


#---------------Execution---------------#
if __name__ == '__main__':
    main()
