'''
    Python3 program to print DepthFirstSearch traversal for complete graph
    given a social network of friends, create a function to find if a friend is a distant friend of another friend.

    ie: if A is a friend of B, and B is a friend of C, then A is a distant friend of C.
'''
from collections import defaultdict


class Graph:
    # default dictionary to store graph
    graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, parent, child):
        self.graph[parent].append(child)

    def is_friend_of_friend(self, vertex, visited, target):
        visited.add(vertex)
        for neighbour in self.graph[vertex]:
            if neighbour not in visited:
                self.is_friend_of_friend(neighbour, visited, target)
                if target in visited:
                    return True
        return False

    def DepthFirstSearch(self, start, target):
        # Create a set to store visited vertices
        visited = set()
        # Call the recursive helper function to print DepthFirstSearch traversal
        return self.is_friend_of_friend(start, visited, target)


def is_friend_of_friend(graph, start, target):
    is_friend = graph.DepthFirstSearch(start=start, target=target)
    is_friend = 'Yes' if is_friend else 'No'
    print(f'Is {start} a friend of {target}? {is_friend}')


if __name__ == "__main__":
    friendships = Graph()
    friendships.addEdge('A', 'C')
    friendships.addEdge('B', 'C')
    friendships.addEdge('C', 'A')
    friendships.addEdge('C', 'D')
    friendships.addEdge('D', 'D')

    is_friend_of_friend(graph=friendships, start='C', target='A')
    is_friend_of_friend(graph=friendships, start='C', target='B')
