import random

class Cube:
    def __init__(self):
        self.reset()

    def reset(self):
        """
        Reset cube to solved state using face letters: U, R, F, D, L, B.
        This format is required by the kociemba solver.
        """
        self.faces = {
            'U': ['U'] * 9,
            'R': ['R'] * 9,
            'F': ['F'] * 9,
            'D': ['D'] * 9,
            'L': ['L'] * 9,
            'B': ['B'] * 9,
        }

    def get_facelet_str(self):
        """
        Return 54-character string in URFDLB order for solver.
        """
        order = ['U','R','F','D','L','B']
        return ''.join(''.join(self.faces[f]) for f in order)

    def is_solved(self):
        """
        Check if each face is uniform.
        """
        return all(len(set(self.faces[f])) == 1 for f in self.faces)

    def move(self, move):
        """
        Apply a move notation (e.g., 'R', "U'", 'F2').
        """
        face = move[0]
        suffix = move[1:] if len(move) > 1 else ''
        times = 1
        if suffix == '2':
            times = 2
        elif suffix == "'":
            times = 3
        for _ in range(times):
            self._rotate(face)

    def _rotate(self, face):
        # Rotate the face itself
        f = self.faces[face]
        self.faces[face] = [f[6], f[3], f[0], f[7], f[4], f[1], f[8], f[5], f[2]]

        # Define adjacent face strips to cycle
        adjacent = {
            'U': [('B',[0,1,2]),('R',[0,1,2]),('F',[0,1,2]),('L',[0,1,2])],
            'D': [('F',[6,7,8]),('R',[6,7,8]),('B',[6,7,8]),('L',[6,7,8])],
            'F': [('U',[6,7,8]),('R',[0,3,6]),('D',[2,1,0]),('L',[8,5,2])],
            'B': [('U',[2,1,0]),('L',[0,3,6]),('D',[6,7,8]),('R',[8,5,2])],
            'L': [('U',[0,3,6]),('F',[0,3,6]),('D',[0,3,6]),('B',[8,5,2])],
            'R': [('U',[8,5,2]),('B',[0,3,6]),('D',[8,5,2]),('F',[8,5,2])]
        }
        seq = adjacent[face]
        temp = [ self.faces[fname][i] for fname, idxs in [seq[-1]] for i in idxs ]
        for k in range(len(seq)-1,0,-1):
            from_face, from_idxs = seq[k-1]
            to_face, to_idxs = seq[k]
            for frm_i, to_i in zip(from_idxs, to_idxs):
                self.faces[to_face][to_i] = self.faces[from_face][frm_i]
        first_face, first_idxs = seq[0]
        for val, idx in zip(temp, first_idxs):
            self.faces[first_face][idx] = val

    def scramble(self, steps=20):
        """
        Generate and apply a random scramble; return move list.
        """
        moves = [f + m for f in ['U', 'D', 'L', 'R', 'F', 'B'] for m in ['', "'", '2']]
        seq = []
        prev = ''
        for _ in range(steps):
            mv = random.choice(moves)
            while mv[0] == prev:
                mv = random.choice(moves)
            seq.append(mv)
            self.move(mv)
            prev = mv[0]
        return seq
