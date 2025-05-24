from PIL import ImageGrab
import cv2
import numpy as np


# конвертируем изображение в серое
def gray_image(screenshot):
    img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)
    return img


# скрин полного экрана
def full_screenshot():
    screenshot = ImageGrab.grab()
    return gray_image(screenshot)


# скрин по координатам мышки
def screenshot_of_mause(radius, mouse_x, mouse_y):
    box = (
        mouse_x - radius,
        mouse_y - radius,
        mouse_x + radius,
        mouse_y + radius
    )

    screenshot = ImageGrab.grab(box)
    return gray_image(screenshot)


# скрин по координатам
def screenshot_by_coordinates(x_1, y_1, x_2, y_2):
    box = (x_1, y_1, x_2, y_2)

    screenshot = ImageGrab.grab(box)
    return gray_image(screenshot)
