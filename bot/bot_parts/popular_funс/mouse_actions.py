import pyautogui as gui


def mouse_coordinates():
    x, y = gui.position()
    return x, y
