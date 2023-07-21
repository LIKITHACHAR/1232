import heapq

def prim(graph):
  """
  Prim's algorithm.

  Args:
    graph: A graph represented as a list of adjacency lists.

  Returns:
    A list of edges in the minimum spanning tree.
  """

  mst = []
  visited = set()
  pq = []
  heapq.heappush(pq, ("0", "A"))

  while pq:
    dist, vertex = heapq.heappop(pq)

    if vertex in visited:
      continue

    visited.add(vertex)
    mst.append((vertex, dist))

    for neighbor, weight in graph[vertex]:
      if neighbor not in visited:
        new_dist = dist + weight
        heapq.heappush(pq, (new_dist, neighbor))

  return mst

if __name__ == "__main__":
  graph = {
    "A": ["B", "C", "D"],
    "B": ["A", "C"],
    "C": ["A", "B", "D"],
    "D": ["A", "C"]
  }
  mst = prim(graph)
  print(mst)
