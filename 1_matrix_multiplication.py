def multiply_matrices(A, B):
  """
  Multiply two matrices.

  Args:
    A: The first matrix.
    B: The second matrix.

  Returns:
    The product of the two matrices.
  """

  n = len(A)
  m = len(A[0])
  p = len(B[0])

  C = [[0 for _ in range(p)] for _ in range(n)]

  for i in range(n):
    for j in range(p):
      for k in range(m):
        C[i][j] += A[i][k] * B[k][j]

  return C


if __name__ == "__main__":
  A = [[1, 2], [3, 4]]
  B = [[5, 6], [7, 8]]

  C = multiply_matrices(A, B)

  print(C)