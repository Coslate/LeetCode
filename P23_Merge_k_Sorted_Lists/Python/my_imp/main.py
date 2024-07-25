#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()

    print(f"//Case1:")
    lists = [[1,4,5],[1,3,4],[2,6]]
    for i in range(len(lists)):
        for j in range(len(lists[i])):
            lists[i][j] = ListNode(lists[i][j])

    for i in range(len(lists)):
        for j in range(len(lists[i])):
            if j+1 < len(lists[i]):
                lists[i][j].next = lists[i][j+1]

    print(f"//------Original-------//")
    print(f"lists = {[y.val for x in lists for y in x]}")
    print(f"//------Checked-------//")
    #output = sol.mergeKLists(lists)
    output = sol_opt.mergeKLists(lists)
    output_list = []
    while output:
        output_list.append(output)
        output = output.next
    print(f"output = {[x.val for x in output_list]}")
    print(f"")
    print(f"")


#---------------Execution---------------#
if __name__ == '__main__':
    main()
