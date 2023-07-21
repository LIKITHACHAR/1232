import heapq

def dijkstra(graph, source):
  """
  Dijkstra's algorithm.

  Args:
    graph: A graph represented as a list of adjacency lists.
    source: The source vertex.

  Returns:
    A dictionary mapping each vertex to its shortest distance from the source.
  """

  distances = {}
  for vertex in graph:
    distances[vertex] = float("inf")

  distances[source] = 0
  pq = []
  heapq.heappush(pq, (0, source))

  while pq:
    dist, vertex = heapq.heappop(pq)

    if distances[vertex] < dist:
      continue

    for neighbor, weight in graph[vertex]:
      new_dist = dist + weight
      if new_dist < distances[neighbor]:
        distances[neighbor] = new_dist
        heapq.heappush(pq, (new_dist, neighbor))

  return distances

if __name__ == "__main__":
  graph = {
    "A": ["B", "C", "D"],
    "B": ["A", "C"],
    "C": ["A", "B", "D"],
    "D": ["A", "C"]
  }
  distances = dijkstra(graph, "A")
  print(distances)
