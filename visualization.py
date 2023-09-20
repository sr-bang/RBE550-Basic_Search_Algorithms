import matplotlib.pyplot as plt
import argparse
import os
from algorithms import *
from Obstacle_field import *
from utils import *




def main(coverage_percent):

    
    Parser = argparse.ArgumentParser()
    Parser.add_argument('--grid_size', type=int, default=128)
    # Parser.add_argument('--coverage_percent', type=int, default=60)

    Args = Parser.parse_args()
    grid_size = Args.grid_size
    # coverage_percent = Args.coverage_percent

    grid = create_obstacle_field(coverage_percent, grid_size)

    plt.figure()
    plt.imshow(grid,cmap='gray')

    ran_start,ran_target = choose_start_target(grid)
        
    start = (0,0)
    # if start is obstacle then choose random start
    if grid[start]!=1: 
        start = ran_start

    target = (grid_size-1, grid_size-1)
    if grid[target]!=1:
        target = ran_target

    print(start, target)
    
    adj_list = adjacency_list(grid)

    adj_list_wts = adjacency_list_with_wts(grid)

    planner = algo_planner(start, target)
    
    iterations_bfs, final_path_bfs = planner.bfs(adj_list)
    iterations_dfs, final_path_dfs = planner.dfs(adj_list)
    iterations_random, final_path_random = planner.random_planner(adj_list)
    iterations_dijkstra, final_path_dijkstra = planner.dijkstra(adj_list_wts) 


    def plot_path(final_path):
        final_1 = []
        final_2 = []

        for node in final_path:
            final_1.append(node[0])
            final_2.append(node[1])
        return final_1, final_2

    if len(final_path_bfs)==0:
        print("No path found by BFS")
    else: 
        final_1_bfs, final_2_bfs = plot_path(final_path_bfs)
        plt.plot(final_2_bfs, final_1_bfs, label="BFS", color="green")

    if len(final_path_dfs)==0:
        print("No path found by DFS")
    else:    
        final_1_dfs, final_2_dfs = plot_path(final_path_dfs)
        plt.plot(final_2_dfs, final_1_dfs, label="DFS", color="blue")
    
    if len(final_path_dijkstra)==0:
        print("No path found by Djikstra")
    else:    
        final_1_dijkstra, final_2_dijkstra = plot_path(final_path_dijkstra)
        plt.plot(final_2_dijkstra, final_1_dijkstra, label="Djikstra", color="red")
    
    if len(final_path_random)==0:
        print("No path found by Random")
    else:    
        final_1_random, final_2_random = plot_path(final_path_random)
        plt.plot(final_2_random, final_1_random, label="Random", color="yellow")
 
    plt.title(f"Coverage=%d percent" % coverage_percent)
    plt.legend(loc = "upper right")

    if not os.path.exists('results'):
        os.makedirs('results')
    
    #save fig in results folder
    plt.savefig(f'results/Coverage_{coverage_percent}.png')
    plt.close()

    return  iterations_bfs, iterations_dfs, iterations_random, iterations_dijkstra


if __name__=="__main__":
    bfs = []
    dfs = []
    random_p = []
    dijkstra = []
    coverage =[]

    for i in range(0,76,10):
        iterations_bfs, iterations_dfs, iterations_random, iterations_dijkstra = main(coverage_percent=i)
        bfs.append(iterations_bfs)
        dfs.append(iterations_dfs)
        random_p.append(iterations_random)
        dijkstra.append(iterations_dijkstra)
        coverage.append(i)


    print(bfs)
    print(dfs)
    print(random_p)
    print(dijkstra)
    print(coverage)
    
    # Plot the graph of no. of iterations vs coverage
    plt.figure()
    plt.plot(coverage, bfs, label="BFS", color="green")
    plt.plot(coverage, dfs, label="DFS", color="blue")
    plt.plot(coverage, random_p, label="Random", color="yellow")
    plt.plot(coverage, dijkstra, label="Djikstra", color="red")
    plt.title("No. of iterations vs Coverage")
    plt.xlabel("Coverage")
    plt.ylabel("No. of iterations")
    plt.legend(loc = "upper right")
    plt.savefig(f'results/Performance.png')

    plt.close()


