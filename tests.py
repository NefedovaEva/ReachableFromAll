from find_reachable_vertices import (
    read_incidence_matrix,
    reverse_incidence_matrix,
    dfs,
    find_vertices_reachable_from_all,
)


CHAIN = [
    [1, 0],
    [-1, 1],
    [0, -1],
]

DIAMOND = [
    [1, 1, 0, 0],
    [-1, 0, 1, 0],
    [0, -1, 0, 1],
    [0, 0, -1, -1],
]

CYCLE = [
    [1, 0, -1],
    [-1, 1, 0],
    [0, -1, 1],
]

SINGLE_EDGE = [
    [1],
    [-1],
]

NO_EDGES = [
    [0, 0],
    [0, 0],
]

TWO_COMPONENTS = [
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1],
]


def test_reverse_empty_matrix_gives_empty():
    assert reverse_incidence_matrix([]) == []


def test_reverse_flips_signs():
    matrix = [[0, 1], [-1, 0]]
    assert reverse_incidence_matrix(matrix) == [[0, -1], [1, 0]]


def test_reverse_does_not_mutate_input():
    matrix = [[0, 1], [-1, 0]]
    reverse_incidence_matrix(matrix)
    assert matrix == [[0, 1], [-1, 0]]


def test_dfs_from_isolated_vertex():
    assert dfs([[0]], 0) == 0


def test_dfs_chain_forward():
    assert dfs(CHAIN, 0) == 2


def test_dfs_chain_from_end():
    assert dfs(CHAIN, 2) == 0


def test_dfs_diamond():
    assert dfs(DIAMOND, 0) == 3


def test_dfs_cycle():
    assert dfs(CYCLE, 0) == 2
    assert dfs(CYCLE, 1) == 2


def test_reachable_empty_matrix():
    assert find_vertices_reachable_from_all([]) == []


def test_reachable_single_vertex():
    assert find_vertices_reachable_from_all([[0]]) == [1]


def test_reachable_single_edge():
    assert find_vertices_reachable_from_all(SINGLE_EDGE) == [2]


def test_reachable_diamond_from_file():
    input_matrix = read_incidence_matrix("test_data/input.txt")
    assert find_vertices_reachable_from_all(input_matrix) == [4]


def test_reachable_no_edges():
    assert find_vertices_reachable_from_all(NO_EDGES) == []


def test_reachable_two_components():
    assert find_vertices_reachable_from_all(TWO_COMPONENTS) == []


def test_reachable_cycle():
    assert find_vertices_reachable_from_all(CYCLE) == [1, 2, 3]


def test_read_matrix_from_file():
    assert read_incidence_matrix("test_data/matrix_with_empty_lines.txt") == [
        [0, 1, -1],
        [1, 0, -1],
        [-1, -1, 0],
    ]


def test_read_empty_file():
    assert read_incidence_matrix("test_data/empty.txt") == []


def test_read_file_with_only_empty_lines():
    assert read_incidence_matrix("test_data/only_empty_lines.txt") == []


def test_read_input_file():
    assert read_incidence_matrix("test_data/input.txt") == [
        [1, 1, 0, 0],
        [-1, 0, 1, 0],
        [0, -1, 0, 1],
        [0, 0, -1, -1],
    ]


def test_read_ragged_rows():
    assert read_incidence_matrix("test_data/ragged_rows.txt") == [
        [0, 1, -1],
        [1, 0],
        [-1],
    ]


if __name__ == "__main__":
    test_reverse_empty_matrix_gives_empty()
    test_reverse_flips_signs()
    test_reverse_does_not_mutate_input()

    test_dfs_from_isolated_vertex()
    test_dfs_chain_forward()
    test_dfs_chain_from_end()
    test_dfs_diamond()
    test_dfs_cycle()

    test_reachable_empty_matrix()
    test_reachable_single_vertex()
    test_reachable_single_edge()
    test_reachable_diamond_from_file()
    test_reachable_no_edges()
    test_reachable_two_components()
    test_reachable_cycle()

    test_read_matrix_from_file()
    test_read_empty_file()
    test_read_file_with_only_empty_lines()
    test_read_input_file()
    test_read_ragged_rows()

    print("All tests passed")
