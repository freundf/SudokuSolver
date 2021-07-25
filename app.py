from pyswip import Prolog
problem1 = "[[_,_,_,_,6,_,_,_,_],[_,_,_,9,5,2,_,_,_],[_,8,_,_,_,_,_,7,_],[_,_,_,_,8,4,_,_,_],[_,2,4,_,_,_,_,_,1],[1,_,9,_,_,_,5,_,_],[_,_,_,3,_,_,_,_,_],[6,_,5,_,_,7,_,8,_],[_,_,_,_,_,_,3,9,_]]"


class App:
    def __init__(self, problem=None):
        if problem is None:
            self.problem = [[None for _ in range(9)] for _ in range(9)]
        else:
            self.problem = problem

        self.prolog = Prolog()
        self.prolog.consult("sudoku.pl")
        self.solution = None

    def read_problem(self):
        for i in range(9):
            for j in range(9):
                number = input("Zahl an {i} {j}".format(i=i, j=j))
                if number.isnumeric() and 1 <= int(number) <= 9:
                    self.problem[i][j] = int(number)
                else:
                    self.problem[i][j] = None

    def solve(self):
        problem = str(self.problem).replace("None", "_")
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
            for row in self.solution:
                print(row)


if __name__ == "__main__":
    a = App()
    a.read_problem()
    a.solve()
    a.print_solution()
