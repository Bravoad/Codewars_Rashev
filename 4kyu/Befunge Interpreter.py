import random

def interpret(code: str) -> str:
    stack = []
    output = []
    string_mode = False
    grid = [list(line) for line in code.split("\n")]
    height = len(grid)
    width = max(len(row) for row in grid)
    for row in grid:
        row.extend(" " * (width - len(row)))
    x, y = 0, 0
    dx, dy = 1, 0

    def push(v): stack.append(v)
    def pop(): return stack.pop() if stack else 0

    while True:
        instr = grid[y][x]

        if string_mode:
            if instr == '"':
                string_mode = False
            else:
                push(ord(instr))
        else:
            if instr.isdigit():
                push(int(instr))
            elif instr == '+':
                a, b = pop(), pop(); push(b + a)
            elif instr == '-':
                a, b = pop(), pop(); push(b - a)
            elif instr == '*':
                a, b = pop(), pop(); push(b * a)
            elif instr == '/':
                a, b = pop(), pop(); push(0 if a == 0 else b // a)
            elif instr == '%':
                a, b = pop(), pop(); push(0 if a == 0 else b % a)
            elif instr == '!':
                a = pop(); push(0 if a else 1)
            elif instr == '`':
                a, b = pop(), pop(); push(1 if b > a else 0)
            elif instr == '>':
                dx, dy = 1, 0
            elif instr == '<':
                dx, dy = -1, 0
            elif instr == '^':
                dx, dy = 0, -1
            elif instr == 'v':
                dx, dy = 0, 1
            elif instr == '?':
                dx, dy = random.choice([(1,0), (-1,0), (0,1), (0,-1)])
            elif instr == '_':
                a = pop(); dx, dy = (1,0) if a == 0 else (-1,0)
            elif instr == '|':
                a = pop(); dx, dy = (0,1) if a == 0 else (0,-1)
            elif instr == '"':
                string_mode = True
            elif instr == ':':
                a = pop(); push(a); push(a)
            elif instr == '\\':
                a, b = pop(), pop(); push(a); push(b)
            elif instr == '$':
                pop()
            elif instr == '.':
                a = pop(); output.append(str(a))
            elif instr == ',':
                a = pop(); output.append(chr(a % 256))
            elif instr == '#':
                x = (x + dx) % width
                y = (y + dy) % height
            elif instr == 'p':
                y_, x_, v = pop(), pop(), pop()
                if 0 <= y_ < height and 0 <= x_ < width:
                    grid[y_][x_] = chr(v % 256)
            elif instr == 'g':
                y_, x_ = pop(), pop()
                if 0 <= y_ < height and 0 <= x_ < width:
                    push(ord(grid[y_][x_]))
                else:
                    push(0)
            elif instr == '@':
                break
            elif instr == ' ':
                pass
        x = (x + dx) % width
        y = (y + dy) % height

    return "".join(output)
