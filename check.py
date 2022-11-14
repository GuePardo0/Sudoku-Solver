#this file is used to check if numbers in a grid are breaking Sudoku rules
from getPosition import gpb
def checksimple(pos, grid):
    #checks if a number is wrong in its row or collum
    #returns 0 if it's right and 1 if it's wrong
    a=0
    if grid[pos] != 0:
        if pos > 71:
            if grid[pos] == grid[pos-72]:
                a=1
        if pos > 62:
            if grid[pos] == grid[pos-63]:
                a=1
        if pos > 53:
            if grid[pos] == grid[pos-54]:
                a=1
        if pos > 44:
            if grid[pos] == grid[pos-45]:
                a=1
        if pos > 35:
            if grid[pos] == grid[pos-36]:
                a=1
        if pos > 26:
            if grid[pos] == grid[pos-27]:
                a=1
        if pos > 17:
            if grid[pos] == grid[pos-18]:
                a=1
        if pos > 8:
            if grid[pos] == grid[pos-9]:
                a=1
        if pos < 72:
            if grid[pos] == grid[pos+9]:
                a=1
        if pos < 63:
            if grid[pos] == grid[pos+18]:
                a=1
        if pos < 54:
            if grid[pos] == grid[pos+27]:
                a=1
        if pos < 45:
            if grid[pos] == grid[pos+36]:
                a=1
        if pos < 36:
            if grid[pos] == grid[pos+45]:
                a=1
        if pos < 27:
            if grid[pos] == grid[pos+54]:
                a=1
        if pos < 18:
            if grid[pos] == grid[pos+63]:
                a=1
        if pos < 9:
            if grid[pos] == grid[pos+72]:
                a=1
        b=pos
        while b > 8:
            b-=9
        if b > 0:
            if grid[pos] == grid[pos-1]:
                a=1
        if b > 1:
            if grid[pos] == grid[pos-2]:
                a=1
        if b > 2:
            if grid[pos] == grid[pos-3]:
                a=1
        if b > 3:
            if grid[pos] == grid[pos-4]:
                a=1
        if b > 4:
            if grid[pos] == grid[pos-5]:
                a=1
        if b > 5:
            if grid[pos] == grid[pos-6]:
                a=1
        if b > 6:
            if grid[pos] == grid[pos-7]:
                a=1
        if b > 7:
            if grid[pos] == grid[pos-8]:
                a=1
        if b < 8:
            if grid[pos] == grid[pos+1]:
                a=1
        if b < 7:
            if grid[pos] == grid[pos+2]:
                a=1
        if b < 6:
            if grid[pos] == grid[pos+3]:
                a=1
        if b < 5:
            if grid[pos] == grid[pos+4]:
                a=1
        if b < 4:
            if grid[pos] == grid[pos+5]:
                a=1
        if b < 3:
            if grid[pos] == grid[pos+6]:
                a=1
        if b < 2:
            if grid[pos] == grid[pos+7]:
                a=1
        if b < 1:
            if grid[pos] == grid[pos+8]:
                a=1
    return a
def check(grid, pos = ""):
    #main function
    #checks if a number is wrong in its row, collum or box
    #checks the whole grid if no pos argument is given
    #returns 0 if it's right and 1 if it's wrong
    mode=0
    a=0
    if pos == "":
        mode=1
        pos=0
    while pos != len(grid):
        if grid[pos] != 0:
            if pos > 71 and grid[pos] == grid[pos-72]:
                    a=1
            if pos > 62 and grid[pos] == grid[pos-63]:
                    a=1
            if pos > 53 and grid[pos] == grid[pos-54]:
                    a=1
            if pos > 44 and grid[pos] == grid[pos-45]:
                    a=1
            if pos > 35 and grid[pos] == grid[pos-36]:
                    a=1
            if pos > 26 and grid[pos] == grid[pos-27]:
                    a=1
            if pos > 17 and grid[pos] == grid[pos-18]:
                    a=1
            if pos > 8 and grid[pos] == grid[pos-9]:
                    a=1
            if pos < 72 and grid[pos] == grid[pos+9]:
                    a=1
            if pos < 63 and grid[pos] == grid[pos+18]:
                    a=1
            if pos < 54 and grid[pos] == grid[pos+27]:
                    a=1
            if pos < 45 and grid[pos] == grid[pos+36]:
                    a=1
            if pos < 36 and grid[pos] == grid[pos+45]:
                    a=1
            if pos < 27 and grid[pos] == grid[pos+54]:
                    a=1
            if pos < 18 and grid[pos] == grid[pos+63]:
                    a=1
            if pos < 9 and grid[pos] == grid[pos+72]:
                    a=1
            b=pos
            while b > 8:
                b-=9
            if b > 0 and grid[pos] == grid[pos-1]:
                    a=1
            if b > 1 and grid[pos] == grid[pos-2]:
                    a=1
            if b > 2 and grid[pos] == grid[pos-3]:
                    a=1
            if b > 3 and grid[pos] == grid[pos-4]:
                    a=1
            if b > 4 and grid[pos] == grid[pos-5]:
                    a=1
            if b > 5 and grid[pos] == grid[pos-6]:
                    a=1
            if b > 6 and grid[pos] == grid[pos-7]:
                    a=1
            if b > 7 and grid[pos] == grid[pos-8]:
                    a=1
            if b < 8 and grid[pos] == grid[pos+1]:
                    a=1
            if b < 7 and grid[pos] == grid[pos+2]:
                    a=1
            if b < 6 and grid[pos] == grid[pos+3]:
                    a=1
            if b < 5 and grid[pos] == grid[pos+4]:
                    a=1
            if b < 4 and grid[pos] == grid[pos+5]:
                    a=1
            if b < 3 and grid[pos] == grid[pos+6]:
                    a=1
            if b < 2 and grid[pos] == grid[pos+7]:
                    a=1
            if b < 1 and grid[pos] == grid[pos+8]:
                    a=1
            rand1=0
            while rand1 != 8:
                posbox=gpb(pos)
                rand=rand1
                if rand >= posbox:
                    rand+=1
                rand0=rand
                posbox0=posbox
                if posbox0 > 2:
                    posbox+=6
                if posbox0 > 5:
                    posbox+=6
                if rand0 > 2:
                    rand+=6
                if rand0 > 5:
                    rand+=6
                dist=posbox-rand
                if grid[pos] == grid[pos-dist]:
                    a=1
                rand1+=1
        pos+=1
        if mode == 0:
            break
    return a