TEST = [1,9,10,3,2,3,11,0,99,30,40,50]

def run(program, step=0, noun=12, verb=2):
    p = program[:]
    p[1] = noun
    p[2] = verb
    while True:
        op, x, y, out = p[step],p[step+1],p[step+2],p[step+3]
        step += 4
        if op == 99 or out > len(p):
            return p
        elif op == 1:
            p[out] = p[x] + p[y]
        elif op == 2:
            p[out] = p[x] * p[y]
        else:
            raise RuntimeError("Unknown OPCODE")

#assert run(TEST)[0] == 3500

with open('./inputs/day02.txt', 'r') as f:
    inp = list(map(int, f.read().strip().split(',')))


print(run(inp)[0])

#for verb in range()
