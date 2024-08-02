from threeSATgen import generate, is_valid
from schoning import schoning

"""
generated = False

while generated == False:
    problem = generate(3)
    if is_valid(problem):
        solutions = []
        for i in range(50):
            (counts, solution) = schoning(problem)
            if solution != None and solution not in solutions:
                solutions.append(solution)
        print(len(solutions))
        if len(solutions) == 1:
            print(problem)
            generated = True
"""
                
problem = [(-3, 2, -1), (-3, -2, 1), (3, -1, 2), (-2, 1, -3), (-1, -3, 2), (1, -3, -2), (-2, 1, 3), (-1, -3, -2), (-2, -1, 3), (-3, 1, -2), (-1, 2, -3), (3, 1, 2), (-1, 3, 2)]