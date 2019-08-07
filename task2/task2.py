#!/usr/bin/env python3.7

import sys
from matplotlib.path import Path

def is_point_inside(x, y, figure_coords):
    fx1 = figure_coords[0][0]
    fy1 = figure_coords[0][1]
    fx2 = figure_coords[1][0]
    fy2 = figure_coords[1][1]
    fx3 = figure_coords[2][0]
    fy3 = figure_coords[2][1]
    fx4 = figure_coords[3][0]
    fy4 = figure_coords[3][1]          
    
    # segment (x-x1)/(x2-x1)=(y-y1)/(y2-y1)


    if (x == fx1 and y == fy1) or (x == fx2 and y == fy2) or (x == fx3 and y == fy3) or \
        (x == fx4 and y == fy4):
        return 0
    elif (x - fx1)*(fy2 - fy1) == (y - fy1)*(fx2 - fx1) or \
        (x - fx2)*(fy3 - fy2) == (y - fy2)*(fx3 - fx2) or \
        (x - fx3)*(fy4 - fy3) == (y - fy3)*(fx4 - fx3) or \
        (x - fx4)*(fy1 - fy4) == (y - fy4)*(fx1 - fx4):
        return 1
    elif Path(figure_coords).contains_point([x,y]):
        return 2
    else:
        return 3



if __name__ == "__main__":

    quadrangle_coords = []

    with open(sys.argv[1], "r") as input_file:
        for line in input_file:
            quadrangle_coords.append([float(i) for i in line.split()])
        

    points_coords = []

    with open(sys.argv[2], "r") as input_file:
        for line in input_file:
            points_coords.append([float(i) for i in line.split()])

    for x, y in points_coords:
        print(is_point_inside(x, y, quadrangle_coords))
