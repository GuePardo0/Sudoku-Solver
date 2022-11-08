#this file creates functions that make row related Sudoku strategies
from SudokuAI.Converter import gridConvert
from gpb import gpb
def NSNIB(pm):
    #deletes pencilmarks that are in the same box as a number
    #NSNIB = no same number in a box
    grid=gridConvert(pm)
    a=0
    while a != len(grid):
        b=gpb(a)
        b0=b
        if b0 > 2:
            b+=6
        if b0 > 5:
            b+=6
        a1=0
        while a1 != 9:
            if b > 0 and pm[a*9+a1] == 1 and a1+1 == grid[a-b]:
                    pm[a*9+a1]=0
            if b > 1 and pm[a*9+a1] == 1 and a1+1 == grid[a-b+1]:
                    pm[a*9+a1]=0
            if b > 2 and pm[a*9+a1] == 1 and a1+1 == grid[a-b+2]:
                    pm[a*9+a1]=0
            if b > 9 and pm[a*9+a1] == 1 and a1+1 == grid[a-b+9]:
                    pm[a*9+a1]=0
            if b > 10 and pm[a*9+a1] == 1 and a1+1 == grid[a-b+10]:
                    pm[a*9+a1]=0
            if b > 11 and pm[a*9+a1] == 1 and a1+1 == grid[a-b+11]:
                    pm[a*9+a1]=0
            if b > 18 and pm[a*9+a1] == 1 and a1+1 == grid[a-b+18]:
                    pm[a*9+a1]=0
            if b > 19 and pm[a*9+a1] == 1 and a1+1 == grid[a-b+19]:
                    pm[a*9+a1]=0
            if b < 20 and pm[a*9+a1] == 1 and a1+1 == grid[a-b+20]:
                    pm[a*9+a1]=0
            if b < 19 and pm[a*9+a1] == 1 and a1+1 == grid[a-b+19]:
                    pm[a*9+a1]=0
            if b < 18 and pm[a*9+a1] == 1 and a1+1 == grid[a-b+18]:
                    pm[a*9+a1]=0
            if b < 11 and pm[a*9+a1] == 1 and a1+1 == grid[a-b+11]:
                    pm[a*9+a1]=0
            if b < 10 and pm[a*9+a1] == 1 and a1+1 == grid[a-b+10]:
                    pm[a*9+a1]=0
            if b < 9 and pm[a*9+a1] == 1 and a1+1 == grid[a-b+9]:
                    pm[a*9+a1]=0
            if b < 2 and pm[a*9+a1] == 1 and a1+1 == grid[a-b+2]:
                    pm[a*9+a1]=0
            if b < 1 and pm[a*9+a1] == 1 and a1+1 == grid[a-b+1]:
                    pm[a*9+a1]=0
            a1+=1
        a+=1
    return pm
def OCIB(pm):
    #places numbers that, in a box, can only be in one cell
    #OCIB = one cell in a box
    a=0
    while a != len(pm)/9:
        b=gpb(a)
        b0=b
        if b0 > 2:
            b+=6
        if b0 > 5:
            b+=6
        a1=0
        while a1 != 9:
            if pm[a*9+a1] == 1:
                c=1
                if b > 0 and pm[a*9+a1] == pm[a*9+a1-b*9]:
                        c=0
                if a > 1 and pm[a*9+a1] == pm[a*9+a1+(-b+1)*9]:
                        c=0
                if a > 2 and pm[a*9+a1] == pm[a*9+a1+(-b+2)*9]:
                        c=0
                if a > 9 and pm[a*9+a1] == pm[a*9+a1+(-b+9)*9]:
                        c=0
                if a > 10 and pm[a*9+a1] == pm[a*9+a1+(-b+10)*9]:
                        c=0
                if a > 11 and pm[a*9+a1] == pm[a*9+a1+(-b+11)*9]:
                        c=0
                if a > 18 and pm[a*9+a1] == pm[a*9+a1+(-b+18)*9]:
                        c=0
                if a > 19 and pm[a*9+a1] == pm[a*9+a1+(-b+19)*9]:
                        c=0
                if a < 20 and pm[a*9+a1] == pm[a*9+a1+(-b+20)*9]:
                        c=0
                if a < 19 and pm[a*9+a1] == pm[a*9+a1+(-b+19)*9]:
                        c=0
                if a < 18 and pm[a*9+a1] == pm[a*9+a1+(-b+18)*9]:
                        c=0
                if a < 11 and pm[a*9+a1] == pm[a*9+a1+(-b+11)*9]:
                        c=0
                if a < 10 and pm[a*9+a1] == pm[a*9+a1+(-b+10)*9]:
                        c=0
                if a < 9 and pm[a*9+a1] == pm[a*9+a1+(-b+9)*9]:
                        c=0
                if a < 2 and pm[a*9+a1] == pm[a*9+a1+(-b+2)*9]:
                        c=0
                if a < 1 and pm[a*9+a1] == pm[a*9+a1+(-b+1)*9]:
                        c=0
                if c == 1:
                    a2=0
                    while a2 != 9:
                        if a2 != a1:
                            pm[a*9+a2]=0
                        a2+=1
            a1+=1
        a+=1
    return pm