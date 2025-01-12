#! /usr/bin/env python3

from solution import *

def main():
    print(f"//Case1:")
    amount = 5
    coins = [1,2,5]
    ans = Solution().change(amount, coins)
    ans_opt = Solution().change_opt(amount, coins)
    print(f"ans = {ans}")
    print(f"ans_opt = {ans_opt}")

    print(f"//Case2:")
    amount = 3
    coins = [2]
    ans = Solution().change(amount, coins)
    ans_opt = Solution().change_opt(amount, coins)
    print(f"ans = {ans}")
    print(f"ans_opt = {ans_opt}")

    print(f"//Case3:")
    amount = 10
    coins = [10]
    ans = Solution().change(amount, coins)
    ans_opt = Solution().change_opt(amount, coins)
    print(f"ans = {ans}")
    print(f"ans_opt = {ans_opt}")



#---------------Execution---------------#
if __name__ == '__main__':
    main()
