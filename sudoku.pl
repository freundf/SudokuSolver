:- use_module(library(clpfd)).

sudoku(Rows) :-
    append(Rows, Value), Value ins 1..9,
    maplist(all_distinct, Rows),
    transpose(Rows, Columns),
    maplist(all_distinct, Columns),
    Rows = [A,B,C,D,E,F,G,H,I],
    block(A,B,C), block(D,E,F), block(G,H,I),
    maplist(label, Rows).

block([],[],[]).
block([A,B,C|R1],[D,E,F|R2],[G,H,I|R3]) :-
    all_distinct([A,B,C,D,E,F,G,H,I]),
    block(R1,R2,R3).

problem(Problem, Rows) :- Problem = Rows.


solve(Problem, Rows) :- problem(Problem, Rows), sudoku(Rows), maplist(writeln, Rows).
