import numpy as np 
import matplotlib.pyplot as plt
import random


def create_obstacle_field(percent_coverage, grid_size):
    # Coordinates of the tetrominoes
    tetrominoes= np.asarray([[(0,0),(1,0),(2,0),(3,0)],
                            [(0,0),(0,1),(1,1),(2,1)],
                            [(0,0),(1,0),(1,1),(2,1)],
                            [(1,0),(0,1),(1,1),(2,1)]])
    
    grid = np.ones((grid_size,grid_size),dtype=int)
    # Take user input for percent coverage

    desired_cells = grid_size * grid_size * (percent_coverage/100)
    print("Desired number of filled cells = ", desired_cells) #1638.4

    # Now fill the grid with tetrominoes
    currently_filled= 0
    while(currently_filled < desired_cells):
        xcor = random.randint(0,grid_size-4)
        ycor = random.randint(0,grid_size-2)
        random_idx= np.random.randint(0, 4)
        selected_tetromino = tetrominoes[random_idx]
        collision = False

    # Now check for collision
    # If there is a collision, then break out of the loop
        for xy in selected_tetromino :
            if(grid[xcor,ycor + xy[1]] == 0 or grid[xcor + xy[0],ycor] == 0):
                collision = True
            break
        else:
            pass
            
    # place the tetromino in the grid
        if collision == False:
            for xy in selected_tetromino :
                grid[xcor+xy[0], ycor + xy[1]] = 0
            currently_filled +=4
        plt.imshow(grid, cmap='gray')
    return grid

