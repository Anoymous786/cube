

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from cube import Cube
import time

# Standard face indices in Cube.state
FACE_NAMES = ['U', 'R', 'F', 'D', 'L', 'B']
FACE_COLOR_MAP = {
    'U': 'white',
    'D': 'yellow',
    'F': 'green',
    'B': 'blue',
    'L': 'orange',
    'R': 'red',
}

# Face index ranges in the 1D Cube.state
FACE_INDICES = {
    'U': list(range(0, 9)),
    'R': list(range(9, 18)),
    'F': list(range(18, 27)),
    'D': list(range(27, 36)),
    'L': list(range(36, 45)),
    'B': list(range(45, 54)),
}

def get_face_colors(cube: Cube):
    """
    Return a dict of face -> list of 9 colors for that face.
    """
    return {
        face: [FACE_COLOR_MAP[cube.state[i]] for i in FACE_INDICES[face]]
        for face in FACE_NAMES
    }

def draw_cube(ax, face_colors):
    """
    Draw the cube using matplotlib 3D at current state.
    """
    ax.cla()  # clear axis
    ax.set_axis_off()
    ax.view_init(30, 30)
    ax.set_xlim([-2, 4])
    ax.set_ylim([-2, 4])
    ax.set_zlim([-2, 4])

    # Define face layout in 3D space
    face_layout = {
        'U': (0, 1, 0),
        'D': (0, -1, 0),
        'F': (0, 0, 1),
        'B': (0, 0, -1),
        'L': (-1, 0, 0),
        'R': (1, 0, 0)
    }

    # Offset in 3x3 grid
    def cell_offset(i):
        return (i % 3 - 1, 1 - i // 3)

    for face, normal in face_layout.items():
        base_x, base_y, base_z = normal
        for i in range(9):
            dx, dy = cell_offset(i)
            x, y, z = base_x + dx * 0.95, base_y + dy * 0.95, base_z
            draw_square(ax, (x, y, z), normal, face_colors[face][i])

def draw_square(ax, center, normal, color):
    """
    Draw a single colored square centered at position with normal vector.
    """
    x, y, z = center
    dx, dy, dz = normal

    size = 0.9
    # Define local 2D axes
    if normal == (1, 0, 0) or normal == (-1, 0, 0):
        u, v = (0, size, 0), (0, 0, size)
    elif normal == (0, 1, 0) or normal == (0, -1, 0):
        u, v = (size, 0, 0), (0, 0, size)
    else:
        u, v = (size, 0, 0), (0, size, 0)

    vertices = [
        (x - u[0]/2 - v[0]/2, y - u[1]/2 - v[1]/2, z - u[2]/2 - v[2]/2),
        (x + u[0]/2 - v[0]/2, y + u[1]/2 - v[1]/2, z + u[2]/2 - v[2]/2),
        (x + u[0]/2 + v[0]/2, y + u[1]/2 + v[1]/2, z + u[2]/2 + v[2]/2),
        (x - u[0]/2 + v[0]/2, y - u[1]/2 + v[1]/2, z - u[2]/2 + v[2]/2),
    ]

    square = Poly3DCollection([vertices])
    square.set_facecolor(color)
    square.set_edgecolor('black')
    ax.add_collection3d(square)

def animate_solution(cube: Cube, moves: list, delay=0.5):
    """
    Visualize the cube step-by-step for each move.
    """
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')

    face_colors = get_face_colors(cube)
    draw_cube(ax, face_colors)
    plt.pause(delay)

    for move in moves:
        cube.apply_move(move)
        face_colors = get_face_colors(cube)
        draw_cube(ax, face_colors)
        plt.pause(delay)

    plt.show()
