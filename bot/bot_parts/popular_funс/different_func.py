import time


def time_sleep(step, context):
    pause_time = step.get('pause_time', 1)
    time.sleep(pause_time)
    print(f'{__name__} Выполнение остановлено на {pause_time} сек.')
