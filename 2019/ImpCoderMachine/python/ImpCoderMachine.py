from typing import List

class ImpCoderMachine:
    def __init__(self, program: List[int], cursor: int = 0, user_input: int = 1):
        self.program = program
        self.cursor = cursor
        self.user_input = user_input

    def run(self) -> List[int]:
        p: List[int] = self.program
        output: List[int] = []
        step: int = self.cursor
        while p[step] % 100 != 99:
            op: int = p[step] % 100
            modes: List[int] = [p[step] // i % 10 for i in [100,1000,10000]]
            if op == 1: # Add
                a = (p[step+1] if modes[0] else p[p[step+1]])
                b = (p[step+2] if modes[1] else p[p[step+2]])
                c = (step + 3 if modes[2] else p[step + 3])
                p[c] = a + b
                step += 4
            elif op == 2: # Multiply
                a = (p[step+1] if modes[0] else p[p[step+1]])
                b = (p[step+2] if modes[1] else p[p[step+2]])
                c = (step + 3 if modes[2] else p[step + 3])
                p[c] = a * b
                step += 4
            elif op == 3: # Store input_in
                a = p[step+1]
                p[a] = self.user_input
                step += 2
            elif op == 4: # Output
                a = (p[step+1] if modes[0] else p[p[step+1]])
                output.append(a)
                step += 2
            elif op == 5: # jump-if-true
                a = (p[step+1] if modes[0] else p[p[step+1]])
                b = (p[step+2] if modes[1] else p[p[step+2]])
                step = b if a != 0 else step + 3
            elif op == 6: # jump-if-false
                a = (p[step+1] if modes[0] else p[p[step+1]])
                b = (p[step+2] if modes[1] else p[p[step+2]])
                step = b if a == 0 else step + 3
            elif op == 7: # less than
                a = (p[step+1] if modes[0] else p[p[step+1]])
                b = (p[step+2] if modes[1] else p[p[step+2]])
                c = (step + 3 if modes[2] else p[step + 3])
                p[c] = 1 if a < b else 0
                step += 4
            elif op == 8: # equals
                a = (p[step+1] if modes[0] else p[p[step+1]])
                b = (p[step+2] if modes[1] else p[p[step+2]])
                c = (step + 3 if modes[2] else p[step + 3])
                p[c] = 1 if a == b else 0
                step += 4
            else: raise RuntimeError(f'Unknown OPCODE: {op} from {p[step]} @{step}')
        return output

if __name__ == "__main__":
    # Less than / equal to 8
    assert(ImpCoderMachine([3,9,8,9,10,9,4,9,99,-1,8], 0, 8).run(), [1])
    assert(ImpCoderMachine([3,9,8,9,10,9,4,9,99,-1,8], 0, 5).run(), [0])
    assert(ImpCoderMachine([3,9,7,9,10,9,4,9,99,-1,8], 0, 5).run(), [1])
    assert(ImpCoderMachine([3,3,1108,-1,8,3,4,3,99], 0, 8).run(), [1])
    assert(ImpCoderMachine([3,3,1107,-1,8,3,4,3,99], 0, 5).run(), [1])

    # jumps (input a nonzero?)
    assert(ImpCoderMachine([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], 0, 5).run(), [1])
    assert(ImpCoderMachine([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], 0, 0).run(), [0])
    assert(ImpCoderMachine([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
                            1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
                            999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99], 0, 5).run(), [1])

    inp = [99]
    ImpCoder = ImpCoderMachine(inp[:], 0, 8)
    print('test: ', ImpCoder.run())
