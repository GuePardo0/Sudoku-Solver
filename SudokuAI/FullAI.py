#this is the main file responsible for the AI
from SudokuAI.Converter import pmConvert
from SudokuAI.Converter import gridConvert
from SudokuAI.BasicStrategies import NSNIR
from SudokuAI.BasicStrategies import NSNIC
from SudokuAI.BasicStrategies import NSNIB
from SudokuAI.BasicStrategies import OCIR
from SudokuAI.BasicStrategies import OCIC
from SudokuAI.BasicStrategies import OCIB
from SudokuAI.ComplexStrategies import RANB
from SudokuAI.ComplexStrategies import CANB
from SudokuAI.ComplexStrategies import NRSB
from SudokuAI.ComplexStrategies import NCSB
from SudokuAI.ComplexStrategies import pairsRow
from SudokuAI.ComplexStrategies import pairsColumn
from SudokuAI.ComplexStrategies import pairsBox
def FullAI(grid, alignedPm=True, pairs=True):
    #main funtion
    #runs the AI
    pm=pmConvert(grid)
    while 1:
        pm0=list(pm)
        pm=NSNIR(pm)
        pm=NSNIC(pm)
        pm=NSNIB(pm)
        pm=OCIR(pm)
        pm=OCIC(pm)
        pm=OCIB(pm)
        if alignedPm == True:
            pm=RANB(pm)
            pm=CANB(pm)
            pm=NRSB(pm)
            pm=NCSB(pm)
        if pairs == True:
            pm=pairsRow(pm)
            pm=pairsColumn(pm)
            pm=pairsBox(pm)
        if pm0 == pm:
            break
    grid=gridConvert(pm)
    return grid