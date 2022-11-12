#this file is used to get the position of a cell inside its row, column or box
def gpr(pos):
    #gets the position of a cell inside its row
    #gpc = get position in row
    while pos > 8:
        pos-=9
    return pos
def gpc(pos):
    #gets the position of a cell inside its column
    #gpr = get position in column
    if pos < 9:
        pos=0
    elif pos < 18:
        pos=1
    elif pos < 27:
        pos=2
    elif pos < 36:
        pos=3
    elif pos < 45:
        pos=4
    elif pos < 54:
        pos=5
    elif pos < 63:
        pos=6
    elif pos < 72:
        pos=7
    else:
        pos=8
    return pos
def gpb(pos):
    #gets the position of a cell inside its box
    #gpb = get position in box
    pos1=[0, 3, 6, 27, 30, 33, 54, 57, 60]
    pos2=[1, 4, 7, 28, 31, 34, 55, 58, 61]
    pos3=[2, 5, 8, 29, 32, 35, 56, 59, 62]
    pos4=[9, 12, 15, 36, 39, 42, 63, 66, 69]
    pos5=[10, 13, 16, 37, 40, 43, 64, 67, 70]
    pos6=[11, 14, 17, 38, 41, 44, 65, 68, 71]
    pos7=[18, 21, 24, 45, 48, 51, 72, 75, 78]
    pos8=[19, 22, 25, 46, 49, 52, 73, 76, 79]
    pos9=[20, 23, 26, 47, 50, 53, 74, 77, 80]
    if pos in pos1:
        pos=0
    elif pos in pos2:
        pos=1
    elif pos in pos3:
        pos=2
    elif pos in pos4:
        pos=3
    elif pos in pos5:
        pos=4
    elif pos in pos6:
        pos=5
    elif pos in pos7:
        pos=6
    elif pos in pos8:
        pos=7
    elif pos in pos9:
        pos=8
    return pos