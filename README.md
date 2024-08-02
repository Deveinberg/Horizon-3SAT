# Horizon-3SAT
## Final Files
### 3A Files
Contains all code relevant to Triple Alpha including projector matrices generation, Helium and Hydrogen files, clauses, and code to print a 3A file until hard-coding is required.

### Problems
Contains all valid, generated 3-SAT problems. Validity is tested according to the BZF paper, and tested 50-100 times using Schöning's algorithm to ensure that the problems have a single, unique solution. 

## Solutions
Re-solved solutions and their assignments using Schöning's algorithm, and the BZF algorithm. 

## Other Files
For generating plots, the outline of the Schöning algorithm, the 3-SAT generation algorithm, etc. 
### Schöning vs Schöning Solver
Schöning is the general file that defines the Schöning function. Schöning solver uses it to solve the 3-SAT problems.
Unique3SAT ensures that the generate() and is_valid() functions from the threeSATgen file generate valid 3-SAT problems with single, unique solutions. 
