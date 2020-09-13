# -*- coding: utf-8 -*-

import simple_draw as sd
points = []
lengths = []

def create_snowflakes(count):
    for point in range(count):
        points.append(sd.get_point(sd.random_number(0, 600), 600))
        lengths.append(sd.random_number(10, 40))


def color_of_snowflakes(color):
    for snowflake in points:
        center = snowflake
        length = lengths[points.index(center)]
        sd.snowflake(center=center, length=length, color=color)


def step():
    for snowflake in points:
        snowflake.y -= sd.random_number(1, 10)
        snowflake.x += sd.random_number(-10, 10)


def fallen_snowflakes():
    fslist = []
    for n in points:
        if n.y <= -40:
            fslist.append(points.index(n))
        elif n.x <= -40:
            fslist.append(points.index(n))
        elif n.x >= 640:
            fslist.append(points.index(n))
    return fslist


def delete_snowflakes(fslist):
    for n in fslist:
        points.pop(n)
        lengths.pop(n)

