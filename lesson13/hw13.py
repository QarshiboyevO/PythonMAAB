import numpy as np

# 1. Vector from 10 to 49
v = np.arange(10, 50)
print("1. Vector 10 to 49:\n", v)

# 2. 3x3 matrix from 0 to 8
m1 = np.arange(9).reshape(3, 3)
print("\n2. 3x3 Matrix 0 to 8:\n", m1)

# 3. 3x3 identity matrix
I = np.eye(3)
print("\n3. Identity Matrix:\n", I)

# 4. 3x3x3 random array
arr3d = np.random.rand(3, 3, 3)
print("\n4. 3x3x3 Random Array:\n", arr3d)

# 5. 10x10 random array, min & max
arr10 = np.random.rand(10, 10)
print("\n5. Min:", arr10.min())
print("   Max:", arr10.max())

# 6. Random vector size 30, mean
vec30 = np.random.rand(30)
print("\n6. Mean of vector:", vec30.mean())

# 7. Normalize 5x5 matrix
m5 = np.random.rand(5, 5)
norm = (m5 - m5.min()) / (m5.max() - m5.min())
print("\n7. Normalized Matrix:\n", norm)

# 8. Multiply 5x3 by 3x2
A = np.random.rand(5, 3)
B = np.random.rand(3, 2)
print("\n8. Matrix Product (5x3 * 3x2):\n", A @ B)

# 9. Dot product of two 3x3 matrices
X = np.random.rand(3, 3)
Y = np.random.rand(3, 3)
print("\n9. Dot Product:\n", np.dot(X, Y))

# 10. Transpose of 4x4 matrix
M4 = np.random.rand(4, 4)
print("\n10. Transpose:\n", M4.T)

# 11. Determinant of 3x3 matrix
D = np.random.rand(3, 3)
print("\n11. Determinant:", np.linalg.det(D))

# 12. A(3x4) * B(4x3)
A = np.random.rand(3, 4)
B = np.random.rand(4, 3)
print("\n12. A * B:\n", A @ B)

# 13. Matrix-vector product
M = np.random.rand(3, 3)
v = np.random.rand(3, 1)
print("\n13. Matrix-Vector Product:\n", M @ v)

# 14. Solve Ax = b
A = np.array([[2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]])
b = np.array([8, -11, -3])
x = np.linalg.solve(A, b)
print("\n14. Solution x:\n", x)

# 15. Row-wise and column-wise sums
M5 = np.random.rand(5, 5)
print("\n15. Row-wise sum:", M5.sum(axis=1))
print("    Column-wise sum:", M5.sum(axis=0))