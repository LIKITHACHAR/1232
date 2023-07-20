def selection_sort(numbers):
  """
  Sort a list of numbers using Selection Sort algorithm.

  Args:
    numbers: A list of numbers.

  Returns:
    A sorted list of numbers.
  """

  n = len(numbers)

  for i in range(n):
    min_index = i
    for j in range(i + 1, n):
      if numbers[j] < numbers[min_index]:
        min_index = j

    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

  return numbers


if __name__ == "__main__":
  numbers = [55, 25, 15, 40, 60, 35, 17, 65, 75, 10]

  sorted_numbers = selection_sort(numbers)

  print(sorted_numbers)