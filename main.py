import yaml
from core import bot_modules
import time

"""
Основная логика находится в core/bot_modules/dynamic_bot.py
"""


def main():
    """
    Чтение файла config/name.yaml с "кодом" бота.
    Вызов наследника абстрактного класса
    и передача аргументов.
    """

    with open('config/test.yaml', 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)

    bot = bot_modules.dynamic_bot.DynamicBot(config)
    bot.run()


if __name__ == '__main__':
    x = time.time()
    main()
    print(time.time() - x)
