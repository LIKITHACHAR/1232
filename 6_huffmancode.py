import heapq

def huffman_coding(characters):
  """
  Huffman coding algorithm.

  Args:
    characters: A list of characters, where each character is a string.

  Returns:
    A dictionary mapping each character to its Huffman code.
  """

  frequencies = {}
  for character in characters:
    frequencies[character] = 0
  for character in characters:
    frequencies[character] += 1

  nodes = []
  for character, frequency in frequencies.items():
    nodes.append((frequency, character))
  heapq.heapify(nodes)

  while len(nodes) > 1:
    frequency1, character1 = heapq.heappop(nodes)
    frequency2, character2 = heapq.heappop(nodes)
    new_frequency = frequency1 + frequency2
    new_character = character1 + character2
    nodes.append((new_frequency, new_character))

  root = nodes[0][1]
  codes = {}
  def _build_codes(node, code):
    if not node:
      return
    if isinstance(node, str):
      codes[node] = code
      return
    _build_codes(node.left, code + "0")
    _build_codes(node.right, code + "1")
  _build_codes(root, "")
  return codes

if __name__ == "__main__":
  characters = ["a", "b", "c", "d", "e"]
  codes = huffman_coding(characters)
  print(codes)
