from vpython import *


class Visualizer:
    def __init__(self, cube, solver):
        self.cube = cube
        self.solver = solver

        scene.title = "Rubik Cube Test"
        scene.width = 900
        scene.height = 700
        scene.background = color.gray(0.15)

        self.CUBE_SIZE = 1.0
        self.GAP = 0.06
        self.OFFSET = self.CUBE_SIZE + self.GAP

        self.BLACK = vector(0.08, 0.08, 0.08)
        self.WHITE = vector(1, 1, 1)
        self.YELLOW = vector(1, 1, 0)
        self.RED = vector(0.8, 0, 0)
        self.ORANGE = vector(1, 0.5, 0)
        self.GREEN = vector(0, 0.7, 0)
        self.BLUE = vector(0, 0.2, 0.8)

        self.COLOR_MAP = {
            "W": self.WHITE,
            "Y": self.YELLOW,
            "R": self.RED,
            "O": self.ORANGE,
            "G": self.GREEN,
            "B": self.BLUE,
            "X": self.BLACK
        }

        self.cubies = []
        self.create_all_cubies()

    def get_color(self, letter):
        return self.COLOR_MAP.get(letter.upper(), self.BLACK)

    def create_vis_cube(self, x, y, z):
        pos_vec = vector(x * self.OFFSET, y * self.OFFSET, -z * self.OFFSET)

        body = box(
            pos=pos_vec,
            size=vector(self.CUBE_SIZE, self.CUBE_SIZE, self.CUBE_SIZE),
            color=self.BLACK
        )

        stickers = [None] * 6
        sticker_thickness = self.CUBE_SIZE * 0.08
        sticker_size = self.CUBE_SIZE * 0.88
        sticker_offset = self.CUBE_SIZE / 2 + sticker_thickness / 2 + 0.001

        if y == 1:
            stickers[5] = box(
                pos=pos_vec + vector(0, sticker_offset, 0),
                size=vector(sticker_size, sticker_thickness, sticker_size),
                color=self.get_color(self.cube.cube[x + 1, y + 1, z + 1][5])
            )

        if y == -1:
            stickers[4] = box(
                pos=pos_vec + vector(0, -sticker_offset, 0),
                size=vector(sticker_size, sticker_thickness, sticker_size),
                color=self.get_color(self.cube.cube[x + 1, y + 1, z + 1][4])
            )

        if z == 1:
            stickers[3] = box(
                pos=pos_vec + vector(0, 0, -sticker_offset),
                size=vector(sticker_size, sticker_size, sticker_thickness),
                color=self.get_color(self.cube.cube[x + 1, y + 1, z + 1][3])
            )

        if z == -1:
            stickers[1] = box(
                pos=pos_vec + vector(0, 0, sticker_offset),
                size=vector(sticker_size, sticker_size, sticker_thickness),
                color=self.get_color(self.cube.cube[x + 1, y + 1, z + 1][1])
            )

        if x == 1:
            stickers[2] = box(
                pos=pos_vec + vector(sticker_offset, 0, 0),
                size=vector(sticker_thickness, sticker_size, sticker_size),
                color=self.get_color(self.cube.cube[x + 1, y + 1, z + 1][2])
            )

        if x == -1:
            stickers[0] = box(
                pos=pos_vec + vector(-sticker_offset, 0, 0),
                size=vector(sticker_thickness, sticker_size, sticker_size),
                color=self.get_color(self.cube.cube[x + 1, y + 1, z + 1][0])
            )

        return {
            "body": body,
            "stickers": stickers,
            "grid_pos": (x, y, z)
        }

    def create_all_cubies(self):
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                for z in [-1, 0, 1]:
                    self.cubies.append(self.create_vis_cube(x, y, z))

    def update_colors(self):
        for cubie in self.cubies:
            x = cubie["grid_pos"][0]
            y = cubie["grid_pos"][1]
            z = cubie["grid_pos"][2]

            if y == 1:
                cubie["stickers"][5].color = self.get_color(self.cube.cube[x + 1, y + 1, z + 1][5])

            if y == -1:
                cubie["stickers"][4].color = self.get_color(self.cube.cube[x + 1, y + 1, z + 1][4])

            if z == 1:
                cubie["stickers"][3].color = self.get_color(self.cube.cube[x + 1, y + 1, z + 1][3])

            if z == -1:
                cubie["stickers"][1].color = self.get_color(self.cube.cube[x + 1, y + 1, z + 1][1])

            if x == 1:
                cubie["stickers"][2].color = self.get_color(self.cube.cube[x + 1, y + 1, z + 1][2])

            if x == -1:
                cubie["stickers"][0].color = self.get_color(self.cube.cube[x + 1, y + 1, z + 1][0])

    def key_input(self, evt):
        print("Taste:", evt.key)

        if evt.key == "q":
            self.cube.rotateLeftBackwards()
        if evt.key == "w":
            self.cube.rotateTopLeft()
        if evt.key == "e":
            self.cube.rotateTopRight()
        if evt.key == "r":
            self.cube.rotateRightBackwards()
        if evt.key == "a":
            self.cube.rotateLeftForwards()
        if evt.key == "s":
            self.cube.rotateBottomLeft()
        if evt.key == "d":
            self.cube.rotateBottomRight()
        if evt.key == "f":
            self.cube.rotateRightForwards()
        if evt.key == "x":
            self.cube.rotateFrontRight()
        if evt.key == "y":
            self.cube.rotateFrontLeft()
        if evt.key == "c":
            self.cube.rotateBackLeft()
        if evt.key == "v":
            self.cube.rotateBackRight()
        if evt.key == "o":
            self.solver.solveWithHistory(self)
        if evt.key == "1":
            self.cube.randomMoves(10)
        if evt.key == "2":
            self.solver.solve(self)

        self.update_colors()

    def run(self):
        scene.bind("keydown", self.key_input)

        scene.forward = vector(-1, -1, -1)
        scene.up = vector(0, 1, 0)

        self.update_colors()

        while True:
            rate(60)