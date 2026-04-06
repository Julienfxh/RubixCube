import time
class Solver:
    def __init__(self, cube):
        self.cube = cube

    def solveWithHistory(self, visualizer = None):
        for i in reversed(self.cube.history):
            if i == 1:
                self.cube.rotateRightBackwards()
            if i == -1:
                self.cube.rotateRightForwards()
            if i == 2:
                self.cube.rotateLeftBackwards()
            if i == -2:
                self.cube.rotateLeftForwards()
            if i == 3:
                self.cube.rotateTopRight()
            if i == -3:
                self.cube.rotateTopLeft()
            if i == 4:
                self.cube.rotateBottomRight()
            if i == -4:
                self.cube.rotateBottomLeft()
            if i == 5:
                self.cube.rotateFrontRight()
            if i == -5:
                self.cube.rotateFrontLeft()
            if i == 6:
                self.cube.rotateBackRight()
            if i == -6:
                self.cube.rotateBackLeft()
            visualizer.update_colors()
            time.sleep(0.5)
        self.cube.history = []


