#Helper from WhiteCross, search and set the White-Red Cubie
def whiteCrossRED(solver,visualizer=None):
    #forwards the position from the White-Red Cubie
    x,y,z = solver.isTwoSidedCubie(solver.cube,'W','R')
    match (x,y,z):
        #When the White-Red Cubie is at the Front from the Cube
        case (_,_,0):
            while(x!=2 or y!=1):
                solver.do("rotateFrontLeft",visualizer)
                x,y,z = solver.isTwoSidedCubie(solver.cube,'W','R')

        #When the White-Red Cubie at the Back from the cube
        case (_,_,2):
            while(x!=2 or y!=1):
                solver.do("rotateBackLeft",visualizer)
                x,y,z = solver.isTwoSidedCubie(solver.cube,'W','R')
            solver.doNTimes("rotateRightForwards",visualizer)
            x,y,z = solver.isTwoSidedCubie(solver.cube,'W','R')

        #When the White-Red Cubie is in the Middle from the Cube
        case (_,_,1):

            #checks if the Rotation is needed at the right or left side
            if x==0:
                while z!=2:
                    solver.do("rotateLeftForwards",visualizer)
                    x,y,z = solver.isTwoSidedCubie(solver.cube,'W','R')
            else:
                while z!= 2:
                    solver.do("rotateRightForwards",visualizer)
                    x,y,z = solver.isTwoSidedCubie(solver.cube,'W','R')
            while(x!=2 or y!=1):
                solver.do("rotateBackLeft",visualizer)
                x,y,z = solver.isTwoSidedCubie(solver.cube,'W','R')
            solver.doNTimes("rotateRightForwards",visualizer)
            x,y,z = solver.isTwoSidedCubie(solver.cube,'W','R')

    #when the cubie is at the right place but the White side is not at the front
    if(solver.cube.cube[x,y,z][1]=='R'):
        solver.do("rotateRightBackwards",visualizer)
        solver.do("rotateFrontLeft",visualizer)
        solver.do("rotateTopLeft",visualizer)
        solver.do("rotateFrontRight",visualizer)

#Helper from WhiteCross, searchs and sets the White-Blue Cubie
def whiteCrossBlue(solver,visualizer=None):
    #forwards the position from the White-Blue Cubie
    x,y,z = solver.isTwoSidedCubie(solver.cube,'W','B')
    match (x,y,z):
        #When the White-Blue Cubie is at the Front from the Cube
        #It can not be at (2,1,0) because of the White-Red Cubie
        case (_,_,0):
            if(x!=1 or y!=2):
                if x==0:
                    solver.doNTimes("rotateLeftForwards", visualizer)
                elif y==0:
                    solver.doNTimes("rotateBottomLeft", visualizer)
                while(x!=1 or y!=2):
                    solver.do("rotateBackLeft", visualizer)
                    x,y,z = solver.isTwoSidedCubie(solver.cube,'W','B')
                solver.doNTimes("rotateTopLeft", visualizer)
        #When the White-Blue Cubie is at the Back from the Cube
        case (_,_,2):
            while(x!=1 or y!=2):
                solver.do("rotateBackLeft", visualizer)
                x,y,z = solver.isTwoSidedCubie(solver.cube,'W','B')
            solver.doNTimes("rotateTopLeft", visualizer)
            x,y,z = solver.isTwoSidedCubie(solver.cube,'W','B')

        #When the White-Blue Cubie is in the Middle from the Cube
        case (_,_,1):
            #checks if the Rotation is needed at the right or left side
            if x==0:
                #checks if top or bottom on left side
                if y == 0:
                    solver.do("rotateLeftForwards", visualizer)
                    solver.do("rotateBackLeft", visualizer)
                    solver.do("rotateLeftBackwards", visualizer)
                    x,y,z = solver.isTwoSidedCubie(solver.cube,'W','B')
                else:
                    solver.do("rotateLeftBackwards", visualizer)
                    solver.do("rotateBackLeft", visualizer)
                    solver.do("rotateLeftForwards", visualizer)
                    x,y,z = solver.isTwoSidedCubie(solver.cube,'W','B')

            else:
                #checks if top or bottom on right side
                if y == 0:
                    solver.do("rotateRightForwards", visualizer)
                    solver.do("rotateBackLeft", visualizer)
                    solver.do("rotateRightBackwards", visualizer)
                    x,y,z = solver.isTwoSidedCubie(solver.cube,'W','B')
                else:
                    solver.do("rotateRightBackwards", visualizer)
                    solver.do("rotateBackLeft", visualizer)
                    solver.do("rotateRightForwards", visualizer)
                    x,y,z = solver.isTwoSidedCubie(solver.cube,'W','B')

            while(x!=1 or y!=2):
                solver.do("rotateBackLeft", visualizer)
                x,y,z = solver.isTwoSidedCubie(solver.cube,'W','B')
            solver.doNTimes("rotateTopLeft", visualizer)
            x,y,z = solver.isTwoSidedCubie(solver.cube,'W','B')

    #when the cubie is at the right place but the White side is not at the front
    if(solver.cube.cube[x,y,z][1]=='B'):
        solver.do("rotateTopLeft", visualizer)
        solver.do("rotateFrontLeft", visualizer)
        solver.do("rotateLeftForwards", visualizer)
        solver.do("rotateFrontRight", visualizer)

#Helper from WhiteCross, searchs and sets the White-Orange Cubie
def whiteCrossOrange(solver,visualizer=None):
    #forwards the position from the White-Orange Cubie
    x,y,z = solver.isTwoSidedCubie(solver.cube,'W','O')
    match (x,y,z):
        #When the White-Blue Cubie is at the Front from the Cube
        #It can not be at (2,1,0) and (1,2,0) because of the White-Red and White-Blue Cubie
        case (_,_,0):
            if(x!=0 or y!=1):
                solver.doNTimes("rotateBottomLeft", visualizer)
                while(x!=0 or y!=1):
                    solver.do("rotateBackLeft", visualizer)
                    x,y,z = solver.isTwoSidedCubie(solver.cube,'W','O')
                solver.doNTimes("rotateLeftForwards", visualizer)
                x,y,z = solver.isTwoSidedCubie(solver.cube,'W','O')
        #When the White-Orange Cubie is at the Back from the Cube
        case (_,_,2):
            while(x!=0 or y!=1):
                solver.do("rotateBackLeft", visualizer)
                x,y,z = solver.isTwoSidedCubie(solver.cube,'W','O')
            solver.doNTimes("rotateLeftForwards", visualizer)
            x,y,z = solver.isTwoSidedCubie(solver.cube,'W','O')

        #When the White-Orange Cubie is in the Middle from the Cube
        case (_,_,1):
            #checks if the Rotation is needed at the right or left side
            if x!=0 or y!=1 or z!=0:
                if x==0:
                    #checks if top or bottom on left side
                    if y == 0:
                        solver.do("rotateLeftForwards", visualizer)
                        solver.do("rotateBackLeft", visualizer)
                        solver.do("rotateLeftBackwards", visualizer)
                        x,y,z = solver.isTwoSidedCubie(solver.cube,'W','O')
                    else:
                        solver.do("rotateLeftBackwards", visualizer)
                        solver.do("rotateBackLeft", visualizer)
                        solver.do("rotateLeftForwards", visualizer)
                        x,y,z = solver.isTwoSidedCubie(solver.cube,'W','O')
                else:
                    #checks if top or bottom on right side
                    if y == 0:
                        solver.do("rotateRightForwards", visualizer)
                        solver.do("rotateBackLeft", visualizer)
                        solver.do("rotateRightBackwards", visualizer)
                        x,y,z = solver.isTwoSidedCubie(solver.cube,'W','O')
                    else:
                        solver.do("rotateRightBackwards", visualizer)
                        solver.do("rotateBackLeft", visualizer)
                        solver.do("rotateRightForwards", visualizer)
                        x,y,z = solver.isTwoSidedCubie(solver.cube,'W','O')

                while(x!=0 or y!=1):
                    solver.do("rotateBackLeft", visualizer)
                    x,y,z = solver.isTwoSidedCubie(solver.cube,'W','O')
                solver.doNTimes("rotateLeftForwards", visualizer)
                x,y,z = solver.isTwoSidedCubie(solver.cube,'W','O')

    #when the cubie is at the right place but the White side is not at the front
    if(solver.cube.cube[x,y,z][1]=='O'):
        solver.do("rotateLeftForwards", visualizer)
        solver.do("rotateFrontLeft", visualizer)
        solver.do("rotateBottomRight", visualizer)
        solver.do("rotateFrontRight", visualizer)

def whiteCrossGreen(solver,visualizer=None):
    #forwards the position from the White-Green Cubie
    x,y,z = solver.isTwoSidedCubie(solver.cube,'W','G')
    match (x,y,z):
        #When the White-Green Cubie is at the Front from the Cube
        #Case (_,_,0) is trivial because when it hits, the cubie is already at the right place
        case (_,_,2):
            while(x!=1 or y!=0):
                solver.do("rotateBackLeft", visualizer)
                x,y,z = solver.isTwoSidedCubie(solver.cube,'W','G')
            solver.doNTimes("rotateBottomLeft", visualizer)
            x,y,z = solver.isTwoSidedCubie(solver.cube,'W','G')

        #When the White-Green Cubie is in the Middle from the Cube
        case (_,_,1):
            #checks if the Rotation is needed at the right or left side
            if x!=1 or y!=0 or z!=0:
                if x==0:
                    #checks if top or bottom on left side
                    if y == 0:
                        solver.do("rotateLeftForwards", visualizer)
                        solver.do("rotateBackLeft", visualizer)
                        solver.do("rotateLeftBackwards", visualizer)
                        x,y,z = solver.isTwoSidedCubie(solver.cube,'W','G')
                    else:
                        solver.do("rotateLeftBackwards", visualizer)
                        solver.do("rotateBackLeft", visualizer)
                        solver.do("rotateLeftForwards", visualizer)
                        x,y,z = solver.isTwoSidedCubie(solver.cube,'W','G')
                else:
                    #checks if top or bottom on right side
                    if y == 0:
                        solver.do("rotateRightForwards", visualizer)
                        solver.do("rotateBackLeft", visualizer)
                        solver.do("rotateRightBackwards", visualizer)
                        x,y,z = solver.isTwoSidedCubie(solver.cube,'W','G')
                    else:
                        solver.do("rotateRightBackwards", visualizer)
                        solver.do("rotateBackLeft", visualizer)
                        solver.do("rotateRightForwards", visualizer)
                        x,y,z = solver.isTwoSidedCubie(solver.cube,'W','G')

                while(x!=1 or y!=0):
                    solver.do("rotateBackLeft", visualizer)
                    x,y,z = solver.isTwoSidedCubie(solver.cube,'W','G')
                solver.doNTimes("rotateBottomLeft", visualizer)
                x,y,z = solver.isTwoSidedCubie(solver.cube,'W','G')

    #when the cubie is at the right place but the White side is not at the front
    if(solver.cube.cube[x,y,z][1]=='G'):
        solver.do("rotateBottomRight", visualizer)
        solver.do("rotateFrontLeft", visualizer)
        solver.do("rotateRightBackwards", visualizer)
        solver.do("rotateFrontRight", visualizer)

def whiteCross(solver,visualizer=None):
    whiteCrossRED(solver,visualizer)
    whiteCrossBlue(solver,visualizer)
    whiteCrossOrange(solver,visualizer)
    whiteCrossGreen(solver,visualizer)