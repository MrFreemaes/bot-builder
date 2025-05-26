from .base_bot import BaseBot
from bot.bot_parts import search_template, mouse_clicks, keyboard_press
from bot.bot_parts.popular_funс import different

"""Функции для вызова по имени заданном в config/name.yaml"""
ACTIONS = {
    'search_template': search_template.search_template,
    'mouse_action': mouse_clicks.mouse_actions,
    'keyboard_action': keyboard_press.keyboard_action,
    'time_sleep': different.time_sleep,
    # '': ''
}


class DynamicBot(BaseBot):
    """
    Основной блок. Распределение и выполнение всех функций.
    Принимает значения из config/name.yaml.
    """

    def run(self):
        """
        Обязательный метод для выполнения.
        Вызывает метод execute_step() если есть блоки step в config.
        """
        steps = self.config['steps']
        context = {}

        for step in steps:
            self.execute_step(step, context)

    def execute_step(self, step, context):
        """
        Метод определяет функцию по названию
        и обращается к соответствующему методу
        передавая все аргументы и вложенные функции.
        """
        action = step.get('action')

        if action == 'loop_forever':
            self.loop_forever(step, context)
        elif action == 'loop_until_found':
            self.loop_until_found(step, context)
        else:
            func = ACTIONS.get(action)
            if func:
                func(step, context)
            else:
                print(f'{__name__} Неизвестное действие: {action}')

    def loop_forever(self, step, context):
        """
        Бесконечный цикл.
        Определяется в config как: - action: loop_forever
                                     steps:
        Выполняет все вложенные в steps функции пока не будет отключен пользователем.
        """
        inner_steps = step.get('steps', [])
        print(f'{__name__} Запуск бесконечного цикла')
        while True:
            for inner_step in inner_steps:
                self.execute_step(inner_step, context)

    def loop_until_found(self, step, context):
        """
        Основной метод для поиска шаблона.
        Ищет шаблон пока он не будет найден.
        Выходит из цикла при нахождении шаблона.
        """
        key_to_check = step.get('exit_if')
        context[key_to_check] = None  # одно из решений зацикливания при повторном применении функции
        inner_steps = step.get('steps', [])

        print(f'{__name__} Запуск цикла до нахождения ключа: {key_to_check}')
        while True:
            # условие выхода
            if key_to_check and context.get(key_to_check):
                print(f'{__name__} Ключ найден в контексте — выход из цикла')
                break

            for inner_step in inner_steps:
                self.execute_step(inner_step, context)
