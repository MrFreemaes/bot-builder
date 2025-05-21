from PIL import ImageGrab
import cv2
import numpy as np


def full_screen():
    full_screenshot = ImageGrab.grab()
    img = cv2.cvtColor(np.array(full_screenshot), cv2.COLOR_RGB2GRAY)
    return img


def screen_of_mause(radius, mouse_x, mouse_y):
    box = (
        mouse_x - radius,
        mouse_y - radius,
        mouse_x + radius,
        mouse_y + radius
    )

    screenshot_mause = ImageGrab.grab(box)
    img = cv2.cvtColor(np.array(screenshot_mause), cv2.COLOR_RGB2GRAY)
    return img
