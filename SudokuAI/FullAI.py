#this is the main file responsible for the AI
from SudokuAI.Converter import pmConvert
from SudokuAI.Converter import gridConvert
from SudokuAI.RowTactics import OCIR
from SudokuAI.RowTactics import NSNIR
from SudokuAI.CollumTactics import OCIC
from SudokuAI.CollumTactics import NSNIC
from SudokuAI.BoxTactics import OCIB
from SudokuAI.BoxTactics import NSNIB
from SudokuAI.BoxTactics import RANB
from SudokuAI.BoxTactics import CANB
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
        if pm0 == pm:
            break
    grid=gridConvert(pm)
    return grid