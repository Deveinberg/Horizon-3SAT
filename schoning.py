import random
import ast

def parse_input(test):
    """
    parses the input, returns a list of the clauses and the number of unique booleans
    """
    clauses = ast.literal_eval(f"{test}")
    number_of_booleans = 0
    for clause in clauses:
        for boolean in clause:
            if abs(int(boolean)) > number_of_booleans:
                number_of_booleans = abs(int(boolean))

    return clauses, number_of_booleans

def random_assignment(booleans):
    """
    Randomly initializes boolean values
    """
    return {x: random.choice([True, False])for x in range(1, booleans+1)}

def is_satisfied(clause, initialized):
    """
    Returns True if the clause is satisfied. False otherwise.
    """
    boolean_exp = []
    for a in clause:
        if a > 0:
            boolean_exp.append(str(initialized[a]))
        else:
            boolean_exp.append(str(not initialized[abs(a)]))
    return eval(' or '.join(boolean_exp))

def random_flip(initialized):
    """
    Flips a random boolean
    """
    choice = random.choice(list(initialized.keys()))
    initialized[choice] = not initialized[choice]
    return initialized

def schoning(test_string):
    """
    Putting all the pieces together.
    """
    passed = False
    counter = 0
    problem, booleans = parse_input(test_string)
    cmax = 3 * booleans
    initialized = random_assignment(booleans)
    #print(f"\nTest string: {test_string}\n")
    #print(f"Random assignment: {initialized}")
    while not passed:
        counter += 1
        if counter > cmax:
            #print("Algorithm exceed theoretical upper bound. Please try again.\n")
            return None,None
        evaluated = [is_satisfied(clause, initialized) for clause in problem]
        if False in evaluated:
            initialized = random_flip(initialized)
        else:
            passed = True
    
    return counter, initialized