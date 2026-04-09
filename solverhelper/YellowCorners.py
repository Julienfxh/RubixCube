def checkCornerBlueRedYellow(solver):
    x,y,z = solver.isSidedCubie(solver.cube,'B','Y','R')
    if(x == 2 and y == 2 and z == 2):
        return True
    return False

def checkCornerBlueOrangeYellow(solver):
    x,y,z = solver.isSidedCubie(solver.cube,'B','Y','O')
    if(x == 0 and y == 2 and z == 2):
        return True
    return False

def checkCornerGreenOrangeYellow(solver):
    x,y,z = solver.isSidedCubie(solver.cube,'G','Y','O')
    if(x == 0 and y == 0 and z == 2):
        return True
    return False

def checkCornerGreenRedYellow(solver):
    x,y,z = solver.isSidedCubie(solver.cube,'G','Y','R')
    if(x == 2 and y == 0 and z == 2):
        return True
    return False

def checkAllCorners(solver):
    if checkCornerBlueRedYellow(solver) and checkCornerGreenRedYellow(solver) and checkCornerGreenOrangeYellow(solver) and \
            checkCornerBlueOrangeYellow(solver):
        return True
    return False

def isOneCornerRight(solver):
    if checkCornerBlueRedYellow(solver) or checkCornerGreenRedYellow(solver) or checkCornerGreenOrangeYellow(solver) or \
            checkCornerBlueOrangeYellow(solver):
        return True
    return False

#brings the yellow corners in the right position
def bringYellowCornersInRightPosition(solver, visualizer=None):

    #if no corner is right
    if(isOneCornerRight(solver)==False):

        for i in range(3):
            solver.do("rotateBackLeft",visualizer)
            solver.do("rotateRightBackwards",visualizer)
            solver.do("rotateBackRight",visualizer)
            solver.do("rotateRightForwards",visualizer)

        for i in range(3):
            solver.do("rotateBackRight",visualizer)
            solver.do("rotateTopRight",visualizer)
            solver.do("rotateBackLeft",visualizer)
            solver.do("rotateTopLeft",visualizer)

    if(checkCornerBlueRedYellow(solver)):
        while(checkAllCorners(solver)==False):
            print("E2")
            for i in range(3):
                solver.do("rotateBackLeft",visualizer)
                solver.do("rotateRightBackwards",visualizer)
                solver.do("rotateBackRight",visualizer)
                solver.do("rotateRightForwards",visualizer)

            for i in range(3):
                solver.do("rotateBackRight",visualizer)
                solver.do("rotateTopRight",visualizer)
                solver.do("rotateBackLeft",visualizer)
                solver.do("rotateTopLeft",visualizer)

        return

    if(checkCornerBlueOrangeYellow(solver)):
        while(checkAllCorners(solver)==False):
            print("E3")
            for i in range(3):
                solver.do("rotateBackLeft",visualizer)
                solver.do("rotateTopLeft",visualizer)
                solver.do("rotateBackRight",visualizer)
                solver.do("rotateTopRight",visualizer)

            for i in range(3):
                solver.do("rotateBackRight",visualizer)
                solver.do("rotateLeftBackwards",visualizer)
                solver.do("rotateBackLeft",visualizer)
                solver.do("rotateLeftForwards",visualizer)
        return

    if(checkCornerGreenRedYellow(solver)):
        while(checkAllCorners(solver)==False):
            print("E4")
            for i in range(3):
                solver.do("rotateBackLeft",visualizer)
                solver.do("rotateBottomRight",visualizer)
                solver.do("rotateBackRight",visualizer)
                solver.do("rotateBottomLeft",visualizer)

            for i in range(3):
                solver.do("rotateBackRight",visualizer)
                solver.do("rotateRightForwards",visualizer)
                solver.do("rotateBackLeft",visualizer)
                solver.do("rotateRightBackwards",visualizer)

        return

    if(checkCornerGreenOrangeYellow(solver)):
        while(checkAllCorners(solver)==False):
            print("E5")
            for i in range(3):
                solver.do("rotateBackLeft",visualizer)
                solver.do("rotateLeftForwards",visualizer)
                solver.do("rotateBackRight",visualizer)
                solver.do("rotateLeftBackwards",visualizer)

            for i in range(3):
                solver.do("rotateBackRight",visualizer)
                solver.do("rotateBottomLeft",visualizer)
                solver.do("rotateBackLeft",visualizer)
                solver.do("rotateBottomRight",visualizer)

        return

#this function is a helper for fixingCorners
def cornerAlgorithm(solver,visualizer=None):
    solver.do("rotateFrontRight",visualizer)
    solver.do("rotateRightBackwards",visualizer)
    solver.do("rotateFrontLeft",visualizer)
    solver.do("rotateRightForwards",visualizer)

#turns the corners into the right position
def fixingCorners(solver, visualizer=None):

    #if all corners are already correct
    if solver.cube.cube[2,0,2][3]=='Y' and solver.cube.cube[0,0,2][3]=='Y' and solver.cube.cube[2,2,2][3]=='Y' and solver.cube.cube[0,2,2][3]=='Y':
        return

    for i in range(4):
      while(solver.cube.cube[2,0,2][3]!='Y'):
        cornerAlgorithm(solver,visualizer)
      solver.do("rotateBackLeft",visualizer)

    x,y,z = solver.isSidedCubie(solver.cube,'G','R','Y')
    while(x != 2 or y != 0 or z != 2):
        solver.do("rotateBackLeft",visualizer)
        x,y,z = solver.isSidedCubie(solver.cube,'G','R','Y')

def yellowCorners(solver,visualizer=None):
    bringYellowCornersInRightPosition(solver,visualizer)
    fixingCorners(solver,visualizer)







