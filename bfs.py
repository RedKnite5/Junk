# bfs.py
# by Max Friedman

def BFS(adj: Iterable[Iterable[int]], start: int) -> list[int]:
    """Breadth first traversal"""

    q: Queue[int] = Queue()
    visited: list[int] = [start]

    q.put(start)

    current: int
    while (not q.empty()):
        current = q.get()
        for neighbor in adj[current]:
            if neighbor in visited:
                continue
            q.put(neighbor)
            visited.append(neighbor)
    return visited


def main(adjacency_list: Iterable[Iterable[int]]):
    visited = BFS(adjacency_list, 0)
    print("Visited: ", visited)


if __name__ == "__main__":

    adjacency_list: tuple[tuple[int]] = (
        (1, 2, 3),
        (0, 4, 5, 6),
        (0,),
        (0, 7, 8),
        (1, 9),
        (1,),
        (1,),
        (3,),
        (3,),
        (4,)
    )

    main(adjacency_list)
