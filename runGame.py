#this file is used to run Sudoku Solver
from createGrid import createGrid
from createGrid import tf
from display import display
from check import check
from fgd import fgd
from rgg import rgg
from SudokuAI.FullAI import FullAI
from time import sleep
def runGame(aishowstring, showfixed, language, english, portuguese, spanish):
    #main function
    #runs Sudoku Solver
    pl="\n"*100
    shutdown=False
    if language == "english":
        languageList=english
    elif language == "portuguese":
        languageList=portuguese
    elif language == "spanish":
        languageList=spanish
    while 1:
        if shutdown == True:
            break
        print(pl)
        x=input("%s\n\n\n\n%s\n\n1 %s\n\n2 %s\n\n3 %s\n\n4 %s\n\n" % (languageList[0], languageList[1], languageList[2], languageList[3], languageList[4], languageList[5]))
        if x == "1":
            while 1:
                print(pl)
                x=input("%s\n\n\n\n1 %s\n\n2 %s\n\n3 %s\n\n4 %s\n\n" % (languageList[6], languageList[7], languageList[8], languageList[9], languageList[10]))
                if x == "1":
                    invcom=0
                    while 1:
                        print(pl)
                        if invcom == 1:
                            print("\n%s\n" % languageList[11])
                            invcom=0
                        x=input("%s\n%s\n\n" % (languageList[12], languageList[13]))
                        a=0
                        while a != len(x):
                            if tf(x[a]) == "":
                                invcom=1
                            a+=1
                        if len(x) == 81 and invcom == 0:
                            while 1:
                                print(pl)
                                y=input("%s\n\n\n1 %s\n\n2 %s\n\n" % (languageList[14], languageList[15], languageList[16]))
                                if y == "1":
                                    lista=x
                                    grid=createGrid(lista)
                                    fixed=list(grid)
                                    a=0
                                    while a != len(fixed):
                                        if fixed[a] != 0:
                                            fixed[a]=1
                                        a+=1
                                    print(pl)
                                    if showfixed == "true":
                                        display(grid, fixed)
                                    else:
                                        display(grid)
                                    x=input("\n\n%s\n%s\n\n" % (languageList[31], languageList[32]))
                                    help=0
                                    while 1:
                                        if len(x) == 6 and x != "%s" % languageList[21] and x != "%s" % languageList[22] and x != "%s" % languageList[23] and x != "%s" % languageList[24] and x != "%s" % languageList[25] and x != "%s" % languageList[26] and x != "%s" % languageList[27] and x != "%s" % languageList[28] and x != "%s" % languageList[29] and x != "%s" % languageList[30]:
                                            if x[0] == "%s" % languageList[17] or x[0] == "%s" % languageList[18] and tf(x[1]) != "" and x[2] == "%s" % languageList[19] or x[2] == "%s" % languageList[20] and tf(x[3]) != "" and x[4] == "=" and tf(x[5]) != "":
                                                print(fixed[tf(x[3])+tf(x[1])*9-10])
                                                if fixed[tf(x[3])+tf(x[1])*9-10] == 0:
                                                    grid[tf(x[3])+tf(x[1])*9-10]=tf(x[5])
                                                print(pl)
                                                if showfixed == "true":
                                                    display(grid, fixed)
                                                else:
                                                    display(grid)
                                                if fgd(grid) == 1:
                                                    if check(grid) == 0:
                                                        x=input("\n%s\n\n%s\n\n" % (languageList[33], languageList[34]))
                                                    else:
                                                        x=input("\n%s\n%s\n\n%s\n%s\n\n" % (languageList[35], languageList[36], languageList[31], languageList[32]))
                                                else:
                                                    x=input("\n\n%s\n%s\n\n" % (languageList[31], languageList[32]))
                                            else:
                                                print(pl)
                                                if showfixed == "true":
                                                    display(grid, fixed)
                                                else:
                                                    display(grid)
                                                if fgd(grid) == 1:
                                                    if check(grid) == 0:
                                                        x=input("\n%s\n\n%s\n\n" % (languageList[33], languageList[34]))
                                                    else:
                                                        x=input("\n%s\n%s\n\n%s\n%s\n\n" % (languageList[35], languageList[36], languageList[31], languageList[32]))
                                                else:
                                                    x=input("\n%s\n\n%s\n%s\n\n" % (languageList[37], languageList[31], languageList[32]))
                                        elif x == "%s" % languageList[21] or x == "%s" % languageList[22]:
                                            checkerror="%s" % languageList[38]
                                            if check(grid) == 1:
                                                checkerror="%s\n%s" % (languageList[35], languageList[36])
                                            print(pl)
                                            if showfixed == "true":
                                                display(grid, fixed)
                                            else:
                                                display(grid)
                                            if fgd(grid) == 1:
                                                if check(grid) == 0:
                                                    x=input("\n%s\n\n%s\n\n" % (languageList[33], languageList[34]))
                                                else:
                                                    x=input("\n%s\n%s\n\n%s\n%s\n\n" % (languageList[35], languageList[36], languageList[31], languageList[32]))
                                            else:
                                                x=input("\n%s\n\n%s\n%s\n\n" % (checkerror, languageList[31], languageList[32]))
                                        elif x == "%s" % languageList[23] or x == "%s" % languageList[24]:
                                            a=0
                                            while a != len(grid):
                                                if fixed[a] == 0:
                                                    grid[a]=0
                                                a+=1
                                            print(pl)
                                            if showfixed == "true":
                                                display(grid, fixed)
                                            else:
                                                display(grid)
                                            x=input("\n%s\n\n%s\n%s\n\n" % (languageList[39], languageList[31], languageList[32]))
                                        elif x == "%s" % languageList[25] or x == "%s" % languageList[26]:
                                            break
                                        elif x == "%s" % languageList[27] or x == "%s" % languageList[28]:
                                            lista=""
                                            a=0
                                            while a != len(grid):
                                                lista+="%s" % grid[a]
                                                a+=1
                                            print(pl)
                                            if showfixed == "true":
                                                display(grid, fixed)
                                            else:
                                                display(grid)
                                            if fgd(grid) == 1:
                                                if check(grid) == 0:
                                                    x=input("\n%s\n%s\n\n%s\n\n%s\n\n" % (languageList[40], lista, languageList[33], languageList[34]))
                                                else:
                                                    x=input("\n%s\n%s\n\n%s\n%s\n\n%s\n%s\n\n" % (languageList[40], lista, languageList[35], languageList[36], languageList[31], languageList[32]))
                                            else:
                                                x=input("\n%s\n%s\n\n%s\n%s\n\n" % (languageList[40], lista, languageList[31], languageList[32]))
                                        elif x == "%s" % languageList[29] or x == "%s" % languageList[30]:
                                            print(pl)
                                            x=input("%s\n\n\n-%s\n%s\n\n-%s\n%s\n\n-%s\n%s\n\n-%s\n%s\n\n-%s\n%s\n\n\n%s" % (languageList[41], languageList[21], languageList[42], languageList[23], languageList[43], languageList[25], languageList[44], languageList[27], languageList[45], languageList[29], languageList[46], languageList[47]))
                                            x=""
                                            help=1
                                        else:
                                            print(pl)
                                            if showfixed == "true":
                                                display(grid, fixed)
                                            else:
                                                display(grid)
                                            if fgd(grid) == 1:
                                                if check(grid) == 0:
                                                    x=input("\n%s\n\n%s\n\n" % (languageList[33], languageList[34]))
                                                else:
                                                    x=input("\n%s\n%s\n\n%s\n%s\n\n" % (languageList[35], languageList[36], languageList[31], languageList[32]))
                                            else:
                                                if help == 0:
                                                    x=input("\n%s\n\n%s\n%s\n\n" % (languageList[37], languageList[31], languageList[32]))
                                                else:
                                                    x=input("\n\n%s\n%s\n\n" % (languageList[31], languageList[32]))
                                                    help=0
                                    break
                                if y == "2":
                                    print(pl)
                                    lista=x
                                    grid=createGrid(lista)
                                    display(grid)
                                    print("\n\n%s\n" % languageList[48])
                                    grid=FullAI(grid)
                                    sleep(1)
                                    if fgd(grid) == 1:
                                        print("\n\n%s\n" % languageList[49])
                                    else:
                                        print("\n\n%s\n" % languageList[50])
                                    display(grid)
                                    if aishowstring == "true":
                                        lista=""
                                        a=0
                                        while a != len(grid):
                                            lista+="%s" % grid[a]
                                            a+=1
                                        print("\n%s\n%s" % (languageList[40], lista))
                                    if check(grid) == 1:
                                        print("\n%s" % languageList[51])
                                    x=input("\n%s" % languageList[47])
                                    break
                            break
                        else:
                            invcom=1
                elif x == "2":
                    print(pl)
                    x=input("%s\n\n%s" % (languageList[59], languageList[47]))
                elif x == "3":
                    print(pl)
                    x=input("%s\n\n%s" % (languageList[59], languageList[47]))
                elif x == "4":
                    break
        elif x == "2":
            while 1:
                print(pl)
                x=input("%s\n\n\n1 %s\n%s\n\n2 %s\n%s %s\n\n3 %s\n%s %s\n\n4 %s\n\n" % (languageList[3], languageList[52], languageList[53], languageList[54], languageList[55], aishowstring, languageList[56], languageList[55], showfixed, languageList[57]))
                if x == "1":
                    if language == "english":
                        language="portuguese"
                        languageList=portuguese
                    elif language == "portuguese":
                        language="spanish"
                        languageList=spanish
                    elif language == "spanish":
                        language="english"
                        languageList=english
                elif x == "2":
                    if aishowstring == "true":
                        aishowstring="false"
                    else:
                        aishowstring="true"
                elif x == "3":
                    if showfixed == "true":
                        showfixed="false"
                    else:
                        showfixed="true"
                elif x == "4":
                    break
        elif x == "3":
            print(pl)
            x=input("%s\n\n\n-%s\n%s\n\n-%s\n%s\n\n-%s\n%s\n\n-%s\n%s\n\n-%s\n%s\n\n\n%s" % (languageList[41], languageList[21], languageList[42], languageList[23], languageList[43], languageList[25], languageList[44], languageList[27], languageList[45], languageList[29], languageList[46], languageList[47]))
        elif x == "4":
            shutdown=True
            print(pl)
            print("%s\n" % languageList[58])
            break
    return aishowstring, showfixed, language