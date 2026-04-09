def isYellowCross(solver):
        if(solver.cube.cube[0,1,2][3]=='Y' and solver.cube.cube[1,0,2][3]=='Y' and solver.cube.cube[1,2,2][3]=='Y' and solver.cube.cube[2,1,2][3]=='Y'):
            return True
        return False


def isYellowL(solver,visualizer=None):
    for i in range(4):
        if(solver.cube.cube[0,1,2][3]=='Y' and solver.cube.cube[1,0,2][3]=='Y'):
            return True
        solver.do("rotateBackLeft",visualizer)
    return False

def isYellowLine(solver,visualizer=None):
    for i in range(4):
        if(solver.cube.cube[0,1,2][3]=='Y' and solver.cube.cube[2,1,2][3]=='Y'):
            return True
        solver.do("rotateBackLeft",visualizer)
    return False

def yellowCrossAlgorithm(solver,visualizer=None):
    solver.do("rotateTopLeft",visualizer)
    solver.do("rotateBackLeft",visualizer)
    solver.do("rotateRightBackwards",visualizer)
    solver.do("rotateBackRight",visualizer)
    solver.do("rotateRightForwards",visualizer)
    solver.do("rotateTopRight",visualizer)

def yellowCrossToTheTop(solver,visualizer=None):
   while isYellowLine(solver,visualizer)==False or isYellowL(solver,visualizer)==False or isYellowCross(solver)==False:
       yellowCrossAlgorithm(solver,visualizer)

def isCorrectBlueGreen(solver,visualizer=None):
    for i in range(4):
     if(solver.cube.cube[1,0,2][4]=='G' and solver.cube.cube[1,2,2][5]=='B'):
        return True
     solver.do("rotateBackLeft",visualizer)
    return False

def isCorrectOrangeRed(solver, visualizer=None):
    for i in range(4):
     if solver.cube.cube[0,1,2][0]== 'O' and solver.cube.cube[2,1,2][2]== 'R':
        return True
     solver.do("rotateBackLeft",visualizer)
    return False

def isCorrectCross(solver, visualizer=None):
     if(isCorrectBlueGreen(solver,visualizer) and isCorrectOrangeRed(solver,visualizer)):
        return True
     return False

def isCorrectBlueRed(solver, visualizer=None):
    for i in range(4):
     if solver.cube.cube[1,2,2][5]== 'B' and solver.cube.cube[2,1,2][2]== 'R':
        return True
     solver.do("rotateBackLeft",visualizer)
    return False

def isCorrectBlueOrange(solver,visualizer=None):
    for i in range(4):
     if solver.cube.cube[1,2,2][5]== 'B' and solver.cube.cube[0,1,2][0]== 'O':
        return True
     solver.do("rotateBackLeft",visualizer)
    return False

def isCorrectGreenOrange(solver,visualizer=None):
    for i in range(4):
     if solver.cube.cube[1,0,2][4]== 'G' and solver.cube.cube[0,1,2][0]== 'O':
        return True
     solver.do("rotateBackLeft",visualizer)
    return False

def isCorrectGreenRed(solver, visualizer=None):
    for i in range(4):
     if solver.cube.cube[1,0,2][4]== 'G' and solver.cube.cube[2,1,2][2]== 'R':
        return True
     solver.do("rotateBackLeft",visualizer)
    return False

#fixes the cross so that it match with the middle
def directTheYellowCross(solver,visualizer=None):

    #when the cross is already correct
    if isCorrectCross(solver):
        return

    if(isCorrectBlueGreen(solver,visualizer) or isCorrectOrangeRed(solver,visualizer)):
        solver.do("rotateBottomRight",visualizer)
        solver.do("rotateBackLeft",visualizer)
        solver.do("rotateBottomLeft",visualizer)
        solver.do("rotateBackLeft",visualizer)
        solver.do("rotateBottomRight",visualizer)
        solver.do("rotateBackRight",visualizer)
        solver.do("rotateBackRight",visualizer)
        solver.do("rotateBottomLeft",visualizer)

    if isCorrectBlueRed(solver,visualizer):
        solver.do("rotateTopLeft",visualizer)
        solver.do("rotateBackLeft",visualizer)
        solver.do("rotateTopRight",visualizer)
        solver.do("rotateBackLeft",visualizer)
        solver.do("rotateTopLeft",visualizer)
        solver.do("rotateBackRight",visualizer)
        solver.do("rotateBackRight",visualizer)
        solver.do("rotateTopRight",visualizer)
        isCorrectCross(solver,visualizer)
        return

    if isCorrectBlueOrange(solver,visualizer):
        solver.do("rotateLeftForwards",visualizer)
        solver.do("rotateBackLeft",visualizer)
        solver.do("rotateLeftBackwards",visualizer)
        solver.do("rotateBackLeft",visualizer)
        solver.do("rotateLeftForwards",visualizer)
        solver.do("rotateBackRight",visualizer)
        solver.do("rotateBackRight",visualizer)
        solver.do("rotateLeftBackwards",visualizer)
        isCorrectCross(solver,visualizer)
        return

    if isCorrectGreenRed(solver,visualizer):
        solver.do("rotateRightBackwards",visualizer)
        solver.do("rotateBackLeft",visualizer)
        solver.do("rotateRightForwards",visualizer)
        solver.do("rotateBackLeft",visualizer)
        solver.do("rotateRightBackwards",visualizer)
        solver.do("rotateBackRight",visualizer)
        solver.do("rotateBackRight",visualizer)
        solver.do("rotateRightForwards",visualizer)
        isCorrectCross(solver,visualizer)
        return

    if isCorrectGreenOrange(solver,visualizer):
        solver.do("rotateBottomRight",visualizer)
        solver.do("rotateBackLeft",visualizer)
        solver.do("rotateBottomLeft",visualizer)
        solver.do("rotateBackLeft",visualizer)
        solver.do("rotateBottomRight",visualizer)
        solver.do("rotateBackRight",visualizer)
        solver.do("rotateBackRight",visualizer)
        solver.do("rotateBottomLeft",visualizer)
        isCorrectCross(solver,visualizer)
        return







def yellowCross(solver,visualizer=None):
    yellowCrossToTheTop(solver,visualizer)
    directTheYellowCross(solver,visualizer)