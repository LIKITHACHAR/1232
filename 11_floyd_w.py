def floyd_warshall(graph):
  """
  Floyd-Warshall algorithm.

  Args:
    graph: A graph represented as a list of adjacency lists.

  Returns:
    A matrix of distances between all pairs of vertices.
  """

  n = len(graph)
  distances = [[float("inf") for _ in range(n)] for _ in range(n)]

  for i in range(n):
    for j in range(n):
      if graph[i][j] is not None:
        distances[i][j] = graph[i][j]

  for k in range(n):
    for i in range(n):
      for j in range(n):
        if distances[i][j] > distances[i][k] + distances[k][j]:
          distances[i][j] = distances[i][k] + distances[k][j]

  return distances

if __name__ == "__main__":
  graph = {
    "A": ["B", "C", "D"],
    "B": ["A", "C"],
    "C": ["A", "B", "D"],
    "D": ["A", "C"]
  }
  distances = floyd_warshall(graph)
  print(distances)
