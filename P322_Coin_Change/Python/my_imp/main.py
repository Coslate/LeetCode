#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()

    coins = [1, 2, 5]
    amount = 11
    print(f"//Case1:")
    print(f"//------Original-------//")
    print(f"coins = {coins}, amount = {amount}")
    print(f"//------Checked-------//")
    output = sol.coinChange(coins, amount)
    output_opt = sol_opt.coinChange(coins, amount)
    print(f"output = {output}")
    print(f"output_opt = {output_opt}")
    print(f"")
    print(f"")

    coins = [2]
    amount = 3
    print(f"//Case2:")
    print(f"//------Original-------//")
    print(f"coins = {coins}, amount = {amount}")
    print(f"//------Checked-------//")
    output = sol.coinChange(coins, amount)
    output_opt = sol_opt.coinChange(coins, amount)
    print(f"output = {output}")
    print(f"output_opt = {output_opt}")
    print(f"")
    print(f"")

    coins = [1]
    amount = 0
    print(f"//Case3:")
    print(f"//------Original-------//")
    print(f"coins = {coins}, amount = {amount}")
    print(f"//------Checked-------//")
    output = sol.coinChange(coins, amount)
    output_opt = sol_opt.coinChange(coins, amount)
    print(f"output = {output}")
    print(f"output_opt = {output_opt}")
    print(f"")
    print(f"")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
