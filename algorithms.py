import math
import random
import numpy as np
from collections import deque
from queue import Queue
from typing import Dict, List, Tuple
from utils import *


class algo_planner():

    def __init__(self, start, target):
        self.start = start
        self.target = target

    def bfs(self,adj_list):
        q = Queue()
        path = []
        visited = dict.fromkeys(adj_list, False)
        parent = dict.fromkeys(adj_list,False) #parent (key: child, value: parent)

        #set start node as visited
        visited[self.start] = True
        q.put(self.start)

        #to keep track of the nodes we traverse
        while not q.empty():
            # print(len(q.queue))
            curr_node = q.get()
            path.append(curr_node)
            for child in adj_list[curr_node]: 
                if visited[child]== False:  #   if child is not visited
                    if child == self.target:  # If target reached, return
                        visited[child] = True
                        parent[child] = curr_node
                        # print(parent)
                        with q.mutex:
                            q.queue.clear()
                        break
                # If not visited, add to queue
                    visited[child] = True
                    parent[child] = curr_node
                    # print(parent)
                    q.put(child)

        final_path = []
        current = self.target
        while current != self.start:
            if current not in parent:
                print("No path exists")
                return len(path), []
            next = parent[current]  #parent (key: child, value: parent)
            final_path.append(next)
            current = next
        
        iterations = len(path)
        print("Iterations for BFS: ", len(path))
        return iterations, final_path
    

    def dfs(self, adj_list):
        stack = deque()
        path = []
        visited = dict.fromkeys(adj_list, False) # Mark all nodes as unvisited
        parent = dict.fromkeys(adj_list,False)  # To keep track of the parent of each node

        curr_node = self.start
        visited[curr_node] = True
        path.append(curr_node)
        stack.append(curr_node)

        while len(stack)!=0:
            children = get_unvisited_children(adj_list, curr_node, visited)
            if len(children)==0: # If no children, backtrack
                curr_node = stack.pop()

            for child in children:
                if visited[child]:
                    continue

                if child == self.target:  # If goal reached, terminate traversal
                    visited[child] = True # Mark as visited
                    parent[child] = curr_node
                    path.append(child)
                    stack.clear()
                    break

                visited[child] = True
                parent[child] = curr_node
                path.append(child)
                stack.append(curr_node)
                curr_node = child
                break

        final_path = []
        current = self.target
        # print(current)
        while current != self.start: # Backtrack to find the path
            if current not in parent:
                print("No path exists")
                return len(path), []
            parent_node = parent[current] # Find the parent of the current node
            final_path.append(parent_node)
            current = parent_node

        iterations = len(path)
        print("Iterations for DFS: ", len(final_path))
        return iterations, final_path
    

    def dijkstra(self, adj_list_wts):
        q = Queue()
        visited = dict.fromkeys(adj_list_wts, False)
        parent = dict.fromkeys(adj_list_wts,False)

        path = []
        visited[self.start] = True
        q.put(self.start)

        while not q.empty():
            curr_node = q.get()
            path.append(curr_node) 
            for child in adj_list_wts[curr_node]:
                if visited[child]==False:  # Ignore already visited node
                    if child == self.target:  # If goal reached, terminate traversal
                        visited[child] = True
                        parent[child] = curr_node
                        
                        with q.mutex:
                            q.queue.clear()
                        break

                    visited[child] = True
                    parent[child] = curr_node
                    q.put(child)
                    # print('working')

        final_path = []
        current = self.target
        while current != self.start:
            if current not in parent:
                print("No path exists")
                return len(path), []
            parent_node = parent[current]
            final_path.append(parent_node)
            current = parent_node

        iterations = len(path)
        print("Iterations for Djikstra: ", len(path))
        return iterations, final_path
    

    def random_planner(self, adj_list):
        path = []
        visited = dict.fromkeys(adj_list, False)
        parent = dict.fromkeys(adj_list,False)

        curr_node = self.start
        visited[curr_node] = True
        path.append(curr_node)

        count = 0
        while curr_node != self.target and count <=10000:
            count += 1
            children = get_unvisited_children(adj_list, curr_node, visited)
            if not children:  # If no children, backtrack
                if curr_node not in parent:
                    print("No path exists")
                    return count, []
                curr_node = parent[curr_node]
                path = path[:-1]
                continue

            child = random.choice(adj_list[curr_node]) # Choose a random child
            if visited[child]==False:
                visited[child] = True
                path.append(child)
                parent[child] = curr_node
                curr_node = child

        print("Iterations for Random plannar: ", len(path))
        return count, path
