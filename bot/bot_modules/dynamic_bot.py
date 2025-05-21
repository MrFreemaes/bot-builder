from .base_bot import BaseBot
from bot.bot_parts import search_template, mouse_clicks

ACTIONS = {
    'search_template': search_template.search_template,
    'click': mouse_clicks.click_on_coordinates
}


class DynamicBot(BaseBot):
    def run(self):
        steps = self.config['steps']
        context = {}

        for step in steps:
            action = step['action']
            func = ACTIONS.get(action)
            if func:
                func(step, context)
            else:
                print(f'Неизвестное действие {action}')
