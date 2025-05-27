import pyautogui


def mouse_coordinates():
    """
    Возвращает координаты мышки в данный момент.
    """
    x, y = pyautogui.position()
    return x, y
