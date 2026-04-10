from vpython import *


class Visualizer:
    def __init__(self, cube, solver):
        self.cube = cube
        self.solver = solver

        scene.title = "Rubik Cube Solver"
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
        self.create_ui()

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
            x, y, z = cubie["grid_pos"]

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

    def create_ui(self):
        scene.append_to_caption("\nControl")
        scene.append_to_caption(" " * 40)
        scene.append_to_caption("Keybinding\n\n")

        button(text="Q", bind=lambda _: self.do_action("q"))
        scene.append_to_caption(" ")
        button(text="W", bind=lambda _: self.do_action("w"))
        scene.append_to_caption(" ")
        button(text="E", bind=lambda _: self.do_action("e"))
        scene.append_to_caption(" ")
        button(text="R", bind=lambda _: self.do_action("r"))
        scene.append_to_caption(" " * 20 + "Q/A = Left\n")

        button(text="A", bind=lambda _: self.do_action("a"))
        scene.append_to_caption(" ")
        button(text="S", bind=lambda _: self.do_action("s"))
        scene.append_to_caption(" ")
        button(text="D", bind=lambda _: self.do_action("d"))
        scene.append_to_caption(" ")
        button(text="F", bind=lambda _: self.do_action("f"))
        scene.append_to_caption(" " * 20 + "W/E = Top\n")

        button(text="X", bind=lambda _: self.do_action("x"))
        scene.append_to_caption(" ")
        button(text="Y", bind=lambda _: self.do_action("y"))
        scene.append_to_caption(" ")
        button(text="C", bind=lambda _: self.do_action("c"))
        scene.append_to_caption(" ")
        button(text="V", bind=lambda _: self.do_action("v"))
        scene.append_to_caption(" " * 20 + "S/D = Bottom\n\n")

        button(text="Solve with History", bind=lambda _: self.do_action("o"))
        scene.append_to_caption(" ")
        button(text="Solve", bind=lambda _: self.do_action("2"))
        scene.append_to_caption(" " * 10 + "R/F = Right\n\n")

        scene.append_to_caption("Random Moves ")
        button(text="10", bind=lambda _: self.random_moves(10))
        scene.append_to_caption(" ")
        button(text="100", bind=lambda _: self.random_moves(100))
        scene.append_to_caption(" ")
        button(text="1000", bind=lambda _: self.random_moves(1000))
        scene.append_to_caption(" " * 5 + "X/Y = Front\n")

        scene.append_to_caption(" " * 45 + "C/V = Back\n")
        scene.append_to_caption(" " * 45 + "O = Solve with History\n")
        scene.append_to_caption(" " * 45 + "1 = Random | 2 = Solve\n\n")


    def do_action(self, key):
        if key == "q":
            self.cube.rotateLeftBackwards()
        elif key == "w":
            self.cube.rotateTopLeft()
        elif key == "e":
            self.cube.rotateTopRight()
        elif key == "r":
            self.cube.rotateRightBackwards()
        elif key == "a":
            self.cube.rotateLeftForwards()
        elif key == "s":
            self.cube.rotateBottomLeft()
        elif key == "d":
            self.cube.rotateBottomRight()
        elif key == "f":
            self.cube.rotateRightForwards()
        elif key == "x":
            self.cube.rotateFrontRight()
        elif key == "y":
            self.cube.rotateFrontLeft()
        elif key == "c":
            self.cube.rotateBackLeft()
        elif key == "v":
            self.cube.rotateBackRight()
        elif key == "o":
            self.solver.solveWithHistory(self)
        elif key == "1":
            self.cube.randomMoves(10)
        elif key == "2":
            self.solver.solve(self)

        self.update_colors()

    def random_moves(self, amount):
        self.cube.randomMoves(amount)
        self.update_colors()

    def key_input(self, evt):
        self.do_action(evt.key.lower())

    def run(self):
        scene.bind("keydown", self.key_input)

        scene.forward = vector(-1, -1, -1)
        scene.up = vector(0, 1, 0)

        self.update_colors()

        while True:
            rate(60)