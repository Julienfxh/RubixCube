import time
import numpy as np
from solverhelper.WhiteCross import whiteCross
from solverhelper.WhiteCorners import whiteCorners
from solverhelper.Middle import middle
from solverhelper.YellowCross import yellowCross
from solverhelper.YellowCorners import yellowCorners

class Solver:
    def __init__(self, cube):
        self.cube = cube

    #does a specific rotation
    def do(self, name, visualizer=None):
        getattr(self.cube, name)()
        if visualizer is not None:
            visualizer.update_colors()
        time.sleep(0.05)

    #does a specific rotation n times
    def doNTimes(self, name, visualizer=None, n=2):
        for i in range(n):
            self.do(name, visualizer)

    def solveWithHistory(self, visualizer=None):
        move_map = {
            1: "rotateRightBackwards",
            -1: "rotateRightForwards",
            2: "rotateLeftBackwards",
            -2: "rotateLeftForwards",
            3: "rotateTopRight",
            -3: "rotateTopLeft",
            4: "rotateBottomRight",
            -4: "rotateBottomLeft",
            5: "rotateFrontRight",
            -5: "rotateFrontLeft",
            6: "rotateBackRight",
            -6: "rotateBackLeft",
        }

        for move in reversed(self.cube.history):
          action = move_map.get(move)
          if action:
            self.do(action, visualizer)

        self.cube.history = []

    #checks where the position from a cubie is with only this two visible Colors
    def isSidedCubie(self,cube, color1, color2, color3=None):
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    piece = np.asarray(cube.cube[x, y, z]).flatten()

                    if color3 is not None:
                        if np.count_nonzero(piece == color1) == 1 and \
                                np.count_nonzero(piece == color2) == 1 and \
                                np.count_nonzero(piece == color3) == 1 and \
                                np.count_nonzero(piece == 'X') == 3:
                            return x, y, z
                    else:
                        if np.count_nonzero(piece == color1) == 1 and \
                                np.count_nonzero(piece == color2) == 1 and \
                                np.count_nonzero(piece == 'X') == 4:
                            return x, y, z
        return None

    #function that get called by the visualizer
    def solve(self,visualizer):
        whiteCross(self,visualizer)
        whiteCorners(self,visualizer)
        middle(self,visualizer)
        yellowCross(self,visualizer)
        yellowCorners(self,visualizer)
