import pyautogui
import time
from pyautogui import pixelMatchesColor
# init Pixel of CDG icon
pix_loggedin1 = (211, 45, 31)
pix_loggedin2 = (208, 18, 27)
pix_loggedin3 = (207, 17, 26)
pix_not_login1 = (86, 84, 83)
pix_not_login2 = (110, 196, 53)

def Get_CDG_Icon_Position():
    abscissa = 0
    ordinates = 0
    # Get screen size
    x, y = pyautogui.size()
    flag = 0
    # traversal coordinate
    for i in range(int(x * 0.8), x):
        for j in range(y - 30, y):
            # compare pixel of every coordinate
            match1 = pixelMatchesColor(i, j, pix_loggedin1, tolerance=10)
            match2 = pixelMatchesColor(i, j, pix_loggedin2, tolerance=10)
            match3 = pixelMatchesColor(i, j, pix_not_login1, tolerance=10)
            match4 = pixelMatchesColor(i, j, pix_not_login2, tolerance=10)
            match5 = pixelMatchesColor(i, j, pix_loggedin3, tolerance=10)
            # if pixel match to specified pixel,get the coordinate and quit Inner loop
            if match1 or match2 or match3 or match4:
                abscissa = i
                ordinates = j
                flag = 1
                break
            # if find specified quit surrounding loop
            if flag == 1:
                break
    return abscissa,ordinates

print(Get_CDG_Icon_Position())



