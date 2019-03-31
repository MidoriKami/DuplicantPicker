try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from multiprocessing.dummy import Pool as ThreadPool
import numpy as np
from imagesearch import *
import sys
import psutil
import win32gui
import win32con

def ImageFound(image):
    if image[0] != -1 :
        return True
    else:
        return False



def ProcessDuplicant(x1, y1, x2, y2, c1, c2):
    counter = 0
    divers = imagesearcharea("DiversLungs.png", x1, y1, x2, y2)
    gastrophobia = imagesearcharea("Gastrophobia.png", x1, y1, x2, y2)
    pacifist = imagesearcharea("Pacifist.png", x1, y1, x2, y2)

    while ((( ImageFound(divers)  and  (ImageFound(gastrophobia) or ImageFound(pacifist)) ) == False ) and counter < 100 ):
        pyautogui.click(c1, c2)
        counter += 1
        divers = imagesearcharea("DiversLungs.png", x1, y1, x2, y2)
        gastrophobia = imagesearcharea("Gastrophobia.png", x1, y1, x2, y2)
        pacifist = imagesearcharea("Pacifist.png", x1, y1, x2, y2)

if "OxygenNotIncluded.exe" in (p.name() for p in psutil.process_iter()) :
    pool = ThreadPool(13)

    whnd = win32gui.FindWindow(None, "Oxygen Not Included")

    win32gui.ShowWindow(whnd, win32con.SW_MAXIMIZE)
    win32gui.SetForegroundWindow(whnd)


    #   All values are screen coordinates
    #   x1, y1, x2, y2, c1, c2
    #
    #   x1 -    Top Left X Coordinate for the "Traits Section" of the duplicant
    #   y1 -    Top Left Y Coordinate for the "Traits Section" of the duplicant
    #   x2 -    Bottom Right X Coordinate for the "Traits Section" of the duplicant
    #   y2 -    Bottom Right Y Coordinate for the "Traits Section" of the duplicant
    #   c1 -    X Coordinate for "Suffle Button"
    #   c2 -    Y Coordinate for "Shuffle Button"
    pool.starmap(ProcessDuplicant, [ 
        [870, 510, 1040, 560, 1000, 425], 
        [1270, 510, 1470, 560, 1400, 425],
        [1670, 510, 1870, 560, 1800, 425]
    ])

