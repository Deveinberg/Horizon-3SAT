from schoning import schoning

booleans = [6,8,10,11,12,13,14,15,16,17,18,19,20]
for boolean in booleans:
    file = f"Final Files/Problems/3SAT_{boolean}_booleans.txt"
    with open(file, 'r') as f:
        problems = f.read() 
    problems = problems.split("\n")
    problems.pop()
    solutions = []
    total_counts = []
    for problem in problems:
        iterations = 90
        successful_iterations = 0
        avg_counts = []
        current_problem_solution = []
        for _ in range(iterations):
            try:
                counts, solution = schoning(problem)
                if solution != None and solution not in current_problem_solution:
                    current_problem_solution.append(solution)
                if counts != None:
                    avg_counts.append(counts)
                    successful_iterations += 1
            except:
                pass
        try:
            if len(current_problem_solution) != 1:
                print(len(current_problem_solution), current_problem_solution)
                print(f"Problem {problem} is not uniquely satisfiable.")
            if len(current_problem_solution) == 1:
                total_counts.append(round((sum(avg_counts)/successful_iterations),2))
                for solution in current_problem_solution:
                    solutions.append(f"{problem};{solution}")
        except:
            pass
    print(solutions)
    print(f"{file} read; {len(problems)} problems solved.")
    with open(f"Final Files/Solutions/3SAT_SOLUTIONS_{boolean}_booleans.txt", "a+") as f:
        for solution in solutions:
            f.write(f"{solution}\n")
    with open(f"Final Files/Solutions/3SAT_COUNTS_{boolean}_booleans.txt", "a+") as f:
        for count in total_counts:
            f.write(f"{count}\n")
