#محمدرضا محمدی درویشانی


f = open ("puzzles.txt" , "r")
puzzle = f.read()
f.close

def solve_puzzle(puzzle):
    bool_list=[]
    new_list = puzzle.splitlines()
    for i in new_list:
        try:
            n = eval(i)
            z = bool(n)
            bool_list.append(z)

        except (SyntaxError , ValueError , Exception):
            bool_list.append(False)

    return bool_list

print(solve_puzzle(puzzle))


