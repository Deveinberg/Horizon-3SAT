from schoning import schoning
from time import process_time

booleans = [6,8,10,11,12,13,14,15,16,17,18,19,20]
n_bool_cpu_times = []
for b in booleans:
    file = f"Final Files/Problems/3SAT_{b}_booleans.txt"
    with open(file, 'r') as f:
        problems = f.read()
    problems = problems.split("\n")
    problems.pop()
    current_bool_cpu_times = []
    for problem in problems:
        problem_cpu_time = []
        for i in range(50):
            try:
                cpu_start_time = process_time()
                counts, solution = schoning(problem)
                cpu_end_time = process_time()
                if solution != None:
                    #print(cpu_end_time - cpu_start_time)
                    problem_cpu_time.append(cpu_end_time - cpu_start_time)
            except:
                pass
        try:
            current_bool_cpu_times.append((sum(problem_cpu_time)/len(problem_cpu_time)))
        except:
            pass
    print(len(current_bool_cpu_times))
    n_bool_cpu_times.append(sum(current_bool_cpu_times)/len(current_bool_cpu_times))
with open("Final Files/Solutions/CPU_times.txt", "a+") as f:
    for boolean, cpu_time in zip(booleans, n_bool_cpu_times):
        f.write(f"{boolean} booleans;{cpu_time}\n")



