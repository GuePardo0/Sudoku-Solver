#this file is used to create a random game of sudoku
from check import checksimple
from getPosition import gpb
from SudokuAI.FullAI import FullAI
from fgd import fgd
from display import display
import random
def swap(a, b, grid):
    #swaps two digits in a grid
    ba=grid[a]
    grid[a]=grid[b]
    grid[b]=ba
    return grid
def rfgg():
    #generates a random full grid
    #rfgg = Random Full Grid Generator
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
                rand=random.randint(0, 7)
                posbox=gpb(order[a])
                if rand >= posbox:
                    rand+=1
                posbox0=posbox
                rand0=rand
                if posbox0 > 2:
                    posbox+=6
                if posbox0 > 5:
                    posbox+=6
                if rand0 > 2:
                    rand+=6
                if rand0 > 5:
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
def rgg(dif):
    #main function
    #generates a random grid
    #rgg = Random Grid Generator
    while 1:
        grid=rfgg()
        if dif == "1":
            alignedPm=False
            pairs=False
            dif=1
        elif dif == "2":
            alignedPm=True
            pairs=False
            dif=2
        elif dif == "3":
            alignedPm=True
            pairs=True
            dif=3
        er=0
        while 1:
            grid1=list(grid)
            rand=random.randint(0, 80)
            grid1=list(grid)
            rand=random.randint(0, 80)
            grid1=list(grid)
            if grid1[rand] != 0:
                grid1[rand]=0
                if fgd(FullAI(grid1, alignedPm, pairs)) == 0:
                    alignedPm=True
                    pairs=True
                    if fgd(FullAI(grid1, alignedPm, pairs)) == 1:
                        grid=list(grid1)
                        er=1
                    dif="1"
                    break
                else:
                    grid=list(grid1)
                    er=0
        if er == 1:
            break
    return grid
grid=rgg("1")
display(grid)
print(grid)
display(FullAI(grid, False, False))
display(FullAI(grid, True, False))
display(FullAI(grid, True, True))