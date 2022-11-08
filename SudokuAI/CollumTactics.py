#this file creates functions that make column related Sudoku strategies
from SudokuAI.Converter import gridConvert
def NSNIC(pm):
    #deletes pencilmarks that are in the same column as a number
    #NSNIC = no same number in a column
    grid=gridConvert(pm)
    a=0
    while a != len(grid):
        a1=0
        while a1 != 9:
            if a > 71 and pm[a*9+a1] == 1 and a1+1 == grid[a-72]:
                    pm[a*9+a1]=0
            if a > 62 and pm[a*9+a1] == 1 and a1+1 == grid[a-63]:
                    pm[a*9+a1]=0
            if a > 53 and pm[a*9+a1] == 1 and a1+1 == grid[a-54]:
                    pm[a*9+a1]=0
            if a > 44 and pm[a*9+a1] == 1 and a1+1 == grid[a-45]:
                    pm[a*9+a1]=0
            if a > 35 and pm[a*9+a1] == 1 and a1+1 == grid[a-36]:
                    pm[a*9+a1]=0
            if a > 26 and pm[a*9+a1] == 1 and a1+1 == grid[a-27]:
                    pm[a*9+a1]=0
            if a > 17 and pm[a*9+a1] == 1 and a1+1 == grid[a-18]:
                    pm[a*9+a1]=0
            if a > 8 and pm[a*9+a1] == 1 and a1+1 == grid[a-9]:
                    pm[a*9+a1]=0
            if a < 72 and pm[a*9+a1] == 1 and a1+1 == grid[a+9]:
                    pm[a*9+a1]=0
            if a < 63 and pm[a*9+a1] == 1 and a1+1 == grid[a+18]:
                    pm[a*9+a1]=0
            if a < 54 and pm[a*9+a1] == 1 and a1+1 == grid[a+27]:
                    pm[a*9+a1]=0
            if a < 45 and pm[a*9+a1] == 1 and a1+1 == grid[a+36]:
                    pm[a*9+a1]=0
            if a < 36 and pm[a*9+a1] == 1 and a1+1 == grid[a+45]:
                    pm[a*9+a1]=0
            if a < 27 and pm[a*9+a1] == 1 and a1+1 == grid[a+54]:
                    pm[a*9+a1]=0
            if a < 18 and pm[a*9+a1] == 1 and a1+1 == grid[a+63]:
                    pm[a*9+a1]=0
            if a < 9 and pm[a*9+a1] == 1 and a1+1 == grid[a+72]:
                    pm[a*9+a1]=0
            a1+=1
        a+=1
    return pm
def OCIC(pm):
    #places numbers that, in a column, can only be in one cell
    #OCIC = one cell in a column
    a=0
    while a != len(pm)/9:
        a1=0
        while a1 != 9:
            if pm[a*9+a1] == 1:
                c=1
                if a > 8 and pm[a*9+a1] == pm[a*9+a1-81]:
                        c=0
                if a > 17 and pm[a*9+a1] == pm[a*9+a1-162]:
                        c=0
                if a > 26 and pm[a*9+a1] == pm[a*9+a1-243]:
                        c=0
                if a > 35 and pm[a*9+a1] == pm[a*9+a1-324]:
                        c=0
                if a > 44 and pm[a*9+a1] == pm[a*9+a1-405]:
                        c=0
                if a > 53 and pm[a*9+a1] == pm[a*9+a1-486]:
                        c=0
                if a > 62 and pm[a*9+a1] == pm[a*9+a1-567]:
                        c=0
                if a > 71 and pm[a*9+a1] == pm[a*9+a1-648]:
                        c=0
                if a < 72:
                    if pm[a*9+a1] == pm[a*9+a1+81]:
                        c=0
                if a < 63:
                    if pm[a*9+a1] == pm[a*9+a1+162]:
                        c=0
                if a < 54:
                    if pm[a*9+a1] == pm[a*9+a1+243]:
                        c=0
                if a < 45:
                    if pm[a*9+a1] == pm[a*9+a1+324]:
                        c=0
                if a < 36:
                    if pm[a*9+a1] == pm[a*9+a1+405]:
                        c=0
                if a < 27:
                    if pm[a*9+a1] == pm[a*9+a1+486]:
                        c=0
                if a < 18:
                    if pm[a*9+a1] == pm[a*9+a1+567]:
                        c=0
                if a < 9:
                    if pm[a*9+a1] == pm[a*9+a1+648]:
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