#this file creates functions that make basic Sudoku strategies
from SudokuAI.Converter import gridConvert
from getPosition import gpr
from getPosition import gpc
from getPosition import gpb
def NSNIR(pm):
    #deletes pencilmarks that are in the same row as a number
    #NSNIR = no same number in a row
    grid=gridConvert(pm)
    a=0
    while a != len(grid):
        b=gpr(a)
        if grid[a] != 0:
            a1=0
            if a1 == b:
                a1+=1
            while a1 < 9:
                if grid[a-b+a1] == 0:
                    pm[a*9-b*9+a1*9+grid[a]-1]=0
                if a1+1 == b:
                    a1+=1
                a1+=1
        a+=1
    return pm
def NSNIC(pm):
    #deletes pencilmarks that are in the same column as a number
    #NSNIC = no same number in a column
    grid=gridConvert(pm)
    a=0
    while a != len(grid):
        b=gpc(a)
        if grid[a] != 0:
            a1=0
            if a1 == b:
                a1+=1
            while a1 < 9:
                if grid[a-b*9+a1*9] == 0:
                    pm[a*9-b*81+a1*81+grid[a]-1]=0
                if a1+1 == b:
                    a1+=1
                a1+=1
        a+=1
    return pm
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
        if grid[a] != 0:
            a1=0
            if a1 == b:
                a1+=1
            while a1 < 9:
                a10=a1
                if a1 > 2:
                    a10+=6
                if a1 > 5:
                    a10+=6
                if grid[a-b+a10] == 0:
                    pm[a*9-b*9+a10*9+grid[a]-1]=0
                a10+=1
                if a10 == 3:
                    a10+=6
                elif a10 == 12:
                    a10+=6
                if a10 == b:
                    a1+=1
                a1+=1
        a+=1
    return pm
def OCIR(pm):
    #places numbers that, in a row, can only be in one cell
    #OCIR = one cell in a row
    grid=gridConvert(pm)
    a=0
    while a != len(pm)/9:
        if grid[a] == 0:
            b=gpr(a)
            a1=0
            while a1 != 9:
                if pm[a*9+a1] == 1:
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
def OCIC(pm):
    #places numbers that, in a column, can only be in one cell
    #OCIC = one cell in a column
    grid=gridConvert(pm)
    a=0
    while a != len(pm)/9:
        if grid[a] == 0:
            b=gpc(a)
            a1=0
            while a1 != 9:
                if pm[a*9+a1] == 1:
                    c=1
                    if b > 0 and pm[a*9+a1] == pm[a*9+a1-81]:
                        c=0
                    if b > 1 and pm[a*9+a1] == pm[a*9+a1-162]:
                        c=0
                    if b > 2 and pm[a*9+a1] == pm[a*9+a1-243]:
                        c=0
                    if b > 3 and pm[a*9+a1] == pm[a*9+a1-324]:
                        c=0
                    if b > 4 and pm[a*9+a1] == pm[a*9+a1-405]:
                        c=0
                    if b > 5 and pm[a*9+a1] == pm[a*9+a1-486]:
                        c=0
                    if b > 6 and pm[a*9+a1] == pm[a*9+a1-567]:
                        c=0
                    if b > 7 and pm[a*9+a1] == pm[a*9+a1-648]:
                        c=0
                    if b < 8 and pm[a*9+a1] == pm[a*9+a1+81]:
                        c=0
                    if b < 7 and pm[a*9+a1] == pm[a*9+a1+162]:
                        c=0
                    if b < 6 and pm[a*9+a1] == pm[a*9+a1+243]:
                        c=0
                    if b < 5 and pm[a*9+a1] == pm[a*9+a1+324]:
                        c=0
                    if b < 4 and pm[a*9+a1] == pm[a*9+a1+405]:
                        c=0
                    if b < 3 and pm[a*9+a1] == pm[a*9+a1+486]:
                        c=0
                    if b < 2 and pm[a*9+a1] == pm[a*9+a1+567]:
                        c=0
                    if b < 1 and pm[a*9+a1] == pm[a*9+a1+648]:
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
def OCIB(pm):
    #places numbers that, in a box, can only be in one cell
    #OCIB = one cell in a box
    grid=gridConvert(pm)
    a=0
    while a != len(pm)/9:
        if grid[a] == 0:
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
                    if b > 1 and pm[a*9+a1] == pm[a*9+a1+(-b+1)*9]:
                        c=0
                    if b > 2 and pm[a*9+a1] == pm[a*9+a1+(-b+2)*9]:
                        c=0
                    if b > 9 and pm[a*9+a1] == pm[a*9+a1+(-b+9)*9]:
                        c=0
                    if b > 10 and pm[a*9+a1] == pm[a*9+a1+(-b+10)*9]:
                        c=0
                    if b > 11 and pm[a*9+a1] == pm[a*9+a1+(-b+11)*9]:
                        c=0
                    if b > 18 and pm[a*9+a1] == pm[a*9+a1+(-b+18)*9]:
                        c=0
                    if b > 19 and pm[a*9+a1] == pm[a*9+a1+(-b+19)*9]:
                        c=0
                    if b < 20 and pm[a*9+a1] == pm[a*9+a1+(-b+20)*9]:
                        c=0
                    if b < 19 and pm[a*9+a1] == pm[a*9+a1+(-b+19)*9]:
                        c=0
                    if b < 18 and pm[a*9+a1] == pm[a*9+a1+(-b+18)*9]:
                        c=0
                    if b < 11 and pm[a*9+a1] == pm[a*9+a1+(-b+11)*9]:
                        c=0
                    if b < 10 and pm[a*9+a1] == pm[a*9+a1+(-b+10)*9]:
                        c=0
                    if b < 9 and pm[a*9+a1] == pm[a*9+a1+(-b+9)*9]:
                        c=0
                    if b < 2 and pm[a*9+a1] == pm[a*9+a1+(-b+2)*9]:
                        c=0
                    if b < 1 and pm[a*9+a1] == pm[a*9+a1+(-b+1)*9]:
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