
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        visited = {}
        
        def dfs(original):
            if original in visited:
                return visited[original]
            
            # Create clone
            clone = Node(original.val)
            visited[original] = clone
            
            # Recursively clone all neighbors
            for neighbor in original.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone
        
        return dfs(node)
    
# Example usage:
# Creating a sample graph:
# Node 1 connected to Node 2 and Node 4
# Node 2 connected to Node 1 and Node 3
# Node 3 connected to Node 2 and Node 4
# Node 4 connected to Node 1 and Node 3
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]
solution = Solution()
cloned_graph = solution.cloneGraph(node1)
# To verify the cloned graph, we can print the values and neighbors of the cloned nodes
def print_graph(node, visited=set()):
    if node in visited:
        return
    visited.add(node)
    print(f"Node {node.val} with neighbors {[neighbor.val for neighbor in node.neighbors]}")
    for neighbor in node.neighbors:
        print_graph(neighbor, visited)
print("Original graph:")
print_graph(node1)
print("\nCloned graph:")
print_graph(cloned_graph)



#Alternatively best solution using BFS
# from collections import deque
# from typing import Optional
# class Solution:
#     def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
#         if not node:
#             return None

#         q = deque([node])
#         new = Node(node.val)
#         copies = {node: new}

#         while q:
#             node = q.popleft()
#             node_copy = copies[node]
#             for neighbor in node.neighbors:
#                 if neighbor not in copies:
#                     copies[neighbor] = Node(neighbor.val)
#                     q.append(neighbor)
#                 node_copy.neighbors.append(copies[neighbor])

#         return new