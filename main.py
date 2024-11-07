import numpy as np
A = np.array(([4, 2, 1,],
              [2, 3, 1],
              [5, 7, 8]))
print("Original matrix A:")
print(A)


eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalue Decompsition")
print("Egienvalues :\n", eigenvalues)
print("Egienvectors:\n",eigenvectors)


U, S, Vt = np.linalg.svd(A)
print("\n singular Value Decompsition")
print("U Matrix:\n", U)
print("S Singular:\n", S)
print("Vt Matrix:\n", Vt)

#Reconstruct the matrix using SVD components
A_reconstructed = U @ np.diag(S) @ Vt
print("\nConstructed Martix from SVD: ")
print(A_reconstructed)

