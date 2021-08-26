import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class GraphVertex:
    white, gray, black = range(3)
    def __init__(self) -> None:
        self.color = GraphVertex.white
        self.edges: List['GraphVertex'] = []



def is_deadlocked(graph: List[GraphVertex]) -> bool:
    def has_cyle(cur):
        if cur.color == GraphVertex.gray:
            return True

        cur.color = GraphVertex.gray

        if any(next.color != GraphVertex.black and has_cyle(next) for next in cur.edges):
            return True
        cur.color = GraphVertex.black
        return False


    return any(vertex.color == GraphVertex.white and has_cyle(vertex) for vertex in graph)


@enable_executor_hook
def is_deadlocked_wrapper(executor, num_nodes, edges):
    if num_nodes <= 0:
        raise RuntimeError('Invalid num_nodes value')
    graph = [GraphVertex() for _ in range(num_nodes)]

    for (fr, to) in edges:
        if fr < 0 or fr >= num_nodes or to < 0 or to >= num_nodes:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(is_deadlocked, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('deadlock_detection.py',
                                       'deadlock_detection.tsv',
                                       is_deadlocked_wrapper))
