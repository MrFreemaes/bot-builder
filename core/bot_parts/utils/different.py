import time

"""
Модуль с функциями не относящимся к определенному типу например как mouse_clicks.py
"""


def time_sleep(step, context):
    """
    Вызывается через config.
    Останавливает программу на указанное в pause_time секунд.
    """
    pause_time = step.get('pause_time', 1)
    time.sleep(pause_time)
    print(f'{__name__} Выполнение остановлено на {pause_time} сек.')
