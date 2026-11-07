import clingo
from clingo.application import clingo_main
from sudoku_board import Sudoku

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
        board = Sudoku.from_model(model)
        print(board, end="")

if __name__ == "__main__":
    clingo_main(SudokuSolver())