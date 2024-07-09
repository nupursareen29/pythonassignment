
### 2. `main.py`

"""
Assignment: Implement the most efficient algorithm to solve the given problem.

Problem Statement:
You are given a Directed Acyclic Graph (DAG) with `n` nodes, numbered from `0` to `n-1`.
The graph is represented as an adjacency list where `graph[i]` is a list of tuples `(j, w)`,
representing an edge from node `i` to node `j` with weight `w`. Your task is to find the longest
path in the graph starting from any node.

Function Signature:
def longest_path(graph: list) -> int:

Parameters:
- graph (list): A list of lists, where `graph[i]` contains tuples `(j, w)` representing an edge
  from node `i` to node `j` with weight `w`.

Returns:
- int: The length of the longest path in the graph.

Example:
>>> graph = [
...     [(1, 3), (2, 2)],
...     [(3, 4)],
...     [(3, 1)],
...     []
... ]
>>> longest_path(graph)
7
"""

def longest_path(graph: list) -> int:
    topo_order = topological_sort(graph)
    longest_path_length = calculate_longest_path(graph, topo_order)
    return longest_path_length
    


def topological_sort(graph):
    from collections import deque
    
    n = len(graph)
    indegree = [0] * n
    
    # Calculate indegree for each node
    for neighbors in graph:
        for neighbor, _ in neighbors:
            indegree[neighbor] += 1
    
    # Queue for nodes with zero indegree
    queue = deque()
    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)
    
    topo_order = []
    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for neighbor, _ in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    return topo_order

# Function to calculate longest path using topological sort
def calculate_longest_path(graph, topo_order):
    n = len(graph)
    dp = [-float('inf')] * n
    dp[topo_order[0]] = 0  # Start from the first node in topo_order
    
    for node in topo_order:
        if dp[node] != -float('inf'):  # If node is reachable
            for neighbor, weight in graph[node]:
                dp[neighbor] = max(dp[neighbor], dp[node] + weight)
    
    return max(dp)