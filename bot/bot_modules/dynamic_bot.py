from .base_bot import BaseBot
from bot.bot_parts import search_template, mouse_clicks

ACTIONS = {
    'search_template': search_template.search_template,
    'click': mouse_clicks.click,
    'moveto_and_click': mouse_clicks.moveto_and_click,
    # 'time_sleep': ''
}


class DynamicBot(BaseBot):
    def run(self):
        steps = self.config['steps']
        context = {}

        for step in steps:
            self.execute_step(step, context)

    def execute_step(self, step, context):
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
        inner_steps = step.get('steps', [])
        print(f'{__name__} Запуск бесконечного цикла')
        while True:
            for inner_step in inner_steps:
                self.execute_step(inner_step, context)

    def loop_until_found(self, step, context):
        key_to_check = step.get('exit_if')
        context[key_to_check] = None  # одно из решений зацикливания
        inner_steps = step.get('steps', [])

        print(f'{__name__} Запуск цикла до нахождения ключа: {key_to_check}')
        while True:
            # условие выхода
            if key_to_check and context.get(key_to_check):
                print(f'{__name__} Ключ найден в контексте — выход из цикла')
                break

            for inner_step in inner_steps:
                self.execute_step(inner_step, context)
