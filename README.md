# 🧩 Rubik's Cube Solver – Python GUI + Kociemba Algorithm

**Hackathon’25 Submission – Design Dexterity Challenge**  
📍 *CMR Institute of Technology, Bengaluru | Dept. of ISE*  
👨‍💻 *By Utkarsh Singh (1CR22IS175)*  
📅 *Academic Year: 2024–2025*

---

## 🧠 Project Overview

This project presents a fully functional **Rubik's Cube Solver** built in Python.  
It provides a GUI-based 3×3 cube simulator that can **Scramble**, **Solve**, and **Reset** the cube, integrating the **Kociemba algorithm** for optimal solving and visualizing every move with 2D animations.

> “It’s not just a puzzle – it’s a test of mind, math, and moves!”

---

## 🧩 Key Features

- ✅ Scramble, Solve, and Reset options with GUI buttons  
- ✅ Step-by-step **animated solving** of the 3×3 Rubik’s Cube  
- ✅ Uses **Kociemba algorithm** for fast, optimal solutions (≤20 moves)  
- ✅ Accurate internal cube state & valid move logic  
- ✅ 2D animated cube display using **Matplotlib**  
- ✅ Real-time scramble and solution logging in terminal  
- ✅ Clean, modular Python codebase  

---

## 💡 Technology Stack

- 🐍 Python 3.9+
- 🎯 [Cube](https://github.com/Anoymous786/cube.git)
- 🎨 Matplotlib (2D cube visualization)
- 🖼 Tkinter (GUI + buttons)

---

## 🧠 Data Structures & Logic

- **Cube Representation**:  
  A Python `dict` with keys: `U, D, F, B, L, R`  
  Each face is a 3×3 2D list (colors: `W, Y, R, O, G, B`)
  
- **Move Logic**:  
  - Face rotation using matrix transpose & reversal  
  - Edge strip updates per standard Rubik's Cube notation  

- **Solver**:  
  Uses the Kociemba algorithm to compute a minimal solution, then animates each move with delay.

  ---

SAMPLE OUTPUT:

<img width="14" height="87" alt="state 1" src="https://github.com/user-attachments/assets/dd6761fe-0d5d-444b-aa0a-fa21952d506b" />
<img width="1224" height="820" alt="Scrambled-State" src="https://github.com/user-attachments/assets/7d1f7f61-4076-47e9-8b87-e621292ee29e" />
<img width="1257" height="877" alt="Solved-State" src="https://github.com/user-attachments/assets/a90f180f-63e1-4149-b7fe-badeead648cd" />
<img width="557" height="466" alt="Terminal" src="https://github.com/user-attachments/assets/43e80a38-f55e-44c5-b7b4-5698caf0748e" />



---

## 🛠️ Project Architecture

```text
main GUI (Tkinter)
│
├── cube.py            # Cube logic & internal state
├── solver.py          # Kociemba solving integration
├── my_solver.py       # Optional beginner method
├── visual.py          # 2D/3D Matplotlib animations
├── rubiks_3d_gui.py   # Optional 3D cube viewer
└── app.py             # Entry point script (run this)

▶️ How to Run
1. Install dependencies

pip install matplotlib kociemba numpy pillow ttkthemes

Library Roles:

matplotlib – Animates 2D cube facelets

kociemba – Solves the cube optimally

numpy – Array operations and visualization

pillow – Image handling (optional)

ttkthemes – Stylish Tkinter UI themes

2. Launch the App

python app.py

Then use the GUI to:

🔀 Scramble — Generates a random 20-move cube





🧠 Solve — Calls Kociemba and animates each step

🔄 Reset — Resets the cube to solved state##

