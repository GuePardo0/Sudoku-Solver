#this file is used to create a random game of sudoku (WIP)
#for now, it only makes a random full grid
from check import checksimple
from getPosition import gpb
import random
def swap(a, b, grid):
    #swaps two digits in a grid
    ba=grid[a]
    grid[a]=grid[b]
    grid[b]=ba
    return grid
def rgg():
    #main function
    #generates a random full grid
    #rgg = random grid generator
    grid=[1, 2, 3, 1, 2, 3, 1, 2, 3, 4, 5, 6, 4, 5, 6, 4, 5, 6, 7, 8, 9, 7, 8, 9, 7, 8, 9, 1, 2, 3, 1, 2, 3, 1, 2, 3, 4, 5, 6, 4, 5, 6, 4, 5, 6, 7, 8, 9, 7, 8, 9, 7, 8, 9, 1, 2, 3, 1, 2, 3, 1, 2, 3, 4, 5, 6, 4, 5, 6, 4, 5, 6, 7, 8, 9, 7, 8, 9, 7, 8, 9]
    while 1:
        order=["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
        a=0
        while a != len(order):
            while 1:
                rand=random.randint(0, 80)
                b=0
                c=0
                while b != len(order):
                    if rand == order[b]:
                        c=1
                        break
                    b+=1
                if c != 1:
                    break
            order[a]=rand
            a+=1
        a=0
        while a != len(grid):
            if checksimple(order[a], grid) == 1:
                rand=random.randint(1, 8)
                posbox=gpb(order[a])
                if rand >= posbox:
                    rand+=1
                posbox0=posbox
                rand0=rand
                if posbox0 > 3:
                    posbox+=6
                if posbox0 > 6:
                    posbox+=6
                if rand0 > 3:
                    rand+=6
                if rand0 > 6:
                    rand+=6
                dist=posbox-rand
                grid=swap(order[a], order[a]-dist, grid)
                if checksimple(order[a]-dist, grid) == 1:
                    grid=swap(order[a], order[a]-dist, grid)
                    a-=1
            a+=1
        t=0
        while t != len(grid):
            error=checksimple(t, grid)
            if error == 1:
                break
            t+=1
        if error == 0:
            break
    return grid