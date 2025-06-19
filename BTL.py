import numpy as np

def makesimilar(A):
    Q, R = np.linalg.qr(A)
    B = np.dot(R,Q)
    return B

def eig_qr(A):
    B = makesimilar(A)
    iters = 0
    leig = B[-1, -1]
    diff = 1
    while diff > 1e-32:
        B = makesimilar(B)
        iters += 1
        diff = abs(leig - B[-1, -1])
        leig = B[-1, -1]
    print(f"A_{iters} = \n {B}")
    eigs = [B[i, i] for i in range(len(B))]
    return eigs, iters

# Example usage
A = np.array([[41, 12, 87], [62, 63, 98], [72, 21, 61]])

eigs, iters = eig_qr(A)
print(f"Matrix A:\n{A}")
print(f"Eigenvalues: {eigs}")
print(f"Iterations: {iters}")

