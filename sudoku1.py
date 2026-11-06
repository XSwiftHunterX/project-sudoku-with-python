import clingo
from clingo.application import clingo_main

class SudokuSolver(clingo.application.Application):

    def main(self, control, files):
        # Load the Sudoku rules
        control.load("sudoku.lp")

        # Load the input puzzle
        for file in files:
            control.load(file)

        # Ground the program
        control.ground([("base", [])])

        # Solve the Sudoku
        control.solve()

    def print_model(self, model, printer):
        atoms = model.symbols(shown=True)

        sorted_atoms = sorted(atoms)

        print(" ".join(str(atom) for atom in sorted_atoms))

if __name__ == "__main__":
    clingo_main(SudokuSolver())