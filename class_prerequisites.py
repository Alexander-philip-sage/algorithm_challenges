'''given a list of classes to take. 
some which are pre-requisites to others. Search through the graph of classes'''
from collections import defaultdict

NODE_DATA = [[(0,1),(0,2),(2,3),(1,3), (1,4),(3,4), (1,6),(0,5),(5,4)],
    [(0, 1),(0, 2),(1, 2),(2, 0),(2, 3),(3, 3)],
    [(0, 1),(0, 2),(1, 2),(2, 0),(3,2)],
    [(0,1),(0,3),(2,3)],
    [(0,1),(0,3),(2,1),(2,3)],
    ]
from typing import Tuple, List
class Graph():
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited= set()
        self.dfs_order = []
        self.traversed = set()
        self.bfs_order = []
        self.ct_prerequisites = defaultdict(int)
    def add_node(self, node: Tuple[int]):
        self.graph[node[0]].append(node[1])
        self.ct_prerequisites[node[1]]+=1
        self.ct_prerequisites[node[0]]
    def DFS_stack(self):
        stack = []
        self.dfs_s_order = []
        all_nodes = list(self.graph.keys())
        for node in all_nodes:
            if self.ct_prerequisites[node]==0:
                stack.append(node)
        while stack:
            node = stack.pop(-1)
            ##if there are following courses that are not already in the order
            following_courses_not_order = [x for x in self.graph[node] if x not in self.dfs_s_order]
            if len(following_courses_not_order)>0:
                stack.append(node)
                for following_course in following_courses_not_order:
                    if following_course in stack:
                        self.dfs_s_order = []
                        return
                    else:
                        stack.append(following_course)
            else:
                self.dfs_s_order.append(node)

        self.inverse_order(self.dfs_s_order)
    def DFS(self):
        all_nodes = list(self.graph.keys())
        for node in all_nodes:
            if self.ct_prerequisites[node]==0:
                self.DFS_rec(node)
        self.inverse_order(self.dfs_order)
    def DFS_rec(self, node: int):
        '''implemented with recursion'''
        for following_course in self.graph[node]:
            ##its possible for two classes to be the pre-requisite for the same class
            ##so we need to distinguish between edges we've traversed and nodes we've visited
            ##its ok for a node to appear twice, not for an edge to appear twice
            if (node,following_course) in self.traversed:
                return 0
            if following_course not in self.visited:
                self.traversed.add((node, following_course))
                res = self.DFS_rec(node=following_course)
                if not res:
                    return 0
        ##sets have faster lookup time than lists
        self.visited.add(node)
        self.dfs_order.append(node)
        return 1
    def inverse_order(self, order):
        for i in range(len(order)//2):
            tmp = order[-1-i]
            order[-1-i]=order[i]
            order[i]=tmp
    def BFS(self):
        '''implemented with queues'''
        all_nodes = list(self.graph.keys())
        ct_prerequisites = self.ct_prerequisites.copy()
        queue = []
        for node in all_nodes:
            if ct_prerequisites[node]==0:
                queue.append(node)
        self.bfs_order
        while queue:
            node = queue.pop(0)
            for following_course in self.graph[node]:
                ct_prerequisites[following_course]-=1
                if ct_prerequisites[following_course]==0:
                    queue.append(following_course)
            self.bfs_order.append(node)
        ##if couldn't get all the nodes, then its an invalid sequence
        if len(self.bfs_order)< len(all_nodes):
            self.bfs_order = []
    def BFS_rec(self, node:int=0):
        if node in self.bfs_order:
            self.bfs_order=[]
            return 0
        self.bfs_order.append(node)
        for following_course in self.graph[node]:
            pass

    def check_correct(self, order: List[int]):
        node_order = {order[i]:i for i in range(len(order)) }
        for node in order:
            for following_course in self.graph[node]:
                if node_order[node] > node_order[following_course]:
                    return False
        return True 

def test_func(mode:str):
    passed = True
    for test in NODE_DATA:
        graph = Graph()
        for node in test:
            graph.add_node(node)
        if mode=='dfs_recursive':
            graph.DFS()
            order = graph.dfs_order
        elif mode=='dfs_stack':
            graph.DFS_stack()
            order = graph.dfs_s_order
        elif mode=='bfs':
            graph.BFS()
            order = graph.bfs_order
        if not graph.check_correct(order):
            passed = False
            print("\ntest")
            print(test)
            print("order of classes ", mode,order)
            print("prerequisite count", graph.ct_prerequisites)
    if passed:
        print(mode, "passed all tests")

def dfs(graph, vertex, path, order, visited):
    path.add(vertex)
    for neighbor in graph[vertex]:
        if neighbor in path:
            return False
        if neighbor not in visited:
            visited.add(neighbor)
            if not dfs(graph, neighbor, path, order, visited):
                return False
    path.remove(vertex)
    order.append(vertex)
    return True
def course_schedule(n, prerequisites):
    graph = [[] for i in range(n)]
    for pre in prerequisites:
        graph[pre[1]].append(pre[0])
    visited = set()
    path = set()
    order = []
    for course in range(n):
        if course not in visited:
            visited.add(course)
            if not dfs(graph, course, path, order, visited):
                return False
if __name__=='__main__':
    
    test_func( 'bfs')
    test_func( 'dfs_recursive')
    test_func('dfs_stack')


        