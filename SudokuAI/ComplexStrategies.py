#this file creates functions that make complex Sudoku strategies
from SudokuAI.Converter import gridConvert
from getPosition import gpr
from getPosition import gpc
from getPosition import gpb
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
                if pm[a*9+a1-b*9] == 1 and b != 0:
                    alone=0
                    if b != 0 and b != 1 and b != 2:
                        c=0
                if pm[a*9+a1+(-b+1)*9] == 1 and b != 1:
                    alone=0
                    if b != 0 and b != 1 and b != 2:
                        c=0
                if pm[a*9+a1+(-b+2)*9] == 1 and b != 2:
                    alone=0
                    if b != 0 and b != 1 and b != 2:
                        c=0
                if pm[a*9+a1+(-b+9)*9] == 1 and b != 9:
                    alone=0
                    if b != 9 and b != 10 and b != 11:
                        c=0
                if pm[a*9+a1+(-b+10)*9] == 1 and b != 10:
                    alone=0
                    if b != 9 and b != 10 and b != 11:
                        c=0
                if pm[a*9+a1+(-b+11)*9] == 1 and b != 1:
                    alone=0
                    if b != 9 and b != 10 and b != 11:
                        c=0
                if pm[a*9+a1+(-b+18)*9] == 1 and b != 18:
                    alone=0
                    if b != 18 and b != 19 and b != 20:
                        c=0
                if pm[a*9+a1+(-b+19)*9] == 1 and b != 19:
                    alone=0
                    if b != 18 and b != 19 and b != 20:
                        c=0
                if pm[a*9+a1+(-b+20)*9] == 1 and b != 20:
                    alone=0
                    if b != 18 and b != 19 and b != 20:
                        c=0
                if c == 1 and alone == 0:
                    b1=gpc(a)
                    if b1 < 3:
                        pm[a*9+a1+(3-b1)*9]=0
                        pm[a*9+a1+(4-b1)*9]=0
                        pm[a*9+a1+(5-b1)*9]=0
                        pm[a*9+a1+(6-b1)*9]=0
                        pm[a*9+a1+(7-b1)*9]=0
                        pm[a*9+a1+(8-b1)*9]=0
                    if b1 > 2 and b1 < 6:
                        pm[a*9+a1-b1*9]=0
                        pm[a*9+a1+(1-b1)*9]=0
                        pm[a*9+a1+(2-b1)*9]=0
                        pm[a*9+a1+(6-b1)*9]=0
                        pm[a*9+a1+(7-b1)*9]=0
                        pm[a*9+a1+(8-b1)*9]=0
                    if b1 > 5:
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
                if pm[a*9+a1-b*9] == 1 and b != 0:
                    alone=0
                    if b != 0 and b != 9 and b != 18:
                        c=0
                if pm[a*9+a1+(-b+9)*9] == 1 and b != 9:
                    alone=0
                    if b != 0 and b != 9 and b != 18:
                        c=0
                if pm[a*9+a1+(-b+18)*9] == 1 and b != 18:
                    alone=0
                    if b != 0 and b != 9 and b != 18:
                        c=0
                if pm[a*9+a1+(-b+1)*9] == 1 and b != 1:
                    alone=0
                    if b != 1 and b != 10 and b != 19:
                        c=0
                if pm[a*9+a1+(-b+10)*9] == 1 and b != 10:
                    alone=0
                    if b != 1 and b != 10 and b != 19:
                        c=0
                if pm[a*9+a1+(-b+19)*9] == 1 and b != 19:
                    alone=0
                    if b != 1 and b != 10 and b != 19:
                        c=0
                if pm[a*9+a1+(-b+2)*9] == 1 and b != 2:
                    alone=0
                    if b != 2 and b != 11 and b != 20:
                        c=0
                if pm[a*9+a1+(-b+11)*9] == 1 and b != 11:
                    alone=0
                    if b != 2 and b != 11 and b != 20:
                        c=0
                if pm[a*9+a1+(-b+20)*9] == 1 and b != 20:
                    alone=0
                    if b != 2 and b != 11 and b != 20:
                        c=0
                if c == 1 and alone == 0:
                    b1=gpr(a)
                    if b1 < 3:
                        pm[a*9+a1+(3-b1)*81]=0
                        pm[a*9+a1+(4-b1)*81]=0
                        pm[a*9+a1+(5-b1)*81]=0
                        pm[a*9+a1+(6-b1)*81]=0
                        pm[a*9+a1+(7-b1)*81]=0
                        pm[a*9+a1+(8-b1)*81]=0
                    if b1 > 2 and b1 < 6:
                        pm[a*9+a1-b1*81]=0
                        pm[a*9+a1+(1-b1)*81]=0
                        pm[a*9+a1+(2-b1)*81]=0
                        pm[a*9+a1+(6-b1)*81]=0
                        pm[a*9+a1+(7-b1)*81]=0
                        pm[a*9+a1+(8-b1)*81]=0
                    if b1 > 5:
                        pm[a*9+a1-b1*81]=0
                        pm[a*9+a1+(1-b1)*81]=0
                        pm[a*9+a1+(2-b1)*81]=0
                        pm[a*9+a1+(3-b1)*81]=0
                        pm[a*9+a1+(4-b1)*81]=0
                        pm[a*9+a1+(5-b1)*81]=0
            a1+=1
        a+=1
    return pm
def NRSB(pm):
    #if the only possible numbers in a row are in the same box, clears all numbers in that box
    #NRSB = Numbers in Row in the Same Box
    a=0
    while a != len(pm)/9:
        b=gpc(a)
        a1=0
        while a1 != 9:
            if pm[a*9+a1] == 1:
                c=1
                alone=1
                if pm[a*9+a1-b*9] == 1 and b != 0:
                    alone=0
                    if b > 2:
                        c=0
                if pm[a*9+a1+(-b+1)*9] == 1 and b != 1:
                    alone=0
                    if b > 2:
                        c=0
                if pm[a*9+a1+(-b+2)*9] == 1 and b != 2:
                    alone=0
                    if b > 2:
                        c=0
                if pm[a*9+a1+(-b+3)*9] == 1 and b != 3:
                    alone=0
                    if b < 3 or b > 5:
                        c=0
                if pm[a*9+a1+(-b+4)*9] == 1 and b != 4:
                    alone=0
                    if b < 3 or b > 5:
                        c=0
                if pm[a*9+a1+(-b+5)*9] == 1 and b != 5:
                    alone=0
                    if b < 3 or b > 5:
                        c=0
                if pm[a*9+a1+(-b+6)*9] == 1 and b != 6:
                    alone=0
                    if b < 6:
                        c=0
                if pm[a*9+a1+(-b+7)*9] == 1 and b != 7:
                    alone=0
                    if b < 6:
                        c=0
                if pm[a*9+a1+(-b+8)*9] == 1 and b != 8:
                    alone=0
                    if b < 6:
                        c=0
                if c == 1 and alone == 0:
                    b1=gpb(a)
                    b0=b1
                    if b0 > 2:
                        b1+=6
                    if b0 > 5:
                        b1+=6
                    if b1 < 9:
                        pm[a*9+a1+(9-b1)*9]=0
                        pm[a*9+a1+(10-b1)*9]=0
                        pm[a*9+a1+(11-b1)*9]=0
                        pm[a*9+a1+(18-b1)*9]=0
                        pm[a*9+a1+(19-b1)*9]=0
                        pm[a*9+a1+(20-b1)*9]=0
                    if b1 > 2 and b1 < 18:
                        pm[a*9+a1-b1*9]=0
                        pm[a*9+a1+(1-b1)*9]=0
                        pm[a*9+a1+(2-b1)*9]=0
                        pm[a*9+a1+(18-b1)*9]=0
                        pm[a*9+a1+(19-b1)*9]=0
                        pm[a*9+a1+(20-b1)*9]=0
                    if b1 > 11:
                        pm[a*9+a1-b1*9]=0
                        pm[a*9+a1+(1-b1)*9]=0
                        pm[a*9+a1+(2-b1)*9]=0
                        pm[a*9+a1+(9-b1)*9]=0
                        pm[a*9+a1+(10-b1)*9]=0
                        pm[a*9+a1+(11-b1)*9]=0                    
            a1+=1
        a+=1
    return pm
def NCSB(pm):
    #if the only possible numbers in a column are in the same box, clears all numbers in that box
    #NCSB = Numbers in Column in the Same Box
    a=0
    while a != len(pm)/9:
        b=gpr(a)
        a1=0
        while a1 != 9:
            if pm[a*9+a1] == 1:
                c=1
                alone=1
                if pm[a*9+a1-b*81] == 1 and b != 0:
                    alone=0
                    if b > 2:
                        c=0
                if pm[a*9+a1+(-b+1)*81] == 1 and b != 1:
                    alone=0
                    if b > 2:
                        c=0
                if pm[a*9+a1+(-b+2)*81] == 1 and b != 2:
                    alone=0
                    if b > 2:
                        c=0
                if pm[a*9+a1+(-b+3)*81] == 1 and b != 3:
                    alone=0
                    if b < 3 or b > 5:
                        c=0
                if pm[a*9+a1+(-b+4)*81] == 1 and b != 4:
                    alone=0
                    if b < 3 or b > 5:
                        c=0
                if pm[a*9+a1+(-b+5)*81] == 1 and b != 5:
                    alone=0
                    if b < 3 or b > 5:
                        c=0
                if pm[a*9+a1+(-b+6)*81] == 1 and b != 6:
                    alone=0
                    if b < 6:
                        c=0
                if pm[a*9+a1+(-b+7)*81] == 1 and b != 7:
                    alone=0
                    if b < 6:
                        c=0
                if pm[a*9+a1+(-b+8)*81] == 1 and b != 8:
                    alone=0
                    if b < 6:
                        c=0
                if c == 1 and alone == 0:
                    b1=gpb(a)
                    b0=b1
                    if b0 > 2:
                        b1+=6
                    if b0 > 5:
                        b1+=6
                    if b1 == 0 or b == 9 or b == 18:
                        pm[a*9+a1+(1-b1)*9]=0
                        pm[a*9+a1+(2-b1)*9]=0
                        pm[a*9+a1+(10-b1)*9]=0
                        pm[a*9+a1+(11-b1)*9]=0
                        pm[a*9+a1+(19-b1)*9]=0
                        pm[a*9+a1+(20-b1)*9]=0
                    if b1 == 1 or b == 10 or b == 19:
                        pm[a*9+a1-b1*9]=0
                        pm[a*9+a1+(2-b1)*9]=0
                        pm[a*9+a1+(9-b1)*9]=0
                        pm[a*9+a1+(11-b1)*9]=0
                        pm[a*9+a1+(18-b1)*9]=0
                        pm[a*9+a1+(20-b1)*9]=0
                    if b1 == 2 or b == 11 or b == 20:
                        pm[a*9+a1-b1*9]=0
                        pm[a*9+a1+(1-b1)*9]=0
                        pm[a*9+a1+(9-b1)*9]=0
                        pm[a*9+a1+(10-b1)*9]=0
                        pm[a*9+a1+(18-b1)*9]=0
                        pm[a*9+a1+(19-b1)*9]=0                    
            a1+=1
        a+=1
    return pm