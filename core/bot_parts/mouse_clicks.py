import pyautogui


# возможная проверка координат
# if point is None or not isinstance(point, (tuple, list)) or len(point) != 2:
#     print(f'{__name__} Некорректные координаты: {point}')
#     return

def mouse_actions(step, context):
    """
    Функция определяющая действия с мышкой записанные в config/name.yaml.
    Возможно определение координат как пользователем, так и автоматически.
    """
    if step.get('coordinates'):
        point = step.get('coordinates')
    else:
        point = context.get(step['point_from'])

    if point:
        atype = step.get('action_type', 'click')
        ptype = step.get('pressing_type')

        match atype:
            case 'click':
                click(ptype, point)
            case 'move_to_and_click':
                move_to_and_click(ptype, point, step.get('time_of_movement', 0.2))
            case 'move_to':
                context[step['point_from']] = point  # чтобы мышка оставалась там куда ее передвинули
                pyautogui.moveTo(*point, duration=step.get('time_of_movement', 0.2))
            case 'mouse_down_or_up':
                mouse_down_or_up(ptype, point)
            case _:
                print(f'{__name__} Действие не определено')


def perform_click(ptype, point):
    actions = {
        'click': pyautogui.click,
        'double_click': pyautogui.doubleClick,
        'right_click': pyautogui.rightClick,
        'middle_click': pyautogui.middleClick,
    }
    actions.get(ptype, pyautogui.click)(*point)


# нажать по координатам
def click(ptype, point):
    perform_click(ptype, point)


# передвинуть в координаты и нажать
def move_to_and_click(ptype, point, move_time):
    pyautogui.moveTo(*point, duration=move_time)
    perform_click(ptype, point)


# зажать и отпустить кнопку
def mouse_down_or_up(ptype, point):
    """
    Функция для нажатия и отпускания лкм.
    """
    if ptype == 'down':
        pyautogui.mouseDown(*point)
    elif ptype == 'up':
        pyautogui.mouseUp(*point)
    else:
        print(f'{__name__} Тип нажатия не определен')
