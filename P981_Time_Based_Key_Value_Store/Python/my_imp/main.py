#! /usr/bin/env python3

from solution import *

def main():
    print(f"//Case1:")
    obj = TimeMap()
    obj.set('foo', 'bar', 1)
    print(f"get('foo', 1) = {obj.get('foo', 1)}")
    print(f"get('foo', 3) = {obj.get('foo', 3)}")
    obj.set('foo', 'bar2', 4)
    print(f"get('foo', 4) = {obj.get('foo', 4)}")
    print(f"get('foo', 5) = {obj.get('foo', 5)}")
    print(f"get('foo', 0) = {obj.get('foo', 0)}")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
