#main file
from readFiles import readFiles
from runGame import runGame
#test grids used in development:
#
#400763080008000704010000020500607001700040002800209003090000030204000500070984006
#452763189938125764617498325529637841763841952841259673196572438284316597375984216 (solved)
#
#415030826003010700002000400000203000026040070000609000001000600008020900279060158
#415937826863412795792586413984273561526841379137659284351798642648125937279364158 (solved)
#
#"easy"
#680002049730590610200760058568000103190080004042900860800000200000001000003056980
#685132749734598612219764358568427193197683524342915867851349276926871435473256981 (solved)
#
#"medium"
#000072013000900687000030054900007045050390706400000000210006038600020000004500000
#568472913342951687197638254926817345851394726473265891219746538685123479734589162 (solved)
#
#"hard"
#003600007000000015050070680009800000102007008000102000040000000700000309801004200
#913685427687423915254971683479856132162347598538192764345269871726518349891734256 (solved)
#
#"hard"
#000000000090060800010400030950300008000500200040900600205000000080070100001040002
#724839516593761824816452739952316478637584291148927653265198347489273165371645982 (solved)
#
#"expert"
#000070030005000100080309000503027080600000007002500000000450008040000060000006009
#469175832735248196281369745513627984694813257872594613926451378347982561158736429 (solved)
#
#"expert"
#000800060000400081000293000320000800090340002000000003031600750004039028800070030
#543817269279456381186293475325961847697348512418725693931682754764539128852174936 (solved)
#
#"expert"
#800000000040000060006400010000500900010000008003097005000085000000704120700200000
#
#
#"evil"
#080370902400050000000000070005030701010000060000700080020900103000000006008002000
#586374912479251638132698574265839741817425369943716285624987153791543826358162497 (solved)
#
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