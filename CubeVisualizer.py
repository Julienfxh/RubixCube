from vpython import *
import random
from CUBE import *

scene.title = "Rubik Cube Test"
scene.width = 900
scene.height = 700
scene.background = color.gray(0.15)

CUBE_SIZE = 1.0
GAP = 0.06
OFFSET = CUBE_SIZE + GAP

BLACK  = vector(0.08, 0.08, 0.08)
WHITE  = vector(1, 1, 1)
YELLOW = vector(1, 1, 0)
RED    = vector(0.8, 0, 0)
ORANGE = vector(1, 0.5, 0)
GREEN  = vector(0, 0.7, 0)
BLUE   = vector(0, 0.2, 0.8)

COLORS = [WHITE, YELLOW, RED, ORANGE, GREEN, BLUE]

COLOR_MAP = {
    'W': WHITE,
    'Y': YELLOW,
    'R': RED,
    'O': ORANGE,
    'G': GREEN,
    'B': BLUE,
    'X': BLACK
}

def get_color(letter):
    return COLOR_MAP.get(letter.upper(), BLACK)


def create_visCubes(x,y,z,cube, size=CUBE_SIZE):
    pos_vec = vector(x * OFFSET, y * OFFSET, -z * OFFSET)

    body = box(
        pos=pos_vec,
        size=vector(size, size, size),
        color=BLACK
    )

    stickers = [None] * 6
    sticker_thickness = size * 0.08
    sticker_size = size * 0.88
    sticker_offset = size / 2 + sticker_thickness / 2 + 0.001

    if y==1:
        stickers[5] =box(
            pos=pos_vec + vector(0, sticker_offset, 0),
            size=vector(sticker_size, sticker_thickness, sticker_size),
            color= get_color(cube.cube[x+1,y+1,z+1][5])
        )

    if y == -1:
        stickers[4]=box(
            pos=pos_vec + vector(0, -sticker_offset, 0),
            size=vector(sticker_size, sticker_thickness, sticker_size),
            color=get_color(cube.cube[x+1,y+1,z+1][4])

        )

    if z == 1:
        stickers[3]=box(
            pos=pos_vec + vector(0, 0, -sticker_offset),
            size=vector(sticker_size, sticker_size, sticker_thickness),
            color=get_color(cube.cube[x+1,y+1,z+1][3])
        )

    if z == -1:
        stickers[1]=box(
            pos=pos_vec + vector(0, 0, sticker_offset),
            size=vector(sticker_size, sticker_size, sticker_thickness),
            color=get_color(cube.cube[x+1,y+1,z+1][1])
        )

    if x == 1:
        stickers[2]=box(
            pos=pos_vec + vector(sticker_offset, 0, 0),
            size=vector(sticker_thickness, sticker_size, sticker_size),
            color=get_color(cube.cube[x+1,y+1,z+1][2])
        )

    if x == -1:
        stickers[0]=box(
            pos=pos_vec + vector(-sticker_offset, 0, 0),
            size=vector(sticker_thickness, sticker_size, sticker_size),
            color=get_color(cube.cube[x+1,y+1,z+1][0])
        )

    return {
        "body": body,
        "stickers": stickers,
        "grid_pos": (x, y, z)
    }

# Erst Funktionen, dann Daten erzeugen
cubies = []
cube = Cube()
for x in [-1, 0, 1]:
    for y in [-1, 0, 1]:
        for z in [-1, 0, 1]:
           cubies.append(create_visCubes(x,y,z,cube))

def update_colors():
    print("E wurde gedrückt")
    for cubie in cubies:
        x = cubie["grid_pos"][0]
        y = cubie[("grid_pos")][1]
        z = cubie["grid_pos"][2]

        if y== 1:
            cubie["stickers"][5].color = get_color(cube.cube[x+1,y+1,z+1][5])

        if y == -1:
                cubie["stickers"][4].color = get_color(cube.cube[x+1,y+1,z+1][4])

        if z == 1:
                cubie["stickers"][3].color = get_color(cube.cube[x+1,y+1,z+1][3])

        if z==-1:
                cubie["stickers"][1].color = get_color(cube.cube[x+1,y+1,z+1][1])

        if x == 1:
                cubie["stickers"][2].color = get_color(cube.cube[x+1,y+1,z+1][2])

        if x == -1:
                cubie["stickers"][0].color = get_color(cube.cube[x+1,y+1,z+1][0])


def key_input(evt):
    print("Taste:", evt.key)
    if evt.key == "q":
        cube.rotateLeftBackwards()
    if evt.key == "w":
        cube.rotateTopLeft()
    if evt.key == "e":
        cube.rotateTopRight()
    if evt.key == "r":
        cube.rotateRightBackwards()
    if evt.key == "a":
        cube.rotateLeftForwards()
    if evt.key == "s":
        cube.rotateBottomLeft()
    if evt.key == "d":
        cube.rotateBottomRight()
    if evt.key == "f":
        cube.rotateRightForwards()
    if evt.key == "x":
        cube.rotateFrontRight()
    if evt.key == "y":
        cube.rotateFrontLeft()
    if evt.key == "c":
        cube.rotateBackLeft()
    if evt.key == "v":
        cube.rotateBackRight()
    update_colors()


scene.bind("keydown", key_input)

scene.forward = vector(-1, -1, -1)
scene.up = vector(0, 1, 0)

while True:
    rate(60)