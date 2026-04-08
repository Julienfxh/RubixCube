
#helper form WhiteConers, searchs and sets the orange-white-blue cubie
def topLeftCorner(solver, visualizer=None):
    #this function is splitted into two phases
    #at the first phase we set the cubie at the right spot in the z=2 layer
    #at the second phase we rotate the cubie until it fits into the front

    #phase 1
    #forwards the postion from the orange-white-blue cubie
    x,y,z = solver.isSidedCubie(solver.cube,'W','B','O')

    #checks if the cubie is at the front
    if(z==0):
        #topLeft Corner
        if(x==0 and y==2):
            #checks if cubie is already on the right place
            if(solver.cube.cube[0,2,0][0]=='O' or solver.cube.cube[0,2,0][1]=='W' or solver.cube.cube[0,2,0][5]=='B'):
                return

            solver.do("rotateLeftBackwards",visualizer)
            solver.do("rotateBackLeft",visualizer)
            solver.do("rotateLeftForwards",visualizer)

        #bottomLeft Corner
        if(x==0 and y==0):
            solver.do("rotateLeftForwards",visualizer)
            solver.do("rotateBackLeft",visualizer)
            solver.do("rotateLeftBackwards",visualizer)

        #topRight Corner
        if(x==2 and y==2):
            solver.do("rotateRightBackwards",visualizer)
            solver.do("rotateBackLeft",visualizer)
            solver.do("rotateRightForwards",visualizer)

        #bottomRight Corner
        if(x==2 and y==0):
            solver.do("rotateRightForwards",visualizer)
            solver.do("rotateBackLeft",visualizer)
            solver.do("rotateRightBackwards",visualizer)

        x,y,z = solver.isSidedCubie(solver.cube,'W','B','O')

    while(x!=0 or y!= 2):
        solver.do("rotateBackLeft")
        x,y,z = solver.isSidedCubie(solver.cube,'W','B','O')

    #phase 2
    while(solver.cube.cube[0,2,0][0]!='O' or solver.cube.cube[0,2,0][1]!='W' or solver.cube.cube[0,2,0][5]!='B'):
       solver.do("rotateLeftBackwards",visualizer)
       solver.do("rotateBackRight",visualizer)
       solver.do("rotateLeftForwards",visualizer)
       solver.do("rotateBackLeft",visualizer)
       x,y,z = solver.isSidedCubie(solver.cube,'W','B','O')

def topRightCorner(solver,visualizer=None):

    #Phase 1
    x,y,z = solver.isSidedCubie(solver.cube,'W','R','B')

    if(z==0):
        #topLeft Corner
        if(x==0 and y==2):
            solver.do("rotateLeftBackwards",visualizer)
            solver.do("rotateBackLeft",visualizer)
            solver.do("rotateLeftForwards",visualizer)

        #bottomLeft Corner
        if(x==0 and y==0):
            solver.do("rotateLeftForwards",visualizer)
            solver.do("rotateBackLeft",visualizer)
            solver.do("rotateLeftBackwards",visualizer)

        #topRight Corner
        if(x==2 and y==2):
            if(solver.cube.cube[2,2,0][1]=='W' or solver.cube.cube[2,2,0][2]=='R' or solver.cube.cube[2,2,0][5]=='B'):
                return
            solver.do("rotateRightBackwards",visualizer)
            solver.do("rotateBackLeft",visualizer)
            solver.do("rotateRightForwards",visualizer)

        #bottomRight Corner
        if(x==2 and y==0):
            solver.do("rotateRightForwards",visualizer)
            solver.do("rotateBackLeft",visualizer)
            solver.do("rotateRightBackwards",visualizer)

        x,y,z = solver.isSidedCubie(solver.cube,'W','R','B')

    while(x!=2 or y!=2 ):
        solver.do("rotateBackLeft")
        x,y,z = solver.isSidedCubie(solver.cube,'W','R','B')

    #phase 2
    while(solver.cube.cube[2,2,0][1]!='W' or solver.cube.cube[2,2,0][2]!='R' or solver.cube.cube[2,2,0][5]!='B'):
        solver.do("rotateRightBackwards",visualizer)
        solver.do("rotateBackLeft",visualizer)
        solver.do("rotateRightForwards",visualizer)
        solver.do("rotateBackRight",visualizer)
        x,y,z = solver.isSidedCubie(solver.cube,'W','R','B')

def bottomLeftCorner(solver,visualizer=None):
    #Phase 1
    x,y,z = solver.isSidedCubie(solver.cube,'W','O','G')

    if(z==0):
        #topLeft Corner
        if(x==0 and y==2):
            solver.do("rotateLeftBackwards",visualizer)
            solver.do("rotateBackLeft",visualizer)
            solver.do("rotateLeftForwards",visualizer)

        #bottomLeft Corner
        if(x==0 and y==0):
            if(solver.cube.cube[0,0,0][0]=='O' or solver.cube.cube[0,0,0][1]=='W' or solver.cube.cube[0,0,0][4]=='G'):
                return
            solver.do("rotateLeftForwards",visualizer)
            solver.do("rotateBackLeft",visualizer)
            solver.do("rotateLeftBackwards",visualizer)

        #topRight Corner
        if(x==2 and y==2):
            solver.do("rotateRightBackwards",visualizer)
            solver.do("rotateBackLeft",visualizer)
            solver.do("rotateRightForwards",visualizer)

        #bottomRight Corner
        if(x==2 and y==0):
            solver.do("rotateRightForwards",visualizer)
            solver.do("rotateBackLeft",visualizer)
            solver.do("rotateRightBackwards",visualizer)

        x,y,z = solver.isSidedCubie(solver.cube,'W','O','G')

    while(x!=0 or y!=0 ):
        solver.do("rotateBackLeft")
        x,y,z = solver.isSidedCubie(solver.cube,'W','O','G')

    #phase 2
    while(solver.cube.cube[0,0,0][0]!='O' or solver.cube.cube[0,0,0][1]!='W' or solver.cube.cube[0,0,0][4]!='G'):
        solver.do("rotateLeftForwards",visualizer)
        solver.do("rotateBackLeft",visualizer)
        solver.do("rotateLeftBackwards",visualizer)
        solver.do("rotateBackRight",visualizer)
        x,y,z = solver.isSidedCubie(solver.cube,'W','O','G')

def bottomRightCorners(solver,visualizer=None):
    #Phase 1
    x,y,z = solver.isSidedCubie(solver.cube,'W','R','G')

    if(z==0):
        #topLeft Corner
        if(x==0 and y==2):
            solver.do("rotateLeftBackwards",visualizer)
            solver.do("rotateBackLeft",visualizer)
            solver.do("rotateLeftForwards",visualizer)

        #bottomLeft Corner
        if(x==0 and y==0):
            solver.do("rotateLeftForwards",visualizer)
            solver.do("rotateBackLeft",visualizer)
            solver.do("rotateLeftBackwards",visualizer)

        #topRight Corner
        if(x==2 and y==2):
            solver.do("rotateRightBackwards",visualizer)
            solver.do("rotateBackLeft",visualizer)
            solver.do("rotateRightForwards",visualizer)

        #bottomRight Corner
        if(x==2 and y==0):
            if(solver.cube.cube[2,0,0][1]=='W' or solver.cube.cube[2,0,0][2]=='R' or solver.cube.cube[2,0,0][4]=='G'):
                return
            solver.do("rotateRightForwards",visualizer)
            solver.do("rotateBackLeft",visualizer)
            solver.do("rotateRightBackwards",visualizer)

        x,y,z = solver.isSidedCubie(solver.cube,'W','R','G')

    while(x!=2 or y!=0 ):
        solver.do("rotateBackLeft")
        x,y,z = solver.isSidedCubie(solver.cube,'W','R','G')

    #phase 2
    while(solver.cube.cube[2,0,0][1]!='W' or solver.cube.cube[2,0,0][2]!='R' or solver.cube.cube[2,0,0][4]!='G'):
        solver.do("rotateRightForwards",visualizer)
        solver.do("rotateBackRight",visualizer)
        solver.do("rotateRightBackwards",visualizer)
        solver.do("rotateBackLeft",visualizer)
        x,y,z = solver.isSidedCubie(solver.cube,'W','R','G')



def whiteCorners(solver,visualizer=None):
    topLeftCorner(solver,visualizer)
    topRightCorner(solver,visualizer)
    bottomLeftCorner(solver,visualizer)
    bottomRightCorners(solver,visualizer)







