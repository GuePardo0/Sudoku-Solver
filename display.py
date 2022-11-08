#this file is used to display the grid in a more human understandable way
def display(grid, fixed = ""):
    #main function
    #displays the grid
    if fixed == "":
        fixed=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    a=0
    while a != len(fixed):
        if fixed[a] == 1 or fixed[a] == "1":
            fixed[a]="'"
        else:
            fixed[a]=" "
        a+=1
    b=0
    while b != len(grid):
        if grid[b] == 0 or grid[b] == "0" or grid[b] == "":
            grid[b] = " "
        b+=1
    a=0
    c=0
    print(" -----------  -----------  -----------")
    while a != len(grid):
        print("|%s%s%s|%s%s%s|%s%s%s||%s%s%s|%s%s%s|%s%s%s||%s%s%s|%s%s%s|%s%s%s|" % (fixed[a], grid[a], fixed[a], fixed[a+1], grid[a+1], fixed[a+1], fixed[a+2], grid[a+2], fixed[a+2], fixed[a+3], grid[a+3], fixed[a+3], fixed[a+4], grid[a+4], fixed[a+4], fixed[a+5], grid[a+5], fixed[a+5], fixed[a+6], grid[a+6], fixed[a+6], fixed[a+7], grid[a+7], fixed[a+7], fixed[a+8], grid[a+8], fixed[a+8]))
        if c == 2:
            print(" -----------  -----------  -----------")
        if c == 5:
            print(" -----------  -----------  -----------")
        a=a+9
        c=c+1
    print(" -----------  -----------  -----------")
    a=0
    while a != len(grid):
        if grid[a] == " ":
            grid[a]=0
        if fixed[a] == "'":
            fixed[a]=1
        else:
            fixed[a]=0
        a+=1