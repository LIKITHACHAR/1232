def chained_matrix_multiplication(matrices):
  """
  Chained matrix multiplication algorithm.

  Args:
    matrices: A list of matrices.

  Returns:
    The minimum number of multiplications required to multiply the matrices.
  """

  n = len(matrices)
  M = [[float("inf") for _ in range(n)] for _ in range(n)]

  for i in range(n):
    M[i, i] = 0

  for l in range(2, n + 1):
    for i in range(n - l + 1):
      j = i + l - 1
      for k in range(i + 1, j):
        cost = M[i, k] + M[k, j] + matrices[i].shape[0] * matrices[k].shape[1] * matrices[j].shape[1]
        if cost < M[i, j]:
          M[i, j] = cost

  return M[0, n - 1]

if __name__ == "__main__":
  matrices = [[3, 4], [4, 2], [2, 5]]
  print(chained_matrix_multiplication(matrices))
