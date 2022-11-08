#this file is used to detect if a grid is full
def fgd(grid):
    #main functions
    #detects if a grid is full
    #fgd = full Grid Detector
    full=1
    a=0
    while a != len(grid):
        if grid[a] == 0:
            full=0
        a+=1
    return full
grid=[1, 5, 2, 7, 6, 3, 1, 8, 9, 9, 3, 8, 1, 2, 5, 7, 6, 4, 6, 1, 7, 4, 9, 8, 3, 2, 5, 5, 2, 9, 6, 3, 7, 8, 4, 1, 7, 6, 3, 8, 4, 1, 9, 5, 2, 8, 4, 1, 2, 5, 9, 6, 7, 3, 1, 9, 6, 5, 7, 2, 4, 3, 8, 2, 8, 4, 3, 1, 6, 5, 9, 7, 3, 7, 5, 9, 8, 4, 2, 1, 6]