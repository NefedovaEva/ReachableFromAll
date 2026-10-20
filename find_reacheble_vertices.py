def read_incidence_matrix(filename):
    """
    Reads incidence matrix from file.
    Returns list of matrix rows (list[list[int]]).
    """
    with open(filename, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    return [list(map(int, line.split())) for line in lines]


def reverse_incidence_matrix(matrix):
    """
    Returns new incidence matrix with reversed edge directions.
    """
    return [[-x for x in row] for row in matrix]


def dfs(matrix, start):
    """
    DFS on the given incidence matrix starting from given vertex.

    Returns the number of reachable vertices (excluding start itself).
    """
    n = len(matrix)
    m = len(matrix[0]) if n > 0 else 0

    visited_vertices = [False] * n
    visited_vertices[start] = True
    stack = [start]
    count = 0

    while stack:
        current_vertex = stack.pop()

        for j in range(m):
            if matrix[current_vertex][j] != 1:
                continue

            for i in range(n):
                if matrix[i][j] == -1:
                    if not visited_vertices[i]:
                        visited_vertices[i] = True
                        stack.append(i)
                        count += 1
                    break

    return count


def find_vertices_reachable_from_all(incidence_matrix):
    """
    Finds all vertices reachable from every other vertex.

    Algorithm description: reverse all edge directions in incidence matrix,
    then runs DFS from each vertex on reversed graph. Vertex V
    is reachable from all other vertices iff all other n - 1 vertices
    are reachable from V in the reversed graph.

    Takes incidence matrix (list[list[int]].

    Returns list of vertex numbers reachable from all other vertices.
    """
    n = len(incidence_matrix)
    if n == 0:
        return []

    reversed_matrix = reverse_incidence_matrix(incidence_matrix)

    answer = []
    for v in range(n):
        if dfs(reversed_matrix, v) == n - 1:
            answer.append(v + 1)

    return answer


def main():
    incidence_matrix = read_incidence_matrix("test/input.txt")
    result = find_vertices_reachable_from_all(incidence_matrix)

    if result:
        print("Vertices reachable from all other vertices:", result)
    else:
        print("No vertices are reachable from all other vertices")


if __name__ == "__main__":
    main()