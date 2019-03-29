from imagesearch import *

def ImageFound(image):
    if image[0] != -1 :
        return True
    else:
        return False

def ProcessDuplicant(x1, y1, x2, y2, c1, c2):
    # Find Divers Lungs
    counter = 0
    divers = imagesearcharea("DiversLungs.png", x1, y1, x2, y2)
    gastrophobia = imagesearcharea("Gastrophobia.png", x1, y1, x2, y2)
    pacifist = imagesearcharea("Pacifist.png", x1, y1, x2, y2)

    while ((( ImageFound(divers)  and  (ImageFound(gastrophobia) or ImageFound(pacifist)) ) == False ) and counter < 500 ):
        pyautogui.click(c1, c2)
        counter += 1
        divers = imagesearcharea("DiversLungs.png", x1, y1, x2, y2)
        gastrophobia = imagesearcharea("Gastrophobia.png", x1, y1, x2, y2)
        pacifist = imagesearcharea("Pacifist.png", x1, y1, x2, y2)

ProcessDuplicant(870, 510, 1040, 560, 1000, 425)
ProcessDuplicant(1270, 510, 1470, 560, 1400, 425)
ProcessDuplicant(1670, 510, 1870, 560, 1800, 425)
