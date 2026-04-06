import time
import numpy as np
class Solver:
    def __init__(self, cube):
        self.cube = cube

    def rotateTop2Times(self,visualizer=None):
        x = 2
        while x !=0:
          self.cube.rotateTopLeft()
          visualizer.update_colors()
          time.sleep(0.5)
          x = x-1

    def rotateRight2Times(self,visualizer=None):
        x = 2
        while x !=0:
            self.cube.rotateRightForwards()
            visualizer.update_colors()
            time.sleep(0.5)
            x = x-1

    def rotateLeft2Times(self,visualizer=None):
        x = 2
        while x !=0:
            self.cube.rotateLeftForwards()
            visualizer.update_colors()
            time.sleep(0.5)
            x = x-1

    def rotateBottom2Times(self,visualizer=None):
        x = 2
        while x !=0:
            self.cube.rotateBottomLeft()
            visualizer.update_colors()
            time.sleep(0.5)
            x = x-1


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


    #Helper from WhiteCross, search and set the White-Red Cubie
    def whiteCrossRED(self,visualizer=None):
        #forwards the position from the White-Red Cubie
        x,y,z = self.isTwoSidedCubie(self.cube,'W','R')
        match (x,y,z):
            #When the White-Red Cubie is at the Front from the Cube
            case (_,_,0):
                while(x!=2 or y!=1):
                    self.cube.rotateFrontLeft()
                    visualizer.update_colors()
                    x,y,z = self.isTwoSidedCubie(self.cube,'W','R')
                    time.sleep(0.5)
            #When the White-Red Cubie at the Back from the cube
            case (_,_,2):
                while(x!=2 or y!=1):
                    self.cube.rotateBackLeft()
                    visualizer.update_colors()
                    x,y,z = self.isTwoSidedCubie(self.cube,'W','R')
                    time.sleep(0.5)
                self.rotateRight2Times(visualizer)
                x,y,z = self.isTwoSidedCubie(self.cube,'W','R')
            #When the White-Red Cubie is in the Middle from the Cube
            case (_,_,1):
                #checks if the Rotation is needed at the right or left side
                if x==0:
                    while z!=2:
                        self.cube.rotateLeftForwards()
                        visualizer.update_colors()
                        x,y,z = self.isTwoSidedCubie(self.cube,'W','R')
                        time.sleep(0.5)
                else:
                    while z!= 2:
                        self.cube.rotateRightForwards()
                        visualizer.update_colors()
                        x,y,z = self.isTwoSidedCubie(self.cube,'W','R')
                        time.sleep(0.5)
                while(x!=2 or y!=1):
                    self.cube.rotateBackLeft()
                    visualizer.update_colors()
                    x,y,z = self.isTwoSidedCubie(self.cube,'W','R')
                    time.sleep(0.5)
                self.rotateRight2Times(visualizer)
                x,y,z = self.isTwoSidedCubie(self.cube,'W','R')

        #when the cubie is at the right place but the White side is not at the front
        if(self.cube.cube[x,y,z][1]=='R'):
            self.cube.rotateRightBackwards()
            visualizer.update_colors()
            time.sleep(0.5)
            self.cube.rotateFrontLeft()
            visualizer.update_colors()
            time.sleep(0.5)
            self.cube.rotateTopLeft()
            visualizer.update_colors()
            time.sleep(0.5)
            self.cube.rotateFrontRight()
            visualizer.update_colors()
            time.sleep(0.5)

    #Helper from WhiteCross, searchs and sets the White-Blue Cubie
    def whiteCrossBlue(self,visualizer=None):
        #forwards the position from the White-Blue Cubie
        x,y,z = self.isTwoSidedCubie(self.cube,'W','B')
        match (x,y,z):
            #When the White-Blue Cubie is at the Front from the Cube
            #It can not be at (2,1,0) because of the White-Red Cubie
            case (_,_,0):
                if(x!=1 or y!=2):
                  if x==0:
                    self.rotateLeft2Times(visualizer)
                  elif y==0:
                    self.rotateBottom2Times(visualizer)
                  while(x!=1 or y!=2):
                      self.cube.rotateBackLeft()
                      visualizer.update_colors()
                      x,y,z = self.isTwoSidedCubie(self.cube,'W','B')
                      time.sleep(0.5)
                  self.rotateTop2Times(visualizer)
            #When the White-Blue Cubie is at the Back from the Cube
            case (_,_,2):
                while(x!=1 or y!=2):
                    self.cube.rotateBackLeft()
                    visualizer.update_colors()
                    x,y,z = self.isTwoSidedCubie(self.cube,'W','B')
                    time.sleep(0.5)
                self.rotateTop2Times(visualizer)
                x,y,z = self.isTwoSidedCubie(self.cube,'W','B')

            #When the White-Blue Cubie is in the Middle from the Cube
            case (_,_,1):
                #checks if the Rotation is needed at the right or left side
                if x==0:
                    #checks if top or bottom on left side
                    if y == 0:
                        self.cube.rotateLeftForwards()
                        visualizer.update_colors()
                        time.sleep(0.5)
                        self.cube.rotateBackLeft()
                        visualizer.update_colors()
                        time.sleep(0.5)
                        self.cube.rotateLeftBackwards()
                        visualizer.update_colors()
                        time.sleep(0.5)
                        x,y,z = self.isTwoSidedCubie(self.cube,'W','B')
                    else:
                        self.cube.rotateLeftBackwards()
                        visualizer.update_colors()
                        time.sleep(0.5)
                        self.cube.rotateBackLeft()
                        visualizer.update_colors()
                        time.sleep(0.5)
                        self.cube.rotateLeftForwards()
                        visualizer.update_colors()
                        time.sleep(0.5)
                        x,y,z = self.isTwoSidedCubie(self.cube,'W','B')

                else:
                    #checks if top or bottom on right side
                    if y == 0:
                        self.cube.rotateRightForwards()
                        visualizer.update_colors()
                        time.sleep(0.5)
                        self.cube.rotateBackLeft()
                        visualizer.update_colors()
                        time.sleep(0.5)
                        self.cube.rotateRightBackwards()
                        visualizer.update_colors()
                        time.sleep(0.5)
                        x,y,z = self.isTwoSidedCubie(self.cube,'W','B')
                    else:
                        self.cube.rotateRightBackwards()
                        visualizer.update_colors()
                        time.sleep(0.5)
                        self.cube.rotateBackLeft()
                        visualizer.update_colors()
                        time.sleep(0.5)
                        self.cube.rotateRightForwards()
                        visualizer.update_colors()
                        time.sleep(0.5)
                        x,y,z = self.isTwoSidedCubie(self.cube,'W','B')

                while(x!=1 or y!=2):
                    self.cube.rotateBackLeft()
                    visualizer.update_colors()
                    x,y,z = self.isTwoSidedCubie(self.cube,'W','B')
                    time.sleep(0.5)
                self.rotateTop2Times(visualizer)
                x,y,z = self.isTwoSidedCubie(self.cube,'W','B')

        #when the cubie is at the right place but the White side is not at the front
        if(self.cube.cube[x,y,z][1]=='B'):
            self.cube.rotateTopLeft()
            visualizer.update_colors()
            time.sleep(0.5)
            self.cube.rotateFrontLeft()
            visualizer.update_colors()
            time.sleep(0.5)
            self.cube.rotateLeftForwards()
            visualizer.update_colors()
            time.sleep(0.5)
            self.cube.rotateFrontRight()
            visualizer.update_colors()
            time.sleep(0.5)

    #Helper from WhiteCross, searchs and sets the White-Orange Cubie
    def whiteCrossOrange(self,visualizer=None):
        #forwards the position from the White-Orange Cubie
        x,y,z = self.isTwoSidedCubie(self.cube,'W','O')
        match (x,y,z):
            #When the White-Blue Cubie is at the Front from the Cube
            #It can not be at (2,1,0) and (1,2,0) because of the White-Red and White-Blue Cubie
            case (_,_,0):
                if(x!=0 or y!=1):
                  self.rotateBottom2Times(visualizer)
                  while(x!=0 or y!=1):
                    self.cube.rotateBackLeft()
                    visualizer.update_colors()
                    x,y,z = self.isTwoSidedCubie(self.cube,'W','O')
                    time.sleep(0.5)
                  self.rotateLeft2Times(visualizer)
                  x,y,z = self.isTwoSidedCubie(self.cube,'W','O')
            #When the White-Orange Cubie is at the Back from the Cube
            case (_,_,2):
                while(x!=0 or y!=1):
                    self.cube.rotateBackLeft()
                    visualizer.update_colors()
                    x,y,z = self.isTwoSidedCubie(self.cube,'W','O')
                    time.sleep(0.5)
                self.rotateLeft2Times(visualizer)
                x,y,z = self.isTwoSidedCubie(self.cube,'W','O')

            #When the White-Orange Cubie is in the Middle from the Cube
            case (_,_,1):
                #checks if the Rotation is needed at the right or left side
                if x!=0 or y!=1 or z!=0:
                  if x==0:
                    #checks if top or bottom on left side
                    if y == 0:
                      self.cube.rotateLeftForwards()
                      visualizer.update_colors()
                      time.sleep(0.5)
                      self.cube.rotateBackLeft()
                      visualizer.update_colors()
                      time.sleep(0.5)
                      self.cube.rotateLeftBackwards()
                      visualizer.update_colors()
                      time.sleep(0.5)
                      x,y,z = self.isTwoSidedCubie(self.cube,'W','O')
                    else:
                      self.cube.rotateLeftBackwards()
                      visualizer.update_colors()
                      time.sleep(0.5)
                      self.cube.rotateBackLeft()
                      visualizer.update_colors()
                      time.sleep(0.5)
                      self.cube.rotateLeftForwards()
                      visualizer.update_colors()
                      time.sleep(0.5)
                      x,y,z = self.isTwoSidedCubie(self.cube,'W','O')
                  else:
                      #checks if top or bottom on right side
                      if y == 0:
                          self.cube.rotateRightForwards()
                          visualizer.update_colors()
                          time.sleep(0.5)
                          self.cube.rotateBackLeft()
                          visualizer.update_colors()
                          time.sleep(0.5)
                          self.cube.rotateRightBackwards()
                          visualizer.update_colors()
                          time.sleep(0.5)
                          x,y,z = self.isTwoSidedCubie(self.cube,'W','O')
                      else:
                          self.cube.rotateRightBackwards()
                          visualizer.update_colors()
                          time.sleep(0.5)
                          self.cube.rotateBackLeft()
                          visualizer.update_colors()
                          time.sleep(0.5)
                          self.cube.rotateRightForwards()
                          visualizer.update_colors()
                          time.sleep(0.5)
                          x,y,z = self.isTwoSidedCubie(self.cube,'W','O')

                  while(x!=0 or y!=1):
                    self.cube.rotateBackLeft()
                    visualizer.update_colors()
                    x,y,z = self.isTwoSidedCubie(self.cube,'W','O')
                    time.sleep(0.5)
                  self.rotateLeft2Times(visualizer)
                  x,y,z = self.isTwoSidedCubie(self.cube,'W','O')

        #when the cubie is at the right place but the White side is not at the front
        if(self.cube.cube[x,y,z][1]=='O'):
            self.cube.rotateLeftForwards()
            visualizer.update_colors()
            time.sleep(0.5)
            self.cube.rotateFrontLeft()
            visualizer.update_colors()
            time.sleep(0.5)
            self.cube.rotateBottomRight()
            visualizer.update_colors()
            time.sleep(0.5)
            self.cube.rotateFrontRight()
            visualizer.update_colors()
            time.sleep(0.5)

    def whiteCrossGreen(self,visualizer):
        #forwards the position from the White-Green Cubie
        x,y,z = self.isTwoSidedCubie(self.cube,'W','G')
        match (x,y,z):
            #When the White-Green Cubie is at the Front from the Cube
            #Case (_,_,0) is trivial because when it hits, the cubie is already at the right place
            case (_,_,2):
                while(x!=1 or y!=0):
                    self.cube.rotateBackLeft()
                    visualizer.update_colors()
                    x,y,z = self.isTwoSidedCubie(self.cube,'W','G')
                    time.sleep(0.5)
                self.rotateBottom2Times(visualizer)
                x,y,z = self.isTwoSidedCubie(self.cube,'W','G')

            #When the White-Green Cubie is in the Middle from the Cube
            case (_,_,1):
                #checks if the Rotation is needed at the right or left side
                if x!=1 or y!=0 or z!=0:
                    if x==0:
                        #checks if top or bottom on left side
                        if y == 0:
                            self.cube.rotateLeftForwards()
                            visualizer.update_colors()
                            time.sleep(0.5)
                            self.cube.rotateBackLeft()
                            visualizer.update_colors()
                            time.sleep(0.5)
                            self.cube.rotateLeftBackwards()
                            visualizer.update_colors()
                            time.sleep(0.5)
                            x,y,z = self.isTwoSidedCubie(self.cube,'W','G')
                        else:
                            self.cube.rotateLeftBackwards()
                            visualizer.update_colors()
                            time.sleep(0.5)
                            self.cube.rotateBackLeft()
                            visualizer.update_colors()
                            time.sleep(0.5)
                            self.cube.rotateLeftForwards()
                            visualizer.update_colors()
                            time.sleep(0.5)
                            x,y,z = self.isTwoSidedCubie(self.cube,'W','G')
                    else:
                        #checks if top or bottom on right side
                        if y == 0:
                            self.cube.rotateRightForwards()
                            visualizer.update_colors()
                            time.sleep(0.5)
                            self.cube.rotateBackLeft()
                            visualizer.update_colors()
                            time.sleep(0.5)
                            self.cube.rotateRightBackwards()
                            visualizer.update_colors()
                            time.sleep(0.5)
                            x,y,z = self.isTwoSidedCubie(self.cube,'W','G')
                        else:
                            self.cube.rotateRightBackwards()
                            visualizer.update_colors()
                            time.sleep(0.5)
                            self.cube.rotateBackLeft()
                            visualizer.update_colors()
                            time.sleep(0.5)
                            self.cube.rotateRightForwards()
                            visualizer.update_colors()
                            time.sleep(0.5)
                            x,y,z = self.isTwoSidedCubie(self.cube,'W','G')

                    while(x!=1 or y!=0):
                        self.cube.rotateBackLeft()
                        visualizer.update_colors()
                        x,y,z = self.isTwoSidedCubie(self.cube,'W','G')
                        time.sleep(0.5)
                    self.rotateBottom2Times(visualizer)
                    x,y,z = self.isTwoSidedCubie(self.cube,'W','G')

        #when the cubie is at the right place but the White side is not at the front
        if(self.cube.cube[x,y,z][1]=='G'):
            self.cube.rotateBottomRight()
            visualizer.update_colors()
            time.sleep(0.5)
            self.cube.rotateFrontLeft()
            visualizer.update_colors()
            time.sleep(0.5)
            self.cube.rotateRightBackwards()
            visualizer.update_colors()
            time.sleep(0.5)
            self.cube.rotateFrontRight()
            visualizer.update_colors()
            time.sleep(0.5)





    def whiteCross(self,visualizer=None):
        self.whiteCrossRED(visualizer)
        self.whiteCrossBlue(visualizer)
        self.whiteCrossOrange(visualizer)
        self.whiteCrossGreen(visualizer)







