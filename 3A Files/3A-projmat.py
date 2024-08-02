import numpy as np
import random

problem = []
choices = [True, False]
while len(problem) != 8:
    clause = [random.choice(choices), random.choice(choices), random.choice(choices)]
    if clause not in problem: problem.append(clause)

print(problem)
print(len(problem))

projmat_list = {}
init_thet = 0.7*np.pi/2

def rymat(theta):
    return np.array([[np.cos(theta/2), -np.sin(theta/2)],[np.sin(theta/2), np.cos(theta/2)]])

sigx = np.array([[0,1],[1,0]])

def sq_plus():
    return 1/np.sqrt(2) * np.array([1, 1])

for clause in problem:
    statev = []
    signs = str(clause)#str([i < 0 for i in clause])
    if signs not in projmat_list:
        for lit in range(len(clause)):
            lit = clause[lit]
            if lit < 0:
                st = rymat(np.pi - init_thet).dot(sq_plus())
            else:
                st = rymat(np.pi + init_thet).dot(sq_plus())
            statev.append(st)

        total_statev = statev[0]
        if len(statev) > 1:
            for ii in range(1,len(statev)):
                total_statev = np.kron(total_statev, statev[ii])

        
        projmat = np.outer(total_statev, total_statev)
        assert(np.allclose(projmat.dot(projmat), projmat)) # Sanity check to ensure that P^2 = P
        unitary_projmat = np.kron(projmat, sigx) + np.kron((np.eye(8) - projmat),np.eye(2))
        assert(np.allclose(np.matmul(np.linalg.inv(unitary_projmat),unitary_projmat),np.eye(16))) # U^-1U = I
        projmat_list[str(signs)]=unitary_projmat.tolist()
#print(projmat_list)