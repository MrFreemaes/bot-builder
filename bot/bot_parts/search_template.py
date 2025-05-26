import cv2
import numpy as np
from bot.bot_parts.popular_funс import screenshots, mouse
import time


def search_template(step, context):
    """
    Основная функция определяющая какой вид скриншота нам нужен.
    Берет шаблон из пути указанном в config/name.yaml
    """
    template = cv2.imread(step['template_path'], cv2.IMREAD_GRAYSCALE)
    w, h = template.shape[::-1]

    x = time.time()

    # смотрит какой скриншот делать (можно добавлять)
    stype = step.get('screenshot_type', 'full')
    if stype == 'full':
        search_template_everywhere(step, context, template, w, h)
    elif stype == 'around_mouse':
        search_pattern_around_mouse(step, context, template, w, h)
    elif stype == 'by_coordinates':
        search_template_by_coordinates(step, context, template, w, h)
    else:
        search_template_everywhere(step, context, template, w, h)

    print(time.time() - x)


# поиск шаблона вокруг мышки
def search_pattern_around_mouse(step, context, template, w, h):
    """
    Поиск шаблона вокруг мышки.
    Скорость обработки - большая.
    """
    mouse_x, mouse_y = mouse.mouse_coordinates()
    radius = step.get('radius', 300)
    img = screenshots.screenshot_of_mause(radius, mouse_x, mouse_y)

    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    loc_be = np.where(res >= step.get('threshold', 0.8))

    top_left_x = mouse_x - radius
    top_left_y = mouse_y - radius

    if loc_be[0].size > 0:
        # координаты в вырезанном изображении
        pt = (loc_be[1][0], loc_be[0][0])

        # координаты на полном экране
        screen_x = top_left_x + pt[0]
        screen_y = top_left_y + pt[1]
        center = (screen_x + w // 2, screen_y + h // 2)

        context[step['save_as']] = center
        print(f'{__name__} Найден шаблон: {center}')
    else:
        print(f'{__name__} Шаблон не найден')


# поиск шаблона на всем экране
def search_template_everywhere(step, context, template, w, h):
    """
    Ищет шаблон на всем экране.
    Скорость обработки - средняя.
    """
    img = screenshots.full_screenshot()

    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= step.get('threshold', 0.8))

    if loc[0].size > 0:
        pt = (loc[1][0], loc[0][0])
        center = (pt[0] + w // 2, pt[1] + h // 2)

        context[step['save_as']] = center
        print(f'{__name__} Найден шаблон: {center}')
    else:
        print(f'{__name__} Шаблон не найден')


# поиск шаблона по координатам
def search_template_by_coordinates(step, context, template, w, h):
    """
    Ищет шаблон по заданным пользователем координатам.
    Эффективный способ для нахождения шаблона
    когда заранее известны координаты. Например: кнопки.
    Скорость обработки - очень быстрая при размере шаблона ~ равном зоне поиска.
    """
    x_1, y_1, x_2, y_2 = step.get('coordinates', (0, 0, 1000, 1000))
    img = screenshots.screenshot_by_coordinates(x_1, y_1, x_2, y_2)

    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    loc_be = np.where(res >= step.get('threshold', 0.8))

    if loc_be[0].size > 0:
        # координаты в вырезанном изображении
        pt = (loc_be[1][0], loc_be[0][0])

        # координаты на полном экране
        screen_x = x_1 + pt[0]
        screen_y = y_1 + pt[1]
        center = (screen_x + w // 2, screen_y + h // 2)

        context[step['save_as']] = center
        print(f'{__name__} Найден шаблон: {center}')
    else:
        print(f'{__name__} Шаблон не найден')
