# Horizon-3SAT
## Final Files
### 3A Files
Contains all code relevant to Triple Alpha including projector matrices generation, Helium and Hydrogen files, clauses, and code to print a 3A file until hard-coding is required.
3A-gen-3SAT generates a valid 3-SAT problem (solved by Schöning to ensure that there is only a single unique solution). 

### Problems
Contains all valid, generated 3-SAT problems. Validity is tested according to the BZF paper, and tested 50-100 times using Schöning's algorithm to ensure that the problems have a single, unique solution. 

## Solutions
Re-solved solutions and their assignments using Schöning's algorithm, and the BZF algorithm. Contains both the "number of iterations" (c) results (COUNTS), and the boolean assignment for each problem (SOLUTIONS).

## Other Files
For generating plots, the outline of the Schöning algorithm, the 3-SAT generation algorithm, etc. 
### Schöning vs Schöning Solver
Schöning is the general file that defines the Schöning function. Schöning solver uses it to solve the 3-SAT problems.
Unique3SAT ensures that the generate() and is_valid() functions from the threeSATgen file generate valid 3-SAT problems with single, unique solutions. 
### Plot.py
Imports the generated data from the other files and plots the different plots in the folder "Figures".
