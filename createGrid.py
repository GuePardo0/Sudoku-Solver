#this file is used to create the grid of a list
#(now that I've realized my mistake, I know it would be better to use what I call lists in display.py
#instead of grids but I'm too lazy to do that. I might do it some day, though)
def tf(s):
    #transforms single digit number strings into integers
    #if the input is not a single digit number string, it just returns ""
    #tf = transform
    s1=""
    if s == "0":
        s1=0
    elif s == "1":
        s1=1
    elif s == "2":
        s1=2
    elif s == "3":
        s1=3
    elif s == "4":
        s1=4
    elif s == "5":
        s1=5
    elif s == "6":
        s1=6
    elif s == "7":
        s1=7
    elif s == "8":
        s1=8
    elif s == "9":
        s1=9
    return s1
def createGrid(list):
    #main function
    #creates the grid of a list
    grid=["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    a=0
    while a != 81:
        grid[a]=tf(list[a])
        a+=1
    return grid