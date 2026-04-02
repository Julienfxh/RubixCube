from CubeVisualizer import CubeVisualizer
from CUBE import Cube  # deine Datei
from vpython import *

cube = Cube()
vis = CubeVisualizer(cube.cube)

while True:
    rate(30)