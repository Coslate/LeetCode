#! /usr/bin/env python3

from solution import *

def main():
    sol = Codec()

    print(f"//Case1:")
    dummy_input = ["Hello","World"]
    print(f"//------Original-------//")
    print(f"dummy_input = {dummy_input}")
    print(f"//------Checked-------//")
    encoded_str = sol.encode(dummy_input)
    print(f"encoded_str = {encoded_str}")
    decode_ans = sol.decode(encoded_str)
    print(f"decode_ans = {decode_ans}")
    print(f"")
    print(f"")

    print(f"//Case2:")
    dummy_input = [""]
    print(f"//------Original-------//")
    print(f"dummy_input = {dummy_input}")
    print(f"//------Checked-------//")
    encoded_str = sol.encode(dummy_input)
    print(f"encoded_str = {encoded_str}")
    decode_ans = sol.decode(encoded_str)
    print(f"decode_ans = {decode_ans}")
    print(f"")
    print(f"")

    print(f"//Case3:")
    dummy_input = ["C#","&","~Xp|F","R4QBf9g=_"]
    print(f"//------Original-------//")
    print(f"dummy_input = {dummy_input}")
    print(f"//------Checked-------//")
    encoded_str = sol.encode(dummy_input)
    print(f"encoded_str = {encoded_str}")
    decode_ans = sol.decode(encoded_str)
    print(f"decode_ans = {decode_ans}")
    print(f"")
    print(f"")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
