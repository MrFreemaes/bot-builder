import pyautogui as gui


def click_on_coordinates(step, context):
    point = context.get(step['point_from'])
    if point:
        gui.click(*point)
        print(f'{__name__} Клик по координатам: {point}')
    else:
        print(f'{__name__} Точка не найдена в контексте')
