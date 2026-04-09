from CUBE import Cube
from Solver import Solver
from CubeVisualizer import Visualizer




def main():
    cube = Cube()
    solver = Solver(cube)
    visualizer = Visualizer(cube, solver)

    visualizer.run()


if __name__ == "__main__":
    main()