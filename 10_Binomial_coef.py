def binomial_coefficient(n, k):
  """
  Calculates the binomial coefficient nCr.

  Args:
    n: The number of trials.
    k: The number of successes.

  Returns:
    The binomial coefficient nCr.
  """

  if k > n:
    raise ValueError("k must be less than or equal to n.")

  if k == 0 or k == n:
    return 1

  return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)

if __name__ == "__main__":
  print(binomial_coefficient(5, 2))
