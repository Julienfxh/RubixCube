#algorithm that brings cubies from the back into the left or right middle side
# i = 1 brings into topLeft, 2 into topRight, 3 into leftLeft(left side, left middle cubie), 4 into leftRight,
# 5 into rightLeft, 6 into rightRight, 7 into bottomleft, 8 into bottomRight
def middleAlgorithm(i,solver,visualizer=None):
    if i==1:
        solver.do("rotateBackRight",visualizer)
        solver.do("rotateLeftBackwards",visualizer)
        solver.do("rotateBackLeft",visualizer)
        solver.do("rotateLeftForwards",visualizer)

        solver.do("rotateBackLeft",visualizer)
        solver.do("rotateTopLeft",visualizer)
        solver.do("rotateBackRight",visualizer)
        solver.do("rotateTopRight",visualizer)

    if i==2:
        solver.do("rotateBackLeft",visualizer)
        solver.do("rotateRightBackwards",visualizer)
        solver.do("rotateBackRight",visualizer)
        solver.do("rotateRightForwards",visualizer)

        solver.do("rotateBackRight",visualizer)
        solver.do("rotateTopRight",visualizer)
        solver.do("rotateBackLeft",visualizer)
        solver.do("rotateTopLeft",visualizer)

    if i==3:
        solver.do("rotateBackRight",visualizer)
        solver.do("rotateBottomLeft",visualizer)
        solver.do("rotateBackLeft",visualizer)
        solver.do("rotateBottomRight",visualizer)

        solver.do("rotateBackLeft",visualizer)
        solver.do("rotateLeftForwards",visualizer)
        solver.do("rotateBackRight",visualizer)
        solver.do("rotateLeftBackwards",visualizer)

    if i==4:
        solver.do("rotateBackLeft",visualizer)
        solver.do("rotateTopLeft",visualizer)
        solver.do("rotateBackRight",visualizer)
        solver.do("rotateTopRight",visualizer)

        solver.do("rotateBackRight",visualizer)
        solver.do("rotateLeftBackwards",visualizer)
        solver.do("rotateBackLeft",visualizer)
        solver.do("rotateLeftForwards",visualizer)

    if i==5:
        solver.do("rotateBackRight",visualizer)
        solver.do("rotateTopRight",visualizer)
        solver.do("rotateBackLeft",visualizer)
        solver.do("rotateTopLeft",visualizer)

        solver.do("rotateBackLeft",visualizer)
        solver.do("rotateRightBackwards",visualizer)
        solver.do("rotateBackRight",visualizer)
        solver.do("rotateRightForwards",visualizer)

    if i==6:
        solver.do("rotateBackLeft",visualizer)
        solver.do("rotateBottomRight",visualizer)
        solver.do("rotateBackRight",visualizer)
        solver.do("rotateBottomLeft",visualizer)

        solver.do("rotateBackRight",visualizer)
        solver.do("rotateRightForwards",visualizer)
        solver.do("rotateBackLeft",visualizer)
        solver.do("rotateRightBackwards",visualizer)

    if i==7:
        solver.do("rotateBackLeft",visualizer)
        solver.do("rotateLeftForwards",visualizer)
        solver.do("rotateBackRight",visualizer)
        solver.do("rotateLeftBackwards",visualizer)

        solver.do("rotateBackRight",visualizer)
        solver.do("rotateBottomLeft",visualizer)
        solver.do("rotateBackLeft",visualizer)
        solver.do("rotateBottomRight",visualizer)

    if i==8:
        solver.do("rotateBackRight",visualizer)
        solver.do("rotateRightForwards",visualizer)
        solver.do("rotateBackLeft",visualizer)
        solver.do("rotateRightBackwards",visualizer)

        solver.do("rotateBackLeft",visualizer)
        solver.do("rotateBottomRight",visualizer)
        solver.do("rotateBackRight",visualizer)
        solver.do("rotateBottomLeft",visualizer)

def bringItOutTheMiddle(x,y,z,solver,visulaizer=None):
    match (x,y,z):

        case (0,2,1):
            middleAlgorithm(1,solver,visulaizer)
        case (2,2,1):
            middleAlgorithm(2,solver,visulaizer)
        case (0,0,1):
            middleAlgorithm(3,solver,visulaizer)
        case (2,0,1):
            middleAlgorithm(6,solver,visulaizer)

def middleTopLeft(solver,visulaizer=None):
    x,y,z = solver.isSidedCubie(solver.cube,'B','O')

    if(solver.cube.cube[x,y,z][5]=='B' and x==0 and y==2 and z ==1):
        return

    bringItOutTheMiddle(x,y,z,solver,visulaizer)
    x,y,z = solver.isSidedCubie(solver.cube,'B','O')

    while(y!=2):
        solver.do("rotateBackLeft",visulaizer)
        x,y,z = solver.isSidedCubie(solver.cube,'B','O')

    if(solver.cube.cube[1,2,2][5]=='B'):
        middleAlgorithm(1,solver,visulaizer)
    else:
        solver.do("rotateBackLeft",visulaizer)
        middleAlgorithm(4,solver,visulaizer)

def middleTopRight(solver,visulaizer=None):
    x,y,z = solver.isSidedCubie(solver.cube,'B','R')

    if(solver.cube.cube[x,y,z][5]=='B' and x==2 and y==2 and z ==1):
        return

    bringItOutTheMiddle(x,y,z,solver,visulaizer)
    x,y,z = solver.isSidedCubie(solver.cube,'B','R')

    while(y!=2):
        solver.do("rotateBackLeft",visulaizer)
        x,y,z = solver.isSidedCubie(solver.cube,'B','R')

    if(solver.cube.cube[1,2,2][5]=='B'):
        middleAlgorithm(2,solver,visulaizer)
    else:
        solver.do("rotateBackRight",visulaizer)
        middleAlgorithm(5,solver,visulaizer)

def middleBottomLeft(solver,visulaizer=None):
    x,y,z = solver.isSidedCubie(solver.cube,'G','O')

    if(solver.cube.cube[x,y,z][4]=='G' and x==0 and y==0 and z ==1):
        return

    bringItOutTheMiddle(x,y,z,solver,visulaizer)
    x,y,z = solver.isSidedCubie(solver.cube,'G','O')

    while(y!=0):
        solver.do("rotateBackLeft",visulaizer)
        x,y,z = solver.isSidedCubie(solver.cube,'G','O')

    if(solver.cube.cube[1,0,2][4]=='G'):
        middleAlgorithm(7,solver,visulaizer)
    else:
        solver.do("rotateBackRight",visulaizer)
        middleAlgorithm(3,solver,visulaizer)

def middleBottomRight(solver,visualaizer=None):
    x,y,z = solver.isSidedCubie(solver.cube,'G','R')

    if solver.cube.cube[x,y,z][4]== 'G' and x==2 and y==0 and z ==1:
        return

    bringItOutTheMiddle(x, y, z, solver, visualaizer)
    x,y,z = solver.isSidedCubie(solver.cube,'G','R')

    while(y!=0):
        solver.do("rotateBackLeft", visualaizer)
        x,y,z = solver.isSidedCubie(solver.cube,'G','R')

    if(solver.cube.cube[1,0,2][4]=='G'):
        middleAlgorithm(8, solver, visualaizer)
    else:
        solver.do("rotateBackLeft", visualaizer)
        middleAlgorithm(6, solver, visualaizer)


def middle(solver,visualizer=None):
    middleTopLeft(solver,visualizer)
    middleTopRight(solver,visualizer)
    middleBottomLeft(solver,visualizer)
    middleBottomRight(solver, visualizer)


