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
def RANB(pm):
    #if the only possible numbers in a box align in a row, clears all numbers in that row
    #RANB = Row Aligned Numbers in Box
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
                alone=1
                if pm[a*9+a1-b*9] == 1:
                    alone=0
                    if b != 0 and b != 1 and b != 2:
                        c=0
                if pm[a*9+a1+(-b+1)*9] == 1:
                    alone=0
                    if b != 0 and b != 1 and b != 2:
                        c=0
                if pm[a*9+a1+(-b+2)*9] == 1:
                    alone=0
                    if b != 0 and b != 1 and b != 2:
                        c=0
                if pm[a*9+a1+(-b+9)*9] == 1:
                    alone=0
                    if b != 9 and b != 10 and b != 11:
                        c=0
                if pm[a*9+a1+(-b+10)*9] == 1:
                    alone=0
                    if b != 9 and b != 10 and b != 11:
                        c=0
                if pm[a*9+a1+(-b+11)*9] == 1:
                    alone=0
                    if b != 9 and b != 10 and b != 11:
                        c=0
                if pm[a*9+a1+(-b+18)*9] == 1:
                    alone=0
                    if b != 18 and b != 19 and b != 20:
                        c=0
                if pm[a*9+a1+(-b+19)*9] == 1:
                    alone=0
                    if b != 18 and b != 19 and b != 20:
                        c=0
                if pm[a*9+a1+(-b+20)*9] == 1:
                    alone=0
                    if b != 18 and b != 19 and b != 20:
                        c=0
                if c == 1 and alone == 0:
                    b1=a
                    while b1 > 8:
                        b1-=9
                    if b1 == 0 or b1 == 1 or b1 == 2:
                        pm[a*9+a1+(3-b1)*9]=0
                        pm[a*9+a1+(4-b1)*9]=0
                        pm[a*9+a1+(5-b1)*9]=0
                        pm[a*9+a1+(6-b1)*9]=0
                        pm[a*9+a1+(7-b1)*9]=0
                        pm[a*9+a1+(8-b1)*9]=0
                    if b1 == 3 or b1 == 4 or b1 == 5:
                        pm[a*9+a1-b1*9]=0
                        pm[a*9+a1+(1-b1)*9]=0
                        pm[a*9+a1+(2-b1)*9]=0
                        pm[a*9+a1+(6-b1)*9]=0
                        pm[a*9+a1+(7-b1)*9]=0
                        pm[a*9+a1+(8-b1)*9]=0
                    if b1 == 6 or b1 == 7 or b1 == 8:
                        pm[a*9+a1-b1*9]=0
                        pm[a*9+a1+(1-b1)*9]=0
                        pm[a*9+a1+(2-b1)*9]=0
                        pm[a*9+a1+(3-b1)*9]=0
                        pm[a*9+a1+(4-b1)*9]=0
                        pm[a*9+a1+(5-b1)*9]=0
            a1+=1
        a+=1
    return pm
def CANB(pm):
    #if the only possible numbers in a box align in a column, clears all numbers in that column
    #CANB = Column Aligned Numbers in Box
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
                alone=1
                if pm[a*9+a1-b*9] == 1:
                    alone=0
                    if b != 0 and b != 9 and b != 18:
                        c=0
                if pm[a*9+a1+(-b+9)*9] == 1:
                    alone=0
                    if b != 0 and b != 9 and b != 18:
                        c=0
                if pm[a*9+a1+(-b+18)*9] == 1:
                    alone=0
                    if b != 0 and b != 9 and b != 18:
                        c=0
                if pm[a*9+a1+(-b+1)*9] == 1:
                    alone=0
                    if b != 1 and b != 10 and b != 19:
                        c=0
                if pm[a*9+a1+(-b+10)*9] == 1:
                    alone=0
                    if b != 1 and b != 10 and b != 19:
                        c=0
                if pm[a*9+a1+(-b+19)*9] == 1:
                    alone=0
                    if b != 1 and b != 10 and b != 19:
                        c=0
                if pm[a*9+a1+(-b+2)*9] == 1:
                    alone=0
                    if b != 2 and b != 11 and b != 20:
                        c=0
                if pm[a*9+a1+(-b+11)*9] == 1:
                    alone=0
                    if b != 2 and b != 11 and b != 20:
                        c=0
                if pm[a*9+a1+(-b+20)*9] == 1:
                    alone=0
                    if b != 2 and b != 11 and b != 20:
                        c=0
                if c == 1 and alone == 0:
                    if a < 9:
                        b1=0
                    elif a < 18:
                        b1=9
                    elif a < 27:
                        b1=18
                    elif a < 36:
                        b1=27
                    elif a < 45:
                        b1=36
                    elif a < 54:
                        b1=45
                    elif a < 63:
                        b1=54
                    elif a < 72:
                        b1=63
                    else:
                        b1=72
                    if b1 == 0 or b1 == 9 or b1 == 18:
                        pm[a*9+a1+(27-b1)*9]=0
                        pm[a*9+a1+(36-b1)*9]=0
                        pm[a*9+a1+(45-b1)*9]=0
                        pm[a*9+a1+(54-b1)*9]=0
                        pm[a*9+a1+(63-b1)*9]=0
                        pm[a*9+a1+(72-b1)*9]=0
                    if b1 == 27 or b1 == 36 or b1 == 45:
                        pm[a*9+a1-b1*9]=0
                        pm[a*9+a1+(9-b1)*9]=0
                        pm[a*9+a1+(18-b1)*9]=0
                        pm[a*9+a1+(54-b1)*9]=0
                        pm[a*9+a1+(63-b1)*9]=0
                        pm[a*9+a1+(72-b1)*9]=0
                    if b1 == 54 or b1 == 63 or b1 == 72:
                        pm[a*9+a1-b1*9]=0
                        pm[a*9+a1+(9-b1)*9]=0
                        pm[a*9+a1+(18-b1)*9]=0
                        pm[a*9+a1+(27-b1)*9]=0
                        pm[a*9+a1+(36-b1)*9]=0
                        pm[a*9+a1+(45-b1)*9]=0
            a1+=1
        a+=1
    return pm