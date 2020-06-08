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
                print(f'[{step}] DEBUG: inst: {op,a,b,c} - mode:{modes}')
                p[c] = a + b
                step += 4
            elif op == 2: # Multiply
                a = (p[step+1] if modes[0] else p[p[step+1]])
                b = (p[step+2] if modes[1] else p[p[step+2]])
                c = (step + 3 if modes[2] else p[step + 3])
                print(f'[{step}] DEBUG: inst: {op,a,b,c} - mode:{modes}')
                p[c] = a * b
                step += 4
            elif op == 3: # Store input_in
                a = p[step+1]
                print(f'[{step}] DEBUG: inst: {op,a} - mode:{modes}')
                p[a] = self.user_input
                step += 2
            elif op == 4: # Output
                a = (p[step+1] if modes[0] else p[p[step+1]])
                output.append(a)
                print(f'[{step}] DEBUG: inst: {op,a} - mode:{modes}')
                step += 2
            else: raise RuntimeError(f'Unknown OPCODE: {op} from {p[step]} @{step}')
        return output

