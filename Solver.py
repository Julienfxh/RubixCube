import time
import numpy as np
from solverhelper.WhiteCross import whiteCross

class Solver:
    def __init__(self, cube):
        self.cube = cube

    #does a specific rotation
    def do(self, name, visualizer=None):
        getattr(self.cube, name)()
        if visualizer is not None:
            visualizer.update_colors()
        time.sleep(0.5)

    #does a specific rotation n times
    def doNTimes(self, name, visualizer=None, n=2):
        for i in range(n):
            self.do(name, visualizer)

    #inverts all moves
    def solveWithHistory(self, visualizer = None):
        for i in reversed(self.cube.history):
            if i == 1:
                self.do("rotateRightBackwards",visualizer)
            if i == -1:
                self.do("rotateRightForwards",visualizer)
            if i == 2:
                self.do("rotateLeftBackwards",visualizer)
            if i == -2:
                self.do("rotateLeftForwards",visualizer)
            if i == 3:
                self.do("rotateTopRight",visualizer)
            if i == -3:
                self.do("rotateTopLeft",visualizer)
            if i == 4:
                self.do("rotateBottomRight",visualizer)
            if i == -4:
                self.do("rotateBottomLeft",visualizer)
            if i == 5:
                self.do("rotateFrontRight",visualizer)
            if i == -5:
                self.do("rotateFrontLeft",visualizer)
            if i == 6:
                self.do("rotateBackRight",visualizer)
            if i == -6:
                self.do("rotateBackLeft",visualizer)
        self.cube.history = []

    #checks where the psoition from a cubie is with only this two visible Colors
    def isTwoSidedCubie(self,cube,color1,color2):
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    piece = np.asarray(cube.cube[x, y, z]).flatten()

                    if np.count_nonzero(piece == color1) == 1 and \
                            np.count_nonzero(piece == color2) == 1 and \
                            np.count_nonzero(piece == 'X') == 4:
                        return x, y, z
        return None

    def solve(self,visualizer):
        whiteCross(self,visualizer)
