def fractional_knapsack(items, capacity):
  """
  Solve the Fractional Knapsack Problem using Greedy Algorithm.

  Args:
    items: A list of items, where each item is a tuple of (value, weight).
    capacity: The capacity of the knapsack.

  Returns:
    The maximum value that can be fit into the knapsack.
  """

  items.sort(key=lambda x: x[0] / x[1], reverse=True)

  total_value = 0
  remaining_capacity = capacity

  for item in items:
    if remaining_capacity >= item[1]:
      total_value += item[0]
      remaining_capacity -= item[1]
    else:
      total_value += item[0] * remaining_capacity / item[1]
      remaining_capacity = 0

  return total_value


if __name__ == "__main__":
  items = [(60, 10), (100, 20), (120, 30)]
  capacity = 50

  total_value = fractional_knapsack(items, capacity)

  print(total_value)