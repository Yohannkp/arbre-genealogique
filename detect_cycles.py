import json
import sys
from collections import defaultdict

def load_edges(filename):
    with open(filename, encoding="utf-8") as f:
        data = json.load(f)
    edges = defaultdict(list)
    for link in data:
        edges[link["parent"]].append(link["child"])
    return edges

def find_cycles(edges):
    visited = set()
    stack = []
    cycles = []

    def visit(node, path):
        if node in path:
            cycle = path[path.index(node):] + [node]
            cycles.append(cycle)
            return
        if node in visited:
            return
        visited.add(node)
        for child in edges.get(node, []):
            visit(child, path + [node])

    for node in edges:
        visit(node, [])
    return cycles

if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else "parentages.json"
    edges = load_edges(filename)
    cycles = find_cycles(edges)
    if cycles:
        print("Cycles détectés :")
        for cycle in cycles:
            print(" -> ".join(cycle))
    else:
        print("Aucun cycle détecté.")