#main file
from readFiles import readFiles
from runGame import runGame
#test grids used in development:
#415030826003010700002000400000203000026040070000609000001000600008020900279060158 a
#
#400763080008000704010000020500607001700040002800209003090000030204000500070984006
#452763189938125764617498325529637841763841952841259673196572438284316597375984216 this is the same as the previous one but solved

#starting the game
initialArguments=readFiles()
aishowstring=initialArguments[0]
showfixed=initialArguments[1]
language=initialArguments[2]
english=initialArguments[3]
portuguese=initialArguments[4]
spanish=initialArguments[5]
afterArguments=runGame(aishowstring, showfixed, language, english, portuguese, spanish)
aishowstring=afterArguments[0]
showfixed=afterArguments[1]
language=afterArguments[2]
file=open("options.txt", "w")
file.write("aishowstring='%s'\nshowfixed='%s'\nlanguage='%s'\n" % (aishowstring, showfixed, language))
file.close