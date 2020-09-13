# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (600, 600)
# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall
from snowfall import create_snowflakes, color_of_snowflakes, step, fallen_snowflakes, delete_snowflakes
# создать_снежинки(N)
create_snowflakes(10)
while True:
    sd.start_drawing()

    color_of_snowflakes(color=sd.background_color)
    #  нарисовать_снежинки_цветом(color=sd.background_color)
    step()
    #  сдвинуть_снежинки()
    color_of_snowflakes(color=sd.COLOR_WHITE)
    #  нарисовать_снежинки_цветом(color)
    out_snowflakes = fallen_snowflakes()
    if out_snowflakes:
        delete_snowflakes(out_snowflakes)
        create_snowflakes(len(out_snowflakes))
    #  если есть номера_достигших_низа_экрана() то
    #       удалить_снежинки(номера)
    #       создать_снежинки(count)
    # create_snowflakes(1)
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
