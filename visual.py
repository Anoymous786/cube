import tkinter as tk
from tkinter import messagebox, ttk
from ttkthemes import ThemedStyle
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import matplotlib.pyplot as plt
import time
import kociemba
from cube import Cube

# === Cube Setup ===
cube = Cube()

# === Root and Themed Style ===
root = tk.Tk()
root.title("Rubik's Cube Visual Solver")

# Apply a modern dark theme
style = ThemedStyle(root)
style.set_theme("equilux")

# Configure ttk styles
style.configure("TFrame", background=style.lookup("TFrame", "background"))
style.configure("TLabel", background=style.lookup("TFrame", "background"), foreground="white", font=("Segoe UI", 12))
style.configure("TButton", font=("Segoe UI", 11, "bold"), padding=8)

# === Layout Frames ===
header = ttk.Frame(root)
header.pack(fill="x", pady=(10, 0))
ttk.Label(header, text="🧠 Rubik’s Cube Solver by Utkarsh Singh", font=("Segoe UI Semibold", 16)).pack()

cube_frame = ttk.Frame(root, borderwidth=2, relief="sunken")
cube_frame.pack(padx=20, pady=15)

controls = ttk.Frame(root)
controls.pack(pady=(0, 20))

# === Matplotlib Canvas ===
fig, ax = plt.subplots(figsize=(5, 4), facecolor=style.lookup("TFrame", "background"))
canvas = FigureCanvasTkAgg(fig, master=cube_frame)
canvas.get_tk_widget().pack()

# === Move Display Label ===
move_display = ttk.Label(root, text="", font=("Consolas", 12), wraplength=500, justify="center")
move_display.pack(pady=(5, 15))

# === Color Map and Positions ===
_color_map = {
    'U': 'white', 'R': 'red', 'F': 'green',
    'D': 'yellow', 'L': 'orange', 'B': 'blue'
}
_face_positions = {
    'U': (3, 6), 'L': (0, 3), 'F': (3, 3),
    'R': (6, 3), 'B': (9, 3), 'D': (3, 0)
}


def draw_cube_state(ax, facelet_str):
    ax.clear()
    for face, (x_off, y_off) in _face_positions.items():
        idx = ['U', 'R', 'F', 'D', 'L', 'B'].index(face) * 9
        face_str = facelet_str[idx:idx + 9]
        for i in range(3):
            for j in range(3):
                color = _color_map[face_str[i * 3 + j]]
                square = plt.Rectangle(
                    (x_off + j, y_off + 2 - i), 1, 1,
                    facecolor=color, edgecolor='black'
                )
                ax.add_patch(square)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 9)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.figure.canvas.draw()


def animate_solution(ax, cube, moves, canvas, root, delay=0.3):
    for move in moves:
        cube.move(move)
        draw_cube_state(ax, cube.get_facelet_str())
        canvas.draw()
        root.update()
        time.sleep(delay)


# Initial draw
draw_cube_state(ax, cube.get_facelet_str())

def show_cube(cube_obj):
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    draw_cube_state(ax, cube_obj)
    plt.show()

def scramble_cube():
    cube.reset()
    draw_cube_state(ax, cube.get_facelet_str())
    moves = cube.scramble()
    move_display.config(text="Scramble Moves: " + ' '.join(moves))
    animate_solution(ax, cube, moves, canvas, root, delay=0.2)

    print("\n" + "═" * 50)
    print("🌀 SCRAMBLE PHASE".center(50))
    print("═" * 50)
    print(f"🔀 Scramble Moves ({len(moves)} steps):")
    print("👉", ' '.join(moves))
    print("═" * 50)


def show_result_popup(title, message):
    try:
        messagebox.showinfo(title, message)
    except:
        print(f"[Popup Fallback] {title}: {message}")


def solve_cube():
    if not cube.is_solved():
        print("\n" + "═" * 50)
        print("🧠 SOLVING CUBE...".center(50))
        print("═" * 50)
        try:
            solution = kociemba.solve(cube.get_facelet_str())
            moves = solution.split()

            print(f"✅ Kociemba Solution ({len(moves)} steps):")
            print("👉", ' '.join(moves))
            move_display.config(text="Solve Moves: " + ' '.join(moves))

            animate_solution(ax, cube, moves, canvas, root, delay=0.3)

            total_delay_ms = int(len(moves) * 300)
            # ✔️ Use widget from canvas instead of root to prevent "invalid command name"
            '''canvas.get_tk_widget().after(
                total_delay_ms,
                lambda: show_result_popup("Cube Solved!", "🎉 The cube has been solved successfully.")
            )'''

        except Exception as e:
            messagebox.showerror("Error", f"❌ Could not solve cube:\n{e}")
    else:
        print("\n🎉 Cube was already solved.")
        messagebox.showinfo("Already Solved", "Cube is already solved!")




def reset_cube():
    cube.reset()
    draw_cube_state(ax, cube.get_facelet_str())
    move_display.config(text="")


# === Control Buttons ===
ttk.Button(controls, text="Scramble", command=scramble_cube).grid(row=0, column=0, padx=5)
ttk.Button(controls, text="Solve",    command=solve_cube).grid( row=0, column=1, padx=5)
ttk.Button(controls, text="Reset",    command=reset_cube).grid( row=0, column=2, padx=5)
# Existing GUI setup above...
canvas.get_tk_widget().pack()

# ✅ This prevents root.mainloop() from running when visual.py is imported
if __name__ == "__main__":
    root.mainloop()

root.mainloop()