

from cube import Cube
from visual import show_cube, scramble_cube, solve_cube, reset_cube
import kociemba
import tkinter as tk

# Create a Cube instance
cube = Cube()
scramble_moves = []  # Declare globally so it’s accessible inside functions



'''def show_result_popup(title, message):
    try:
        popup = tk.Toplevel()
        popup.title(title)
        label = tk.Label(popup, text=message, padx=20, pady=10)
        label.pack()
        ok_button = tk.Button(popup, text="OK", command=popup.destroy)
        ok_button.pack(pady=5)
        popup.lift()
        popup.attributes("-topmost", True)
        popup.grab_set()  # ✅ Only this instead of mainloop
    except Exception as e:
        print(f"[Popup Fallback] {title}: {message} ({str(e)})")'''


def scramble_cube():
    global scramble_moves
    cube.reset()
    scramble_moves = cube.scramble()
    print("✅ Scrambled:", ' '.join(scramble_moves))
    show_cube(cube)


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
            #move_display.config(text="Solve Moves: " + ' '.join(moves))

            #animate_solution(ax, cube, moves, canvas, root, delay=0.3)

            total_delay_ms = int(len(moves) * 300)
            # ✔️ Use widget from canvas instead of root to prevent "invalid command name"
            '''canvas.get_tk_widget().after(
                total_delay_ms,
                lambda: show_result_popup("Cube Solved!", "🎉 The cube has been solved successfully.")
            )'''

        except Exception as e:
            messagebox.showerror("Error", f"❌ Could not solve cube:\n{e}")
    else:
        #print("\n🎉 Cube was already solved.")
        messagebox.showinfo("Already Solved", "Cube is already solved!")




def reset_cube():
    cube.reset()
    print("🔄 Cube reset to solved state.")
    show_cube(cube)


# Do an initial scramble and showscramble_cube()

# GUI
root = tk.Tk()
root.title("Rubik's Cube Solver")

solve_btn = tk.Button(root, text="Solve", command=solve_cube_gui)
solve_btn.pack(pady=5)

scramble_btn = tk.Button(root, text="Scramble", command=scramble_cube)
scramble_btn.pack(pady=5)

reset_btn = tk.Button(root, text="Reset", command=reset_cube)
reset_btn.pack(pady=5)

# Add this at the END of visual.py

def start_gui():
    root.mainloop()
