import yaml
from bot import bot_modules
import time


def main():
    with open('config/test.yaml', 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)

    bot = bot_modules.dynamic_bot.DynamicBot(config)
    bot.run()


if __name__ == '__main__':
    x = time.time()
    main()
    print(time.time() - x)
