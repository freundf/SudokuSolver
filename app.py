from pyswip import Prolog
import os

problem1 = "[[_,_,_,_,6,_,_,_,_],[_,_,_,9,5,2,_,_,_],[_,8,_,_,_,_,_,7,_],[_,_,_,_,8,4,_,_,_],[_,2,4,_,_,_,_,_,1],[1,_,9,_,_,_,5,_,_],[_,_,_,3,_,_,_,_,_],[6,_,5,_,_,7,_,8,_],[_,_,_,_,_,_,3,9,_]]"


def clear_console():
    command = "cls" if os.name in ("nt", "dos") else "clear"
    os.system(command)


class Sudoku:
    def __init__(self, problem=None):
        if problem is None:
            self.problem = [["x" for _ in range(9)] for _ in range(9)]
        else:
            self.problem = problem

        self.prolog = Prolog()
        self.prolog.consult("sudoku.pl")
        self.solution = None

    def __str__(self):
        string = ""

        header = "*_______*_______*_______*\n"
        rows = ["| {r[0]} {r[1]} {r[2]} | {r[3]} {r[4]} {r[5]} | {r[6]} {r[7]} {r[8]} |\n".format(r=r) for r in self.problem]

        j = 0
        for i in range(13):
            if i % 4 == 0 or i == 0:
                string += header
                j += 1
            else:
                string += rows[i - j]

        return string

    def read_problem(self):
        clear_console()
        print(self)
        for i in range(9):
            for j in range(9):
                number = input("Number in row {i}, column {j}: ".format(i=i + 1, j=j + 1))
                if number.isnumeric() and 1 <= int(number) <= 9:
                    self.problem[i][j] = int(number)
                else:
                    self.problem[i][j] = "_"
                clear_console()
                print(self)

    def solve(self):
        problem = str(self.problem).replace("'_'", "_")
        try:
            sudoku = self.prolog.query("solve({}, Rows).".format(problem)).__next__()
            self.solution = sudoku["Rows"]
        except StopIteration:
            self.solution = None
            print("Error")

    def print_solution(self):
        if self.solution is None:
            print("Couldn't find a Solution")
        else:
            self.problem = self.solution
            clear_console()
            print("Solution: \n\n" + str(self))


if __name__ == "__main__":
    s = Sudoku()
    s.read_problem()
    s.solve()
    s.print_solution()
