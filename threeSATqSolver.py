import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.compiler import transpile
from qiskit.circuit.library import UnitaryGate
from qiskit_aer import AerSimulator

def bzf(num_bits, sat_prob):
    def rymat(theta):
        mat = np.array([[np.cos(theta/2), -np.sin(theta/2)],[np.sin(theta/2), np.cos(theta/2)]])
        return mat

    def sq_plus():
        return 1/np.sqrt(2) * np.array([1, 1])


    def measure_circ(circuit, shots):
        simulator = AerSimulator()
        compiled_circuit = transpile(circuit, simulator)
        sim_result = simulator.run(compiled_circuit, shots = shots).result()
        counts = sim_result.get_counts()
        return counts


    def sat3(bitstring, clauses):
        # 1 is true, 0 is false

        set_ = []
        for clause in clauses:

            bitlist = []
            for literal in clause:
                idx = abs(literal) - 1 # 1 based indexing
                if literal < 0:

                    bitlist.append(not(bitstring[idx]))
                else:

                    bitlist.append(bitstring[idx])
            
            sat_clause = bitlist[0] or bitlist[1] or bitlist[2]

            set_.append(sat_clause)

        finalsat = set_[0]
        if len(set_) >1:
            for i_ in range(1, len(set_)):
                finalsat = finalsat and set_[i_]
        return bool(finalsat)
            
    ###########################################################################

    sigx = np.array([[0, 1],[1,0]]) # Sigma X

###########################################################################

    projmat_list = []
    init_thet = 0.7*np.pi/2

    for clause in sat_prob:
        statev = []
        for lit in reversed(range(len(clause))):
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
        projmat_list.append(projmat)

###########################################################################

    cmax = 3*num_bits
    clause_anc = QuantumRegister(1, 'anc') 
    sol_reg = QuantumRegister(num_bits, 'qreg') 
    creg = ClassicalRegister(cmax + num_bits)
    qc = QuantumCircuit(clause_anc, sol_reg, creg)


    for qubit_id in range(num_bits):
        qc.h(sol_reg[qubit_id])


    for cc in range(cmax):
        for c_id in range(len(sat_prob)):
            unitary_mat = np.kron(sigx, projmat_list[c_id]) + np.kron( np.eye(2), (np.eye(8) - projmat_list[c_id]))
            
            # Sanity check to ensure that matrix is unitary
            assert(np.allclose(unitary_mat.dot(np.conj(unitary_mat).T), np.eye(16))) 


            qc.append(UnitaryGate(unitary_mat, label="UProj" + str(c_id)), [sol_reg[abs(sat_prob[c_id][0])-1],
                                                                            sol_reg[abs(sat_prob[c_id][1])-1],
                                                                            sol_reg[abs(sat_prob[c_id][2])-1],
                                                                            clause_anc[0],
                                                                        ])
        qc.measure(clause_anc[0], creg[cc])        # Measure ancilla qubit
        qc.reset(clause_anc[0])                    # Reset ancilla qubit

    qc.barrier()

    for qubit_id in range(num_bits):
        qc.measure(sol_reg[qubit_id], creg[qubit_id + cmax])


    # qc.draw(fold=1000)

    ###########################################################################

    # Make measurement on circuit
    counts = dict(measure_circ(qc, 10000))
    ###########################################################################

    # Postselection. Only choose measurements where all ancilla measured values are 1.

    num_sols = 0
    probsol = dict({})
    valid_sols = []

    for key,val in counts.items():
        if key.endswith("1" * cmax):

            key = key[:num_bits][::-1]
            probsol[key] = val

            bitstr = [int(x) for x in key]
            sat_value = sat3(bitstr, sat_prob)
            #print("Solution:", key, ", Valid:",sat_value)
            if sat_value:
                valid_sols = key
                num_sols = num_sols + 1

    # assert(len(probsol) > 0)

    #print("Number of solutions found:", num_sols)

    valid_sol_dict = {}
    for i in range(len(valid_sols)):
        if int(valid_sols[i]) == 0:
            valid_sol_dict[i+1] = False
        else:
            valid_sol_dict[i+1] = True
    return valid_sol_dict

#sat_prob = [(-1, -7, -5), (-6, -1, -7), (-7, -8, 1), (3, 5, -4), (8, 4, 5), (1, 6, 2), (7, -5, -1), (-3, 4, -8), (6, 4, 1), (-6, 3, 4), (-2, -8, -6), (1, -3, -5), (-8, 4, 2), (3, 7, -6), (8, -3, -4), (-2, 6, -1), (-2, 5, -8), (8, -1, 7), (-7, 1, 4), (-2, 3, 1), (4, 7, -8), (-2, 7, 4), (-4, 1, -3), (-2, -7, -4), (7, 8, 1), (1, 3, -2), (3, -1, 6), (-6, 5, 3), (-6, -8, 5), (-4, -1, 8), (-6, 2, -4), (-4, 8, -6), (7, -3, 6), (-3, -2, -4)]
#print(bzf(8, sat_prob))