import pyautogui as gui


def mouse_actions(step, context):
    if step.get('coordinates'):
        point = step.get('coordinates')
    else:
        point = context.get(step['point_from'])

    if point:
        atype = step.get('action_type', 'click')
        ptype = step.get('pressing_type')

        if atype == 'click':
            click(ptype, point)

        elif atype == 'move_to_and_click':
            time_of_movement = step.get('time_of_movement', 0.2)
            move_to_and_click(ptype, point, time_of_movement)

        elif atype == 'move_to':
            time_of_movement = step.get('time_of_movement', 0.2)
            context[step['point_from']] = point  # чтобы мышка оставалась там куда ее передвинули
            gui.moveTo(*point, duration=time_of_movement)

        elif atype == 'mouse_down_or_up':
            mouse_down_or_up(ptype, point)

        else:
            print(f'{__name__} Действие не определено')


# нажать по координатам
def click(ptype, point):
    if ptype == 'click':
        gui.click(*point)
    elif ptype == 'double_click':
        gui.doubleClick(*point)
    elif ptype == 'right_click':
        gui.rightClick(*point)
    elif ptype == 'middle_click':
        gui.middleClick(*point)
    else:
        print(f'{__name__} Тип нажатия не определен, нажата лкм')
        gui.click(*point)


# передвинуть в координаты и нажать
def move_to_and_click(ptype, point, move_time):
    gui.moveTo(*point, duration=move_time)
    if ptype == 'click':
        gui.click(*point)
    elif ptype == 'double_click':
        gui.doubleClick(*point)
    elif ptype == 'right_click':
        gui.rightClick(*point)
    elif ptype == 'middle_click':
        gui.middleClick(*point)
    else:
        print(f'{__name__} Тип нажатия не определен, нажата лкм')
        gui.click(*point)


# зажать и отпустить кнопку
def mouse_down_or_up(ptype, point):
    if ptype == 'down':
        gui.mouseDown(*point)
    elif ptype == 'up':
        gui.mouseUp(*point)
    else:
        print(f'{__name__} Тип нажатия не определен')
