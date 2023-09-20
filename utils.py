from queue import Queue, PriorityQueue
from collections import deque
from typing import Dict, Tuple, List
import random
import math 

from Obstacle_field import *


# List of all nodes that can be traveresed by a current_node -> left, right, up and down which is not an obstacle and inside the grid
def get_valid_neighbours(curr_node, grid):
    """
    input: current node, grid
    output: list of all the neighbours of the current node 
    """   
    grid_size = grid.shape[0]
    x, y = curr_node
    if grid[curr_node] == 0:
        return []
    neighbours = []
    #List of all neighbours irrespective of obstacle -> up,doown,left and right
    for neighbour in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if not (
            0 <= neighbour[0] <= grid_size - 1 and 0 <= neighbour[1] <= grid_size - 1):
            continue
        if grid[neighbour]==1:  # if not an obstacle
            neighbours.append((neighbour[0], neighbour[1]))
    return neighbours

#Creating an Adjacency list Represenattion for unweighted graph
def adjacency_list(grid):
    """
    input: grid
    output: dict (the adjacency lsit of each traversable point)
    """   
    adj_list = {}
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            adj_list[(i, j)] = get_valid_neighbours((i, j), grid)
    return adj_list       # Dict[Tuple[int, int], Tuple[int, int]]

#Creating an Adjacency list Represenattion for our weighted graph
def  get_valid_neighbours_with_wts(curr_node, grid):
    """
    input: curr_node, grid
    output: dict (the adjacency list of each traversable point with the distance as the cost)
    key: neighbour
    value: distance between the neighbour and the current node
    """
    x, y = curr_node
    neighbours = {}
    all_neighbours= [(x,y+1), (x,y-1), (x+1,y), (x-1,y),(x+1,y+1), (x-1,y-1), (x+1,y-1), (x-1,y+1)]
    for n in all_neighbours:
        if not(n[0] >= 0 and n[0] < grid.shape[0] and n[1] >= 0 and n[1] < grid.shape[1]):
            continue
        if grid[n[0], n[1]] != 0: # if not an obstacle
            neighbours[n] = math.dist(curr_node, n)
    return neighbours

#Adjacency list of our grid with dist as cost for every node
def adjacency_list_with_wts(grid):
    """
    input: grid
    output: dict (the adjacency list of each traversable point with the distance as the cost)
    """
    adj_list_wts = {}
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
                adj_list_wts[(i, j)] = get_valid_neighbours_with_wts((i, j), grid)
    return adj_list_wts


# to get the unvisited children of a particular node
def get_unvisited_children(graph, curr_node, visited):
    """
    input: graph, current node, visited 
        visited: (key: node, value: parent of the node)
    output: list of all the unvisited children of the current node
    """
    unvisited = []
    for child in graph.get(curr_node, []):
        if not visited[child]:
            unvisited.append(child)
    return unvisited

# (only if start and target pt has obstacle)
def choose_start_target(grid) :
    grid_size = grid.shape[0]
    print(grid_size)
    limit = int(10 * grid_size / 100)

    #start locations in the NorthWest
    feasible_start_location = []
    for i in range(limit):
        for j in range(limit):
            if grid[i,j]!=0: # if not an obstacle
                feasible_start_location.append((i,j))

    # target locations in the SouthEast
    feasible_target_location = []
    for i in range(grid_size - limit, grid_size):
        for j in range(grid_size - limit, grid_size):
            if grid[i,j]!=0: # if not an obstacle
                feasible_target_location.append((i,j))

    return random.choice(feasible_start_location), random.choice(feasible_target_location)