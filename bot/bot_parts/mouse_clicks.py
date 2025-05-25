import pyautogui as gui


# нажать по координатам
def click(step, context):
    point = context.get(step['point_from'])
    if point:
        pressing_type = step.get('pressing_type', 'click')
        time_of_movement = step.get('time_of_movement')

        if time_of_movement:
            gui.moveTo(*point, duration=time_of_movement)

        if pressing_type == 'click':
            gui.click(*point)
        elif pressing_type == 'double_click':
            gui.doubleClick(*point)
        elif pressing_type == 'right_click':
            gui.rightClick(*point)
        elif pressing_type == 'middle_click':
            gui.middleClick(*point)
        else:
            print(f'{__name__} Тип нажатия не определен, нажата лкм')
            gui.click(*point)
    else:
        print(f'{__name__} Точка не найдена в контексте')


# передвинуть в координаты и нажать
def moveto_and_click(step, context):
    """
    Функция очень похожа на click().
    Она сделана чтобы не жертвовать временем на обработку gui.moveTo
    moveTo тратит время даже если duration=0
    """
    point = context.get(step['point_from'])

    if point:
        time_of_movement = step.get('time_of_movement', 0.3)
        pressing_type = step.get('pressing_type', 'click')

        # может показаться не логичным использовать moveto 4 раза.
        # это сделано чтобы не было возможности передвинуть мышку перед самым нажатием
        # протестить с 1 использованием
        if pressing_type == 'click':
            gui.moveTo(*point, duration=time_of_movement)
            gui.click(*point)
        elif pressing_type == 'double_click':
            gui.moveTo(*point, duration=time_of_movement)
            gui.doubleClick(*point)
        elif pressing_type == 'right_click':
            gui.moveTo(*point, duration=time_of_movement)
            gui.rightClick(*point)
        elif pressing_type == 'middle_click':
            gui.moveTo(*point, duration=time_of_movement)
            gui.middleClick(*point)
        else:
            print(f'{__name__} Тип нажатия не определен, нажата лкм')
            gui.click(*point)
    else:
        print(f'{__name__} Точка не найдена в контексте')
