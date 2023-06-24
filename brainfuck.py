import sys
import os

memory_size = 2**16
memory = [0 for _ in range(memory_size)]

def bfInterprerter(string):
    global memory
    pointer = 0
    i = 0
    while i < len(string):
        if string[i] == '>':
            pointer += 1
        elif string[i] == '<':
            pointer -= 1
        elif string[i] == '+':
            memory[pointer] += 1
        elif string[i] == '-':
            memory[pointer] -= 1
        elif string[i] == '.':
            print(chr(memory[pointer]), end='')
        elif string[i] == ',':
            memory[pointer] = ord(input())
        elif string[i] == '[':
            if memory[pointer] == 0:
                i += 1
                while string[i] != ']':
                    i += 1
        elif string[i] == ']':
            if memory[pointer] != 0:
                i -= 1
                while string[i] != '[':
                    i -= 1
        i += 1
    return memory

def main():
    if len(sys.argv) != 2:
        if sys.platform == 'win32':
            print("python bf.py <file>")
        elif sys.platform == 'darwin':
            print("python3 bf.py <file>")
        return
    if not os.path.isfile(sys.argv[1]):
        print("File not found")
        return
    with open(sys.argv[1], 'r') as souceCode:
        mem = bfInterprerter(souceCode.read())
    return mem

if __name__ == '__main__':
    main()

