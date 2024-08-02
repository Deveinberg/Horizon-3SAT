"""
Requirements:
1. All clauses are different from each other.

2. Every variable b occurs at least once in the 3-SAT proposition in positive form b i , and at least once in negated form ¬b i .

3. All clauses involve three different variables, thus neither
(b1 ∨ b1 ∨ b2 ) nor (b 1 ∨ ¬b1 ∨ b2 ) could be present.

4. Given n variables we generate m = round(R n) clauses, with R = 4.267.
"""

import random 

# Generate 3-SAT Problem
def generate(number_of_booleans, R=4.267):
    # Initialize
    num_clauses = round(number_of_booleans * R)
    problem = []
    booleans = [x for x in range(1, number_of_booleans+1)]

    # Function to return a random boolean
    def choose(booleans):
        boolean = random.choice(booleans)
        negate = random.choice(["+","-"])
        return int(negate+str(boolean))

    for i in range(num_clauses):
        booleans_copy = booleans.copy()
        bool1 = choose(booleans_copy)
        booleans_copy.remove(abs(bool1))
        bool2 = choose(booleans_copy)
        booleans_copy.remove(abs(bool2))
        bool3 = choose(booleans_copy)
        problem.append((bool1, bool2, bool3))
        booleans_copy = booleans.copy()
    return problem

# Tests for vailidity
def is_valid(problem):
    clauses_seen = []
    # Check for repeated clauses
    for i in range(len(problem)):
        if i == 0:
            clauses_seen.append(problem[i])
        else:
            if problem[i] in clauses_seen:
                return False
        clauses_seen.append(problem[i])
        
    # Check for repeated booleans
    for clause in problem:
        booleans_seen = []
        for boolean in clause:
            if abs(boolean) in booleans_seen:
                return False
            booleans_seen.append(abs(boolean))
            
    return True

"""def main():
    #number_of_problems = int(input("Enter the number of problems to generate: "))
    number_of_problems = 1000
    #number_of_booleans = int(input("Enter the number of booleans: "))
    number_of_booleans = 30
    while number_of_booleans < 100:
        number_of_booleans += 2
        print(f"Your {number_of_problems} 3-SAT problems will be {round(number_of_booleans*4.267)} clauses long, with {number_of_booleans} booleans.")
        print(f"{'-'*20}")
        
        problems = []
        i = 0
        while len(problems) < number_of_problems:
            i+=1
            problem = generate(number_of_booleans)
            if is_valid(problem):
                problems.append(problem)
            
        for problem in problems: 
            with open(f"Final Files/3SAT_{number_of_booleans}_booleans.txt", "a+") as file:
                file.write(f"{str(problem).strip('[').strip(']')}\n")

if __name__ == "__main__":
    main()"""