import functools
from typing import List
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class GraphVertex:
    white, gray, black = range(3)
    def __init__(self, data=None):
        self.data = None
        self.color = GraphVertex.white
        self.edges: [GraphVertex] = []


def is_deadlocked(G):
    def has_cycle(curr: GraphVertex):
        if curr.color == GraphVertex.gray:
            return True
        curr.color = GraphVertex.gray

        if any(next.color != GraphVertex.black and has_cycle(next)
               for next in curr.edges):
            return True
        return False

    return any(vertex.color == GraphVertex.white and has_cycle(vertex)
               for vertex in G)

A = GraphVertex('A')
B = GraphVertex('B')
C = GraphVertex('C')
D = GraphVertex('D')

A.edges = [B]
B.edges = [A, C]
C.edges = [B, D]
# D.edges = [A]
G = [A, B, C, D]
print(F"is_deadlocked(G) = {is_deadlocked(G)}")

# @enable_executor_hook
# def is_deadlocked_wrapper(executor, num_nodes, edges):
#     if num_nodes <= 0:
#         raise RuntimeError('Invalid num_nodes value')
#     graph = [GraphVertex() for _ in range(num_nodes)]
#
#     for (fr, to) in edges:
#         if fr < 0 or fr >= num_nodes or to < 0 or to >= num_nodes:
#             raise RuntimeError('Invalid vertex index')
#         graph[fr].edges.append(graph[to])
#
#     return executor.run(functools.partial(is_deadlocked, graph))
#
#
# if __name__ == '__main__':
#     exit(
#         generic_test.generic_test_main('deadlock_detection.py',
#                                        'deadlock_detection.tsv',
#                                        is_deadlocked_wrapper))