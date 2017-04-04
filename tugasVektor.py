import numpy as np
m = np.mat("0 0 -2; 1 2 1; 1 0 3")
eigenvalue,eigenvektor = np.linalg.eig(m)
print(eigenvalue)
print(eigenvektor)