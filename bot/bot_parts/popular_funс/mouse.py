import pyautogui as gui


def mouse_coordinates():
    """
    Возвращает координаты мышки в данный момент.
    """
    x, y = gui.position()
    return x, y
