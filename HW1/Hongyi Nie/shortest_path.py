# Hongyi Nie, hn327

# Please see instructions.pdf for the description of this problem.

def shortest_path(graph, source, target):
  # `graph` is an object that provides a get_neighbors(node) method that returns
  # a list of (node, weight) edges. both of your graph implementations should be
  # valid inputs. you may assume that the input graph is connected, and that all
  # edges in the graph have positive edge weights.
  #
  # `source` and `target` are both nodes in the input graph. you may assume that
  # at least one path exists from the source node to the target node.
  #
  # this method should return a tuple that looks like
  # ([`source`, ..., `target`], `length`), where the first element is a list of
  # nodes representing the shortest path from the source to the target (in
  # order) and the second element is the length of that path
  #
  # NOTE: Please see instructions.pdf for additional information about the
  # return value of this method.

  # TODO: YOUR CODE HERE, delete the `raise NotImplementedError`line below once you finish writing your code

    nodes = []
    dist = [[0,source,[source]]]
    #visited = set()
    # for node in graph:
    #        # dist[node]  = 10000000000000000000
    #        nodes.append(node)
    #        #visited.append(node)

    while len(dist) >= 1:
      node = min((x for x in dist), key = lambda y : y[0])
      if node[1] == target:
          return node[2], node[0]
      else:
          for neighbor in graph.get_neighbors(node[1]):
              alt = node[0] + neighbor[1]
              #update path
              path = node[2][:]
              path.append(neighbor[0])
              found = False
              for x in dist:
                  if x[1] == neighbor[0]:
                      found = True
                      if alt < x[0]:
                          x[0] = alt
                          x[2] = path
              if not found:
                  dist.append([alt, neighbor[0], path])
          dist.remove(node)
