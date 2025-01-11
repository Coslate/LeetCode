#! /usr/bin/env python3

from solution import *

def main():
    '''
    # Example usage:
    min_heap = MinHeap()
    min_heap.insert(Node('three',3))
    min_heap.insert(Node('one', 1))
    min_heap.insert(Node('six', 6))
    min_heap.insert(Node('five', 5))
    min_heap.insert(Node('two', 2))
    min_heap.insert(Node('four', 4))

    print("Min:", min_heap.get_min().val)  # Output: 1
    print("Extract Min:", min_heap.extract_min().val)  # Output: 1
    print("Min after extraction:", min_heap.get_min().name)  # Output: 2
    print("Extract Min:", min_heap.extract_min().val)  # Output: 2
    print("Min after extraction:", min_heap.get_min().name)  # Output: 3
    print("Extract Min:", min_heap.extract_min().val)  # Output: 3
    print("Min after extraction:", min_heap.get_min().name)  # Output: 4
    print("Extract Min:", min_heap.extract_min().val)  # Output: 4
    print("Min after extraction:", min_heap.get_min().name)  # Output: 5
    print("Extract Min:", min_heap.extract_min().val)  # Output: 5
    print("Min after extraction:", min_heap.get_min().name)  # Output: 6
    print("Extract Min:", min_heap.extract_min().val)  # Output: 6
    print("Min after extraction:", min_heap.get_min().name)  # Output: Error
    '''

    print(f"//Case1:")
    nums = [1,1,1,2,2,3]
    k = 2
    ans = Solution().topKFrequent(nums, k)
    print(f"ans = {ans}")
    print(f"//Case2:")
    nums = [1]
    k = 1
    ans = Solution().topKFrequent(nums, k)
    print(f"ans = {ans}")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
