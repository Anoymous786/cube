from cube import Cube
from my_solver import CubeSolver

cube = Cube()
original = cube.get_faces()  # save solved state

scramble = ["R", "U", "F'", "L", "D2", "B"]
cube.apply_moves(scramble)

solution = solve(scramble)
cube.apply_moves(solution)

final = cube.get_faces()

print("Solved Again:", original == final)
