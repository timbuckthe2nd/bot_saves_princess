#!/usr/bin/python


def displayPathtoPrincess(n, grid):
    # find mario
    for i, lst in enumerate(grid):
        for j, m in enumerate(lst):
            if m == "m":
                mario = [i, j]
# find peach
    for i, lst in enumerate(grid):
        for j, p in enumerate(lst):
            if p == "p":
                peach = [i, j]
# draw x path
    path_x = int(mario[1] - peach[1])
    if path_x > 0:
        movement_x = 'DOWN'
    elif path_x < 0:
        movement_x = 'UP'
    i_x = abs(path_x)
    for i in range(i_x):
        print(movement_x)
# draw y path
    path_y = int(mario[0] - peach[0])
    if path_y > 0:
        movement_y = 'RIGHT'
    elif path_y < 0:
        movement_y = 'LEFT'
    i_y = abs(path_y)
    for i in range(i_y):
        print(movement_y)


m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m, grid)
