#this file is used to get the position of a cell inside its box
def gpb(pos):
    #main function
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
        posb=0
    if pos in pos2:
        posb=1
    if pos in pos3:
        posb=2
    if pos in pos4:
        posb=3
    if pos in pos5:
        posb=4
    if pos in pos6:
        posb=5
    if pos in pos7:
        posb=6
    if pos in pos8:
        posb=7
    if pos in pos9:
        posb=8
    return posb