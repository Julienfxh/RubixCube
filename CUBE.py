from copy import deepcopy

import numpy as np

class Cube:
    def __init__(self):
        pass

    cube = np.empty((3,3,3),dtype=object)

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

        cube[2,2,2] = deepcopy(oldcube[2,0,1])
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

        cube[2,0,0] = deepcopy(oldcube[2,0,1])
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


def main():
    cube = Cube()
    for i in range(4):
      cube.rotateLeftBackwards()

    for i in range(4):
        cube.rotateLeftForwards()

    t = True
    cube2 = Cube()
    for i in range(3):
        for r in range(3):
            for z in range(3):
                if cube.cube[i,r,z]!=cube2.cube[i,r,z]:
                    t = False
    print(t)

if __name__ == "__main__":
    main()




