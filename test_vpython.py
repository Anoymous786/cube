#test_vpython.py
# test_vpython.py

from vpython import box, vector, color, rate, scene
from cube import Cube
from my_solver import solve_cube
import time

# Face color mapping
COLOR_MAP = {
    'U': color.white,
    'D': color.yellow,
    'F': color.green,
    'B': color.blue,
    'L': color.orange,
    'R': color.red,
}

# Cubelet positions by (x, y, z) coordinates
cubelets = {}

# Maps cube facelets to (x, y, z, face)
FACELETS_POSITIONS = {
    'U': [(x, 1, z, 'y') for z in [-1, 0, 1] for x in [-1, 0, 1]],
    'D': [(x, -1, z, 'y') for z in [-1, 0, 1] for x in [-1, 0, 1]],
    'F': [(x, y, 1, 'z') for y in [1, 0, -1] for x in [-1, 0, 1]],
    'B': [(x, y, -1, 'z') for y in [1, 0, -1] for x in [1, 0, -1]],
    'L': [(-1, y, z, 'x') for y in [1, 0, -1] for z in [1, 0, -1]],
    'R': [(1, y, z, 'x') for y in [1, 0, -1] for z in [-1, 0, 1]],
}


def create_visual_cube(cube: Cube):
    """
    Initializes the visual 3D Rubik's Cube.
    """
    scene.center = vector(0, 0, 0)
    scene.background = color.gray(0.2)

    facelet_index = 0
    for face in ['U', 'R', 'F', 'D', 'L', 'B']:
        for idx, (x, y, z, axis) in enumerate(FACELETS_POSITIONS[face]):
            facelet = cube.state[facelet_index]
            facelet_index += 1

            b = box(pos=vector(x, y, z), size=vector(0.95, 0.95, 0.05),
                    color=COLOR_MAP.get(facelet, color.white))

            # Orient correctly
            if axis == 'x':
                b.axis = vector(1, 0, 0)
                b.up = vector(0, 1, 0)
            elif axis == 'y':
                b.axis = vector(0, 1, 0)
                b.up = vector(0, 0, -1)
            elif axis == 'z':
                b.axis = vector(0, 0, 1)
                b.up = vector(0, 1, 0)

            cubelets[(face, idx)] = b


def update_visual_cube(cube: Cube):
    """
    Updates cubelet colors to reflect the cube state.
    """
    facelet_index = 0
    for face in ['U', 'R', 'F', 'D', 'L', 'B']:
        for idx in range(9):
            facelet = cube.state[facelet_index]
            cubelets[(face, idx)].color = COLOR_MAP.get(facelet, color.white)
            facelet_index += 1


def animate_solution(cube: Cube, moves: list, delay=0.4):
    """
    Animate the solution using vpython.
    """
    update_visual_cube(cube)
    rate(1 / delay)
    for move in moves:
        cube.apply_move(move)
        update_visual_cube(cube)
        rate(1 / delay)


def main():
    scramble_moves = "L2 B U' L' U' L F2 R' B R U D' R2 D' U' R' L2 F2 B2 F'"

    # Initialize cube
    cube = Cube()
    cube.apply_moves(scramble_moves)

    # Create visual cube
    create_visual_cube(cube)

    # Solve
    start = time.time()
    solution = solve_cube(cube)
    end = time.time()

    print("🔁 Solution:", ' '.join(solution))
    print(f"⏱️ Time: {end - start:.4f}s")

    # Animate
    animate_solution(cube, solution)


if __name__ == "__main__":
    main()
