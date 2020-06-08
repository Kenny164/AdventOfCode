from typing import List
import os
import sys
scriptpath = "./ImpCoderMachine/python"
sys.path.append(os.path.abspath(scriptpath))
import ImpCoderMachine as icm

if __name__ == "__main__":
    with open('./inputs/day05.txt', 'r') as f:
        inp = list(map(int, f.read().strip().split(',')))
    
    ImpCoder = icm.ImpCoderMachine(inp[:], 0, 1)
    print('Part1', ImpCoder.run())
