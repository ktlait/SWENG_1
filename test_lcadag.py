import pytest
import lcadac

def test_print():
    my_graph = {"A": set(), #                 A
            "B": set(["A"]),#               /  \
            "C": set(["A"]),#             B     C
            "D": set(["C"]), #             \  /  \
            "E": set(["B", "C"]),#          E     D
            "F": set(["E"])}#                \
                          #                   F
    graph = lcadac.Graph(my_graph)
    paths = graph.bfs("A", "D")
    assert graph.print_paths(paths)== "D --> C --> A --> END\n"

    paths = graph.bfs("A", "E")
    assert graph.print_paths(paths) == "E --> B --> A --> END\nE --> C --> A --> END\n"

def test_add_graph():
    yield
def test_init():
    yield
def test_LCADAG():
    yield
def test_error_LCADAG():
    yield
def bfs_test():
    yield
def bfs_test_error():
    yield
    
