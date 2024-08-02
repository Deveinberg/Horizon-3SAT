from schoning import schoning
from threeSATgen import generate, is_valid

for num in [x for x in range(19, 51, 1)]:
    assignments = []
    total_count = 0
    valid_problems = []
    solutions = []
    solution_counts = []
    while len(valid_problems) < 100:
        problem = generate(num)
        # DEBUG: print(len(valid_problems))
    
        if is_valid(problem):
            assignments = []
            iterations = 50
            for i in range(iterations):
                count, assignment = schoning(problem)
                total_count += count if count != None else 0
                if assignment not in assignments and assignment != None:
                    assignments.append(assignment)
            if len(assignments) == 1:
                #DEBUG: print("Uniquely SATISFIABLE.")
                solutions.append([count, assignments])
                solution_counts.append(total_count/iterations)
                valid_problems.append(problem)
            """if len(assignments) > 1:
                # DEBUG: print("Non-uniquely SATISFIABLE.")
            if len(assignments) == 0:
                continue
                # DEBUG: print("UNSATISFIABLE.")"""
        if len(valid_problems) % 10 == 0:
             print(len(valid_problems))
    print(f"{'-'*40}")
    print(f"{len(valid_problems)} uniquely satisfiable problems generated for {num} booleans.")
    print(f"{'-'*40}")

    for problem in valid_problems: 
            with open(f'Final Files/Problems/3SAT_{num}_booleans.txt', "a+") as file:
                file.write(f"{str(problem).strip('[').strip(']')}\n")

    for solution in solutions:
        with open(f'Final Files/Solutions/3SAT_SOLUTIONS_{num}_booleans.txt', 'a+') as file:
                file.write(f"{str(solution).strip('[').strip(']')}\n")
    for count in solution_counts:
        with open(f'Final Files/Solutions/3SAT_COUNTS_{num}_booleans.txt', 'a+') as file:
              file.write(str(count))

        
