import cv2
import numpy as np
from bot.bot_parts.popular_funс import screenshots, mouse_actions


def search_template(step, context):
    template = cv2.imread(step['template_path'], cv2.IMREAD_GRAYSCALE)
    w, h = template.shape[::-1]

    # смотрит какой скриншот делать (можно добавлять)
    stype = step.get('screenshot_type', 'full_screen')
    if stype == 'around_mouse':
        search_pattern_around_mouse(step, context, template, w, h)
    else:
        search_template_everywhere(step, context, template, w, h)


# поиск шаблона вокруг мышки
def search_pattern_around_mouse(step, context, template, w, h):
    mouse_x, mouse_y = mouse_actions.mouse_coordinates()
    radius = step.get('radius', 300)
    img = screenshots.screen_of_mause(radius, mouse_x, mouse_y)

    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    loc_be = np.where(res >= step.get('threshold', 0.7))

    top_left_x = mouse_x - radius
    top_left_y = mouse_y - radius

    if loc_be[0].size > 0:
        # координаты в вырезанном изображении
        pt = (loc_be[1][0], loc_be[0][0])

        # координаты в пределах полного экрана
        screen_x = top_left_x + pt[0]
        screen_y = top_left_y + pt[1]
        center = (screen_x + w // 2, screen_y + h // 2)

        context[step['save_as']] = center
        print(f'{__name__} Найден шаблон: {center}')
    else:
        print(f'{__name__} Шаблон не найден')


# поиск шаблона на всем экране
def search_template_everywhere(step, context, template, w, h):
    img = screenshots.full_screen()

    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= step.get('threshold', 0.7))

    if loc[0].size > 0:
        pt = (loc[1][0], loc[0][0])
        center = (pt[0] + w // 2, pt[1] + h // 2)
        context[step['save_as']] = center
        print(f'{__name__} Найден шаблон: {center}')
    else:
        print(f'{__name__} Шаблон не найден')
