#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()
    s = "QWER"
    print(f"//Case1:")
    print(f"//------Original-------//")
    print(f"s = {s}")
    print(f"//------Checked-------//")
    output = sol.balancedString(s)
    print(f"output = {output}")
    print(f"")
    print(f"")

    s = "QQWE"
    print(f"//Case2:")
    print(f"//------Original-------//")
    print(f"s = {s}")
    print(f"//------Checked-------//")
    output = sol.balancedString(s)
    print(f"output = {output}")
    print(f"")
    print(f"")

    s = "QQQW"
    print(f"//Case3:")
    print(f"//------Original-------//")
    print(f"s = {s}")
    print(f"//------Checked-------//")
    output = sol.balancedString(s)
    print(f"output = {output}")
    print(f"")
    print(f"")

    s = "QQQQ"
    print(f"//Case4:")
    print(f"//------Original-------//")
    print(f"s = {s}")
    print(f"//------Checked-------//")
    output = sol.balancedString(s)
    print(f"output = {output}")
    print(f"")
    print(f"")

    s = "WQWRQQQW"
    print(f"//Case5:")
    print(f"//------Original-------//")
    print(f"s = {s}")
    print(f"//------Checked-------//")
    output = sol.balancedString(s)
    print(f"output = {output}")
    print(f"")
    print(f"")

    s = "WWEQERQWQWWRWWERQWEQ"
    print(f"//Case6:")
    print(f"//------Original-------//")
    print(f"s = {s}")
    print(f"//------Checked-------//")
    output = sol.balancedString(s)
    print(f"output = {output}")
    print(f"")
    print(f"")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
