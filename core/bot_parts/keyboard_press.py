import pyautogui


def keyboard_action(step, context):
    atype = step.get('action_type', '')

    match atype:
        case 'print_text':
            print_text(step.get('path', None), step.get('interval', 0.05))
        case 'key_press_or_release':
            # key_press_or_release()
            pass
        case _:
            pass


def perform_press(key):
    action = {
        'press': pyautogui.press,
    }


def print_text(path, interval):
    if path:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                text = f.read()
                pyautogui.typewrite(text, interval=interval)
        except Exception as err:
            print(f'{__name__} Ошибка {err}')
            return
