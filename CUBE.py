from copy import deepcopy
import random
import numpy as np

class Cube:
    def __init__(self):
        pass

    #in history get the last moves stored
    # 1 for rotateRightForwards -1 for rotateRightBackwords
    # 2 for rotateLeftForwards -2 for rotateLeftBackwords
    # 3 for rotateTopLeft -3 for rotateTopRight
    # 4 for rotateBottomLeft -4 for rotateBottomRight
    # 5 for rotateFrontLeft -5 for rotateFrontRight
    # 6 for rotateBackLeft -6 for rotateBackRight
    cube = np.empty((3, 3, 3), dtype=object)
    history = []

    #Cube erstellen 1.Farbe = rechts, 2. vorne, 3. links, 4. hinten, 5. unten 6. oben, X = DefaultFarbe
    # white side
    cube[0,0,0] = ['O','W','X','X','G','X']
    cube[1,0,0] = ['X','W','X','X','G','X']
    cube[2,0,0] = ['X','W','R','X','G','X']
    cube[0,1,0] = ['O','W','X','X','X','X']
    cube[1,1,0] = ['X','W','X','X','X','X']
    cube[2,1,0] = ['X','W','R','X','X','X']
    cube[0,2,0] = ['O','W','X','X','X','B']
    cube[1,2,0] = ['X','W','X','X','X','B']
    cube[2,2,0] = ['X','W','R','X','X','B']
    #orange side
    cube[0,0,2] = ['O','X','X','Y','G','X']
    cube[0,0,1] = ['O','X','X','X','G','X']
    cube[0,1,2] = ['O','X','X','Y','X','X']
    cube[0,1,1] = ['O','X','X','X','X','X']
    cube[0,2,2] = ['O','X','X','Y','X','B']
    cube[0,2,1] = ['O','X','X','X','X','B']
    #Red side
    cube[2,0,2] = ['X','X','R','Y','G','X']
    cube[2,0,1] = ['X','X','R','X','G','X']
    cube[2,1,2] = ['X','X','R','Y','X','X']
    cube[2,1,1] = ['X','X','R','X','X','X']
    cube[2,2,2] = ['X','X','R','Y','X','B']
    cube[2,2,1] = ['X','X','R','X','X','B']
    #Yellow side
    cube[1,0,2] = ['X','X','X','Y','G','X']
    cube[1,1,2] = ['X','X','X','Y','X','X']
    cube[1,2,2] = ['X','X','X','Y','X','B']
    #Green side
    cube[1,0,1] = ['X','X','X','X','G','X']
    #Blue side
    cube[1,2,1] = ['X','X','X','X','X','B']

    #forward ration at the right side from the Cube
    def rotateRightForwards(self):
        oldcube = deepcopy(self.cube)
        cube = deepcopy(self.cube)
        cube[2,0,2] = deepcopy(oldcube[2,0,0])
        cube[2,0,2][1] = oldcube[2,0,0][3]
        cube[2,0,2][3] = oldcube[2,0,0][4]
        cube[2,0,2][4] = oldcube[2,0,0][1]

        cube[2,0,1] = deepcopy(oldcube[2,1,0])
        cube[2,0,1][1] = oldcube[2,1,0][4]
        cube[2,0,1][4] = oldcube[2,1,0][1]

        cube[2,0,0] = deepcopy(oldcube[2,2,0])
        cube[2,0,0][4] = oldcube[2,2,0][1]
        cube[2,0,0][5] = oldcube[2,2,0][4]
        cube[2,0,0][1] = oldcube[2,2,0][5]

        cube[2,1,2] = deepcopy(oldcube[2,0,1])
        cube[2,1,2][3] = oldcube[2,0,1][4]
        cube[2,1,2][4] = oldcube[2,0,1][3]

        cube[2,1,0] = deepcopy(oldcube[2,2,1])
        cube[2,1,0][1] = oldcube[2,2,1][5]
        cube[2,1,0][5] = oldcube[2,2,1][1]

        cube[2,2,2] = deepcopy(oldcube[2,0,2])
        cube[2,2,2][3] = oldcube[2,0,2][4]
        cube[2,2,2][4] = oldcube[2,0,2][5]
        cube[2,2,2][5] = oldcube[2,0,2][3]

        cube[2,2,1] = deepcopy(oldcube[2,1,2])
        cube[2,2,1][3] = oldcube[2,1,2][5]
        cube[2,2,1][5] = oldcube[2,1,2][3]

        cube[2,2,0] = deepcopy(oldcube[2,2,2])
        cube[2,2,0][1] = oldcube[2,2,2][5]
        cube[2,2,0][3] = oldcube[2,2,2][1]
        cube[2,2,0][5] = oldcube[2,2,2][3]
        self.cube = cube
        self.history.append(1)

    #backwards rotation at the right side from the cube
    def rotateRightBackwards(self):
        oldcube = deepcopy(self.cube)
        cube = deepcopy(self.cube)

        cube[2,2,0] = deepcopy(oldcube[2,0,0])
        cube[2,2,0][1] = oldcube[2,0,0][4]
        cube[2,2,0][4] = oldcube[2,0,0][5]
        cube[2,2,0][5] = oldcube[2,0,0][1]

        cube[2,2,1] = deepcopy(oldcube[2,1,0])
        cube[2,2,1][1] = oldcube[2,1,0][5]
        cube[2,2,1][5] = oldcube[2,1,0][1]

        cube[2,2,2] = deepcopy(oldcube[2,2,0])
        cube[2,2,2][1] = oldcube[2,2,0][3]
        cube[2,2,2][3] = oldcube[2,2,0][5]
        cube[2,2,2][5] = oldcube[2,2,0][1]

        cube[2,1,0] = deepcopy(oldcube[2,0,1])
        cube[2,1,0][1] = oldcube[2,0,1][4]
        cube[2,1,0][4] = oldcube[2,0,1][1]

        cube[2,1,2] = deepcopy(oldcube[2,2,1])
        cube[2,1,2][3] = oldcube[2,2,1][5]
        cube[2,1,2][5] = oldcube[2,2,1][3]

        cube[2,0,0] = deepcopy(oldcube[2,0,2])
        cube[2,0,0][1] = oldcube[2,0,2][4]
        cube[2,0,0][4] = oldcube[2,0,2][3]
        cube[2,0,0][3] = oldcube[2,0,2][1]

        cube[2,0,1] = deepcopy(oldcube[2,1,2])
        cube[2,0,1][3] = oldcube[2,1,2][4]
        cube[2,0,1][4] = oldcube[2,1,2][3]

        cube[2,0,2] = deepcopy(oldcube[2,2,2])
        cube[2,0,2][3] = oldcube[2,2,2][5]
        cube[2,0,2][4] = oldcube[2,2,2][3]
        cube[2,0,2][5] = oldcube[2,2,2][4]
        self.cube = cube
        self.history.append(-1)


    #forward rotation at the left side from the cube
    def rotateLeftForwards(self):
        oldcube = deepcopy(self.cube)
        cube = deepcopy(self.cube)

        cube[0,0,2] = deepcopy(oldcube[0,0,0])
        cube[0,0,2][1] = oldcube[0,0,0][3]
        cube[0,0,2][3] = oldcube[0,0,0][4]
        cube[0,0,2][4] = oldcube[0,0,0][1]

        cube[0,0,1] = deepcopy(oldcube[0,1,0])
        cube[0,0,1][4] = oldcube[0,1,0][1]
        cube[0,0,1][1] = oldcube[0,1,0][4]

        cube[0,0,0] = deepcopy(oldcube[0,2,0])
        cube[0,0,0][1] = oldcube[0,2,0][5]
        cube[0,0,0][4] = oldcube[0,2,0][1]
        cube[0,0,0][5] = oldcube[0,2,0][4]

        cube[0,1,0] = deepcopy(oldcube[0,2,1])
        cube[0,1,0][5] = oldcube[0,2,1][1]
        cube[0,1,0][1] = oldcube[0,2,1][5]

        cube[0,2,0] = deepcopy(oldcube[0,2,2])
        cube[0,2,0][1] = oldcube[0,2,2][5]
        cube[0,2,0][3] = oldcube[0,2,2][1]
        cube[0,2,0][5] = oldcube[0,2,2][3]

        cube[0,1,2] = deepcopy(oldcube[0,0,1])
        cube[0,1,2][4] = oldcube[0,0,1][3]
        cube[0,1,2][3] = oldcube[0,0,1][4]

        cube[0,2,2] = deepcopy(oldcube[0,0,2])
        cube[0,2,2][3] = oldcube[0,0,2][4]
        cube[0,2,2][4] = oldcube[0,0,2][5]
        cube[0,2,2][5] = oldcube[0,0,2][3]

        cube[0,2,1] = deepcopy(oldcube[0,1,2])
        cube[0,2,1][5] = oldcube[0,1,2][3]
        cube[0,2,1][3] = oldcube[0,1,2][5]
        self.cube = cube
        self.history.append(2)

    #backward rotation at the left side from the cube
    def rotateLeftBackwards(self):
        oldcube = deepcopy(self.cube)
        cube = deepcopy(self.cube)

        cube[0,2,0] = deepcopy(oldcube[0,0,0])
        cube[0,2,0][1] = oldcube[0,0,0][4]
        cube[0,2,0][4] = oldcube[0,0,0][5]
        cube[0,2,0][5] = oldcube[0,0,0][1]

        cube[0,2,1] = deepcopy(oldcube[0,1,0])
        cube[0,2,1][5] = oldcube[0,1,0][1]
        cube[0,2,1][1] = oldcube[0,1,0][5]

        cube[0,2,2] = deepcopy(oldcube[0,2,0])
        cube[0,2,2][1] = oldcube[0,2,0][3]
        cube[0,2,2][3] = oldcube[0,2,0][5]
        cube[0,2,2][5] = oldcube[0,2,0][1]

        cube[0,1,2] = deepcopy(oldcube[0,2,1])
        cube[0,1,2][5] = oldcube[0,2,1][3]
        cube[0,1,2][3] = oldcube[0,2,1][5]

        cube[0,0,2] = deepcopy(oldcube[0,2,2])
        cube[0,0,2][3] = oldcube[0,2,2][5]
        cube[0,0,2][4] = oldcube[0,2,2][3]
        cube[0,0,2][5] = oldcube[0,2,2][4]

        cube[0,1,0] = deepcopy(oldcube[0,0,1])
        cube[0,1,0][4] = oldcube[0,0,1][1]
        cube[0,1,0][1] = oldcube[0,0,1][4]

        cube[0,0,0] = deepcopy(oldcube[0,0,2])
        cube[0,0,0][1] = oldcube[0,0,2][4]
        cube[0,0,0][3] = oldcube[0,0,2][1]
        cube[0,0,0][4] = oldcube[0,0,2][3]

        cube[0,0,1] = deepcopy(oldcube[0,1,2])
        cube[0,0,1][4] = oldcube[0,1,2][3]
        cube[0,0,1][3] = oldcube[0,1,2][4]
        self.cube = cube
        self.history.append(-2)

    #right rotation at the top of the cube
    def rotateTopRight(self):
        oldcube = deepcopy(self.cube)
        cube = deepcopy(self.cube)

        cube[2,2,0] = deepcopy(oldcube[0,2,0])
        cube[2,2,0][0] = oldcube[0,2,0][2]
        cube[2,2,0][1] = oldcube[0,2,0][0]
        cube[2,2,0][2] = oldcube[0,2,0][1]

        cube[2,2,1] = deepcopy(oldcube[1,2,0])
        cube[2,2,1][1] = oldcube[1,2,0][2]
        cube[2,2,1][2] = oldcube[1,2,0][1]

        cube[2,2,2] = deepcopy(oldcube[2,2,0])
        cube[2,2,2][1] = oldcube[2,2,0][3]
        cube[2,2,2][2] = oldcube[2,2,0][1]
        cube[2,2,2][3] = oldcube[2,2,0][2]

        cube[1,2,0] = deepcopy(oldcube[0,2,1])
        cube[1,2,0][0] = oldcube[0,2,1][1]
        cube[1,2,0][1] = oldcube[0,2,1][0]

        cube[1,2,2] = deepcopy(oldcube[2,2,1])
        cube[1,2,2][2] = oldcube[2,2,1][3]
        cube[1,2,2][3] = oldcube[2,2,1][2]

        cube[0,2,0] = deepcopy(oldcube[0,2,2])
        cube[0,2,0][0] = oldcube[0,2,2][3]
        cube[0,2,0][1] = oldcube[0,2,2][0]
        cube[0,2,0][3] = oldcube[0,2,2][1]

        cube[0,2,1] = deepcopy(oldcube[1,2,2])
        cube[0,2,1][3] = oldcube[1,2,2][0]
        cube[0,2,1][0] = oldcube[1,2,2][3]

        cube[0,2,2] = deepcopy(oldcube[2,2,2])
        cube[0,2,2][0] = oldcube[2,2,2][3]
        cube[0,2,2][2] = oldcube[2,2,2][0]
        cube[0,2,2][3] = oldcube[2,2,2][2]
        self.cube = cube
        self.history.append(-3)

    #left rotation at the top of the cube
    def rotateTopLeft(self):
        oldcube = deepcopy(self.cube)
        cube = deepcopy(self.cube)

        cube[0,2,2] = deepcopy(oldcube[0,2,0])
        cube[0,2,2][0] = oldcube[0,2,0][1]
        cube[0,2,2][1] = oldcube[0,2,0][3]
        cube[0,2,2][3] = oldcube[0,2,0][0]

        cube[0,2,1] = deepcopy(oldcube[1,2,0])
        cube[0,2,1][1] = oldcube[1,2,0][0]
        cube[0,2,1][0] = oldcube[1,2,0][1]

        cube[0,2,0] = deepcopy(oldcube[2,2,0])
        cube[0,2,0][0] = oldcube[2,2,0][1]
        cube[0,2,0][1] = oldcube[2,2,0][2]
        cube[0,2,0][2] = oldcube[2,2,0][0]

        cube[1,2,2] = deepcopy(oldcube[0,2,1])
        cube[1,2,2][0] = oldcube[0,2,1][3]
        cube[1,2,2][3] = oldcube[0,2,1][0]

        cube[1,2,0] = deepcopy(oldcube[2,2,1])
        cube[1,2,0][2] = oldcube[2,2,1][1]
        cube[1,2,0][1] = oldcube[2,2,1][2]

        cube[2,2,2] = deepcopy(oldcube[0,2,2])
        cube[2,2,2][0] = oldcube[0,2,2][2]
        cube[2,2,2][2] = oldcube[0,2,2][3]
        cube[2,2,2][3] = oldcube[0,2,2][0]

        cube[2,2,1] = deepcopy(oldcube[1,2,2])
        cube[2,2,1][3] = oldcube[1,2,2][2]
        cube[2,2,1][2] = oldcube[1,2,2][3]

        cube[2,2,0] = deepcopy(oldcube[2,2,2])
        cube[2,2,0][1] = oldcube[2,2,2][2]
        cube[2,2,0][2] = oldcube[2,2,2][3]
        cube[2,2,0][3] = oldcube[2,2,2][1]
        self.cube = cube
        self.history.append(3)

    #right rotation at the bottom from the cube
    def rotateBottomRight(self):
        oldcube = deepcopy(self.cube)
        cube = deepcopy(self.cube)

        cube[2,0,0] = deepcopy(oldcube[0,0,0])
        cube[2,0,0][0] = oldcube[0,0,0][2]
        cube[2,0,0][1] = oldcube[0,0,0][0]
        cube[2,0,0][2] = oldcube[0,0,0][1]

        cube[2,0,1] = deepcopy(oldcube[1,0,0])
        cube[2,0,1][1] = oldcube[1,0,0][2]
        cube[2,0,1][2] = oldcube[1,0,0][1]

        cube[2,0,2] = deepcopy(oldcube[2,0,0])
        cube[2,0,2][1] = oldcube[2,0,0][3]
        cube[2,0,2][2] = oldcube[2,0,0][1]
        cube[2,0,2][3] = oldcube[2,0,0][2]

        cube[1,0,0] = deepcopy(oldcube[0,0,1])
        cube[1,0,0][0] = oldcube[0,0,1][1]
        cube[1,0,0][1] = oldcube[0,0,1][0]

        cube[1,0,2] = deepcopy(oldcube[2,0,1])
        cube[1,0,2][2] = oldcube[2,0,1][3]
        cube[1,0,2][3] = oldcube[2,0,1][2]

        cube[0,0,0] = deepcopy(oldcube[0,0,2])
        cube[0,0,0][0] = oldcube[0,0,2][3]
        cube[0,0,0][1] = oldcube[0,0,2][0]
        cube[0,0,0][3] = oldcube[0,0,2][1]

        cube[0,0,1] = deepcopy(oldcube[1,0,2])
        cube[0,0,1][3] = oldcube[1,0,2][0]
        cube[0,0,1][0] = oldcube[1,0,2][3]

        cube[0,0,2] = deepcopy(oldcube[2,0,2])
        cube[0,0,2][0] = oldcube[2,0,2][3]
        cube[0,0,2][2] = oldcube[2,0,2][0]
        cube[0,0,2][3] = oldcube[2,0,2][2]
        self.cube = cube
        self.history.append(-4)

    #left rotation at the bottom of the cube
    def rotateBottomLeft(self):
        oldcube = deepcopy(self.cube)
        cube = deepcopy(self.cube)

        cube[0,0,2] = deepcopy(oldcube[0,0,0])
        cube[0,0,2][0] = oldcube[0,0,0][1]
        cube[0,0,2][1] = oldcube[0,0,0][3]
        cube[0,0,2][3] = oldcube[0,0,0][0]

        cube[0,0,1] = deepcopy(oldcube[1,0,0])
        cube[0,0,1][1] = oldcube[1,0,0][0]
        cube[0,0,1][0] = oldcube[1,0,0][1]

        cube[0,0,0] = deepcopy(oldcube[2,0,0])
        cube[0,0,0][0] = oldcube[2,0,0][1]
        cube[0,0,0][1] = oldcube[2,0,0][2]
        cube[0,0,0][2] = oldcube[2,0,0][0]

        cube[1,0,2] = deepcopy(oldcube[0,0,1])
        cube[1,0,2][0] = oldcube[0,0,1][3]
        cube[1,0,2][3] = oldcube[0,0,1][0]

        cube[1,0,0] = deepcopy(oldcube[2,0,1])
        cube[1,0,0][2] = oldcube[2,0,1][1]
        cube[1,0,0][1] = oldcube[2,0,1][2]

        cube[2,0,2] = deepcopy(oldcube[0,0,2])
        cube[2,0,2][0] = oldcube[0,0,2][2]
        cube[2,0,2][2] = oldcube[0,0,2][3]
        cube[2,0,2][3] = oldcube[0,0,2][0]

        cube[2,0,1] = deepcopy(oldcube[1,0,2])
        cube[2,0,1][3] = oldcube[1,0,2][2]
        cube[2,0,1][2] = oldcube[1,0,2][3]

        cube[2,0,0] = deepcopy(oldcube[2,0,2])
        cube[2,0,0][1] = oldcube[2,0,2][2]
        cube[2,0,0][2] = oldcube[2,0,2][3]
        cube[2,0,0][3] = oldcube[2,0,2][1]
        self.cube = cube
        self.history.append(4)

    #right roatation at the front from the cube
    def rotateFrontRight(self):
        oldcube = deepcopy(self.cube)
        cube = deepcopy(self.cube)

        cube[0,2,0] = deepcopy(oldcube[0,0,0])
        cube[0,2,0][0] = oldcube[0,0,0][4]
        cube[0,2,0][4] = oldcube[0,0,0][5]
        cube[0,2,0][5] = oldcube[0,0,0][0]

        cube[0,1,0] = deepcopy(oldcube[1,0,0])
        cube[0,1,0][0] = oldcube[1,0,0][4]
        cube[0,1,0][4] = oldcube[1,0,0][0]

        cube[0,0,0] = deepcopy(oldcube[2,0,0])
        cube[0,0,0][0] = oldcube[2,0,0][4]
        cube[0,0,0][2] = oldcube[2,0,0][0]
        cube[0,0,0][4] = oldcube[2,0,0][2]

        cube[1,2,0] = deepcopy(oldcube[0,1,0])
        cube[1,2,0][0] = oldcube[0,1,0][5]
        cube[1,2,0][5] = oldcube[0,1,0][0]

        cube[1,0,0] = deepcopy(oldcube[2,1,0])
        cube[1,0,0][2] = oldcube[2,1,0][4]
        cube[1,0,0][4] = oldcube[2,1,0][2]

        cube[2,2,0] = deepcopy(oldcube[0,2,0])
        cube[2,2,0][0] = oldcube[0,2,0][2]
        cube[2,2,0][2] = oldcube[0,2,0][5]
        cube[2,2,0][5] = oldcube[0,2,0][0]

        cube[2,1,0] = deepcopy(oldcube[1,2,0])
        cube[2,1,0][2] = oldcube[1,2,0][5]
        cube[2,1,0][5] = oldcube[1,2,0][2]

        cube[2,0,0] = deepcopy(oldcube[2,2,0])
        cube[2,0,0][2] = oldcube[2,2,0][5]
        cube[2,0,0][4] = oldcube[2,2,0][2]
        cube[2,0,0][5] = oldcube[2,2,0][4]
        self.cube = cube
        self.history.append(-5)

    #left rotation at the front of the cube
    def rotateFrontLeft(self):
        oldcube = deepcopy(self.cube)
        cube = deepcopy(self.cube)

        cube[2,0,0] = deepcopy(oldcube[0,0,0])
        cube[2,0,0][0] = oldcube[0,0,0][2]
        cube[2,0,0][2] = oldcube[0,0,0][4]
        cube[2,0,0][4] = oldcube[0,0,0][0]

        cube[2,1,0] = deepcopy(oldcube[1,0,0])
        cube[2,1,0][2] = oldcube[1,0,0][4]
        cube[2,1,0][4] = oldcube[1,0,0][2]

        cube[2,2,0] = deepcopy(oldcube[2,0,0])
        cube[2,2,0][2] = oldcube[2,0,0][4]
        cube[2,2,0][4] = oldcube[2,0,0][5]
        cube[2,2,0][5] = oldcube[2,0,0][2]

        cube[1,0,0] = deepcopy(oldcube[0,1,0])
        cube[1,0,0][0] = oldcube[0,1,0][4]
        cube[1,0,0][4] = oldcube[0,1,0][0]

        cube[1,2,0] = deepcopy(oldcube[2,1,0])
        cube[1,2,0][2] = oldcube[2,1,0][5]
        cube[1,2,0][5] = oldcube[2,1,0][2]

        cube[0,0,0] = deepcopy(oldcube[0,2,0])
        cube[0,0,0][0] = oldcube[0,2,0][5]
        cube[0,0,0][4] = oldcube[0,2,0][0]
        cube[0,0,0][5] = oldcube[0,2,0][4]

        cube[0,1,0] = deepcopy(oldcube[1,2,0])
        cube[0,1,0][0] = oldcube[1,2,0][5]
        cube[0,1,0][5] = oldcube[1,2,0][0]

        cube[0,2,0] = deepcopy(oldcube[2,2,0])
        cube[0,2,0][0] = oldcube[2,2,0][5]
        cube[0,2,0][2] = oldcube[2,2,0][0]
        cube[0,2,0][5] = oldcube[2,2,0][2]
        self.cube = cube
        self.history.append(5)


    #right rotation at the back of the cube
    def rotateBackRight(self):
        oldcube = deepcopy(self.cube)
        cube = deepcopy(self.cube)

        cube[0,2,2] = deepcopy(oldcube[0,0,2])
        cube[0,2,2][0] = oldcube[0,0,2][4]
        cube[0,2,2][4] = oldcube[0,0,2][5]
        cube[0,2,2][5] = oldcube[0,0,2][0]

        cube[0,1,2] = deepcopy(oldcube[1,0,2])
        cube[0,1,2][0] = oldcube[1,0,2][4]
        cube[0,1,2][4] = oldcube[1,0,2][0]

        cube[0,0,2] = deepcopy(oldcube[2,0,2])
        cube[0,0,2][0] = oldcube[2,0,2][4]
        cube[0,0,2][2] = oldcube[2,0,2][0]
        cube[0,0,2][4] = oldcube[2,0,2][2]

        cube[1,2,2] = deepcopy(oldcube[0,1,2])
        cube[1,2,2][0] = oldcube[0,1,2][5]
        cube[1,2,2][5] = oldcube[0,1,2][0]

        cube[1,0,2] = deepcopy(oldcube[2,1,2])
        cube[1,0,2][2] = oldcube[2,1,2][4]
        cube[1,0,2][4] = oldcube[2,1,2][2]

        cube[2,2,2] = deepcopy(oldcube[0,2,2])
        cube[2,2,2][0] = oldcube[0,2,2][2]
        cube[2,2,2][2] = oldcube[0,2,2][5]
        cube[2,2,2][5] = oldcube[0,2,2][0]

        cube[2,1,2] = deepcopy(oldcube[1,2,2])
        cube[2,1,2][2] = oldcube[1,2,2][5]
        cube[2,1,2][5] = oldcube[1,2,2][2]

        cube[2,0,2] = deepcopy(oldcube[2,2,2])
        cube[2,0,2][2] = oldcube[2,2,2][5]
        cube[2,0,2][4] = oldcube[2,2,2][2]
        cube[2,0,2][5] = oldcube[2,2,2][4]
        self.cube = cube
        self.history.append(-6)

    #left rotation at the back of the cube
    def rotateBackLeft(self):
        oldcube = deepcopy(self.cube)
        cube = deepcopy(self.cube)

        cube[2,0,2] = deepcopy(oldcube[0,0,2])
        cube[2,0,2][0] = oldcube[0,0,2][2]
        cube[2,0,2][2] = oldcube[0,0,2][4]
        cube[2,0,2][4] = oldcube[0,0,2][0]

        cube[2,1,2] = deepcopy(oldcube[1,0,2])
        cube[2,1,2][2] = oldcube[1,0,2][4]
        cube[2,1,2][4] = oldcube[1,0,2][2]

        cube[2,2,2] = deepcopy(oldcube[2,0,2])
        cube[2,2,2][2] = oldcube[2,0,2][4]
        cube[2,2,2][4] = oldcube[2,0,2][5]
        cube[2,2,2][5] = oldcube[2,0,2][2]

        cube[1,0,2] = deepcopy(oldcube[0,1,2])
        cube[1,0,2][0] = oldcube[0,1,2][4]
        cube[1,0,2][4] = oldcube[0,1,2][0]

        cube[1,2,2] = deepcopy(oldcube[2,1,2])
        cube[1,2,2][2] = oldcube[2,1,2][5]
        cube[1,2,2][5] = oldcube[2,1,2][2]

        cube[0,0,2] = deepcopy(oldcube[0,2,2])
        cube[0,0,2][0] = oldcube[0,2,2][5]
        cube[0,0,2][4] = oldcube[0,2,2][0]
        cube[0,0,2][5] = oldcube[0,2,2][4]

        cube[0,1,2] = deepcopy(oldcube[1,2,2])
        cube[0,1,2][0] = oldcube[1,2,2][5]
        cube[0,1,2][5] = oldcube[1,2,2][0]

        cube[0,2,2] = deepcopy(oldcube[2,2,2])
        cube[0,2,2][0] = oldcube[2,2,2][5]
        cube[0,2,2][2] = oldcube[2,2,2][0]
        cube[0,2,2][5] = oldcube[2,2,2][2]
        self.cube = cube
        self.history.append(6)

    def randomMoves(self, x):
        while x:
            i = random.randint(-6, 6)
            while i == 0:
              i = random.randint(-6, 6)
            if i == -1:
                self.rotateRightBackwards()
            if i == 1:
                self.rotateRightForwards()
            if i == -2:
                self.rotateLeftBackwards()
            if i == 2:
                self.rotateLeftForwards()
            if i == -3:
                self.rotateTopRight()
            if i == 3:
                self.rotateTopLeft()
            if i == -4:
                self.rotateBottomRight()
            if i == 4:
                self.rotateBottomLeft()
            if i == -5:
                self.rotateFrontRight()
            if i == 5:
                self.rotateFrontLeft()
            if i == -6:
                self.rotateBackRight()
            if i == 6:
                self.rotateBackLeft()
            x = x-1


def main():
    cube = Cube()
    cube.whiteCross()

if __name__ == "__main__":
    main()










