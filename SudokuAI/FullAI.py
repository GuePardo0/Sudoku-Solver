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
def FullAI(grid):
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
        pm=RANB(pm)
        pm=CANB(pm)
        pm=NRSB(pm)
        pm=NCSB(pm)
        if pm0 == pm:
            break
    grid=gridConvert(pm)
    return grid