#my solver.py
import random
import kociemba

MOVES = ["U", "U'", "U2", "D", "D'", "D2",
         "F", "F'", "F2", "B", "B'", "B2",
         "L", "L'", "L2", "R", "R'", "R2"]

def generate_scramble(length=20):
    scramble = []
    prev = ''
    for _ in range(length):
        move = random.choice(MOVES)
        while move[0] == prev:
            move = random.choice(MOVES)
        scramble.append(move)
        prev = move[0]
    return scramble

def solve_cube(cube):
    try:
        facelets = cube.get_facelet_str()
        solution = kociemba.solve(facelets)
        return solution.split()
    except Exception as e:
        print(f"❌ Solve error: {e}")
        return []
