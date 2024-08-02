problem = [[-3, 2, -1], [-3, -2, 1], [3, -1, 2], [-2, 1, -3], [-1, -3, 2], [1, -3, -2], [-2, 1, 3], [-1, -3, -2], [-2, -1, 3], [-3, 1, -2], [-1, 2, -3], [3, 1, 2], [-1, 3, 2]]

"""
# To print the clauses to clauses.qhe
for i in range(len(problem)):
    for j in range(len(problem[i])):    
        print(f'{problem[i][j]} -> clause{i+1}.[{j+1}]')
"""

# To print the hard-coded file

spaces = 4
for i in range(len(problem)):
    tabs = ' '*spaces
    print(f"{tabs}# Clause {i+1}")
    print(f"{tabs}clause{i+1}.[1] -> t1")
    print(f"{tabs}clause{i+1}.[2] -> t2")
    print(f"{tabs}clause{i+1}.[3] -> t3")
    print(f"{tabs}proj(t1,t2,t3)[", end='')
    for j in range(len(problem[i])):
        if j != len(problem[i]) - 1:
            print(f"q.[{abs(problem[i][j])}],", end='')
        else:
            print(f"q.[{abs(problem[i][j])}],anc]")
    print(f"{tabs}measure[anc] -> m_anc")
    print(f"{tabs}m_anc == 0 -> test")
    print(f"{tabs}if test")
    spaces += 4

"""
spaces = 4
for i in reversed(range(len(problem))):
    tabs = ' '*i*spaces
    two_tabs = ' '*(i+1)*spaces
    print(f"{tabs}end")
    print(f"{tabs}1-test -> test_not")
    print(f"{tabs}if test_not")
    print(f"{two_tabs}gosub initialize")
    print(f"{tabs}end")
"""