"""Shortest paths for directed graphs with non-negative edge weights."""
from __future__ import annotations

import heapq
from itertools import count


def dijkstra(graph: dict, start: str) -> tuple[dict, dict]:
    """Return distance and predecessor maps, including destination-only nodes.

    The graph is not modified. Negative or NaN weights raise ValueError;
    infinite weights are treated as unreachable connections.
    """
    nodes = set(graph)
    nodes.add(start)
    for neighbors in graph.values():
        for node, weight in neighbors.items():
            if weight < 0 or weight != weight:
                raise ValueError("Dijkstra requires non-negative, non-NaN weights")
            nodes.add(node)

    distances = dict.fromkeys(nodes, float("inf"))
    previous = dict.fromkeys(nodes, None)
    distances[start] = 0
    order = count()
    queue = [(0, next(order), start)]
    while queue:
        distance, _, node = heapq.heappop(queue)
        if distance != distances[node]:
            continue
        for neighbor, weight in graph.get(node, {}).items():
            candidate = distance + weight
            if candidate < distances[neighbor]:
                distances[neighbor] = candidate
                previous[neighbor] = node
                heapq.heappush(queue, (candidate, next(order), neighbor))
    return distances, previous


def shortest_path(previous: dict, start: str, end: str) -> list[str] | None:
    """Reconstruct a path, or return None for an unreachable/invalid chain."""
    if start not in previous or end not in previous:
        return None
    result = []
    seen = set()
    node = end
    while node is not None and node not in seen:
        result.append(node)
        if node == start:
            return result[::-1]
        seen.add(node)
        node = previous.get(node)
    return None
