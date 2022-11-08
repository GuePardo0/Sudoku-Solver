#this file creates functions that make row related Sudoku strategies
from SudokuAI.Converter import gridConvert
def NSNIR(pm):
    #deletes pencilmarks that are in the same row as a number
    #NSNIR = no same number in a row
    grid=gridConvert(pm)
    a=0
    while a != len(grid):
        b=a
        while b > 8:
            b-=9
        a1=0
        while a1 != 9:
            if b > 0 and pm[a*9+a1] == 1 and a1+1 == grid[a-1]:
                    pm[a*9+a1]=0
            if b > 1 and pm[a*9+a1] == 1 and a1+1 == grid[a-2]:
                    pm[a*9+a1]=0
            if b > 2 and pm[a*9+a1] == 1 and a1+1 == grid[a-3]:
                    pm[a*9+a1]=0
            if b > 3 and pm[a*9+a1] == 1 and a1+1 == grid[a-4]:
                    pm[a*9+a1]=0
            if b > 4 and pm[a*9+a1] == 1 and a1+1 == grid[a-5]:
                    pm[a*9+a1]=0
            if b > 5 and pm[a*9+a1] == 1 and a1+1 == grid[a-6]:
                    pm[a*9+a1]=0
            if b > 6 and pm[a*9+a1] == 1 and a1+1 == grid[a-7]:
                    pm[a*9+a1]=0
            if b > 7 and pm[a*9+a1] == 1 and a1+1 == grid[a-8]:
                    pm[a*9+a1]=0
            if b < 8 and pm[a*9+a1] == 1 and a1+1 == grid[a+1]:
                    pm[a*9+a1]=0
            if b < 7 and pm[a*9+a1] == 1 and a1+1 == grid[a+2]:
                    pm[a*9+a1]=0
            if b < 6 and pm[a*9+a1] == 1 and a1+1 == grid[a+3]:
                    pm[a*9+a1]=0
            if b < 5 and pm[a*9+a1] == 1 and a1+1 == grid[a+4]:
                    pm[a*9+a1]=0
            if b < 4 and pm[a*9+a1] == 1 and a1+1 == grid[a+5]:
                    pm[a*9+a1]=0
            if b < 3 and pm[a*9+a1] == 1 and a1+1 == grid[a+6]:
                    pm[a*9+a1]=0
            if b < 2 and pm[a*9+a1] == 1 and a1+1 == grid[a+7]:
                    pm[a*9+a1]=0
            if b < 1 and pm[a*9+a1] == 1 and a1+1 == grid[a+8]:
                    pm[a*9+a1]=0
            a1+=1
        a+=1
    return pm
def OCIR(pm):
    #places numbers that, in a row, can only be in one cell
    #OCIR = one cell in a row
    a=0
    while a != len(pm)/9:
        a1=0
        while a1 != 9:
            if pm[a*9+a1] == 1:
                b=a
                while b > 8:
                    b-=9
                c=1
                if b > 0 and pm[a*9+a1] == pm[a*9+a1-9]:
                        c=0
                if b > 1 and pm[a*9+a1] == pm[a*9+a1-18]:
                        c=0
                if b > 2 and pm[a*9+a1] == pm[a*9+a1-27]:
                        c=0
                if b > 3 and pm[a*9+a1] == pm[a*9+a1-36]:
                        c=0
                if b > 4 and pm[a*9+a1] == pm[a*9+a1-45]:
                        c=0
                if b > 5 and pm[a*9+a1] == pm[a*9+a1-54]:
                        c=0
                if b > 6 and pm[a*9+a1] == pm[a*9+a1-63]:
                        c=0
                if b > 7 and pm[a*9+a1] == pm[a*9+a1-72]:
                        c=0
                if b < 8 and pm[a*9+a1] == pm[a*9+a1+9]:
                        c=0
                if b < 7 and pm[a*9+a1] == pm[a*9+a1+18]:
                        c=0
                if b < 6 and pm[a*9+a1] == pm[a*9+a1+27]:
                        c=0
                if b < 5 and pm[a*9+a1] == pm[a*9+a1+36]:
                        c=0
                if b < 4 and pm[a*9+a1] == pm[a*9+a1+45]:
                        c=0
                if b < 3 and pm[a*9+a1] == pm[a*9+a1+54]:
                        c=0
                if b < 2 and pm[a*9+a1] == pm[a*9+a1+63]:
                        c=0
                if b < 1 and pm[a*9+a1] == pm[a*9+a1+72]:
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