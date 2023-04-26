# -*- coding: utf-8 -*-
import random
import time

from sh import redshift
import schedule


# @click.command()
# @click.option('--count', default=1, help='Number of greetings.')
# def test(count):
#     print('hello world')
#     print(count)
UPDATE_INTERVAL = 5


def get_valid_gamma():
    base = random.randint(8, 12)
    return base / 10


def update_color():
    colors = ['{:.2f}'.format(get_valid_gamma()) for _ in range(3)]
    redshift(g=':'.join(colors), o=True)


def loop():
    random.seed()
    update_color()
    schedule.every(UPDATE_INTERVAL).minutes.do(update_color)
    while True:
        schedule.run_pending()
        time.sleep(0.1)
