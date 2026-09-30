from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
from creature import Creature
from config import FIGURE_SIZE

class Visualizer:
    def __init__(self):
        px = 1 / plt.rcParams['figure.dpi']
        self.fig = plt.figure(figsize=(FIGURE_SIZE*px, FIGURE_SIZE*px))
        pass

    def display(self, pool: list[Creature]):
        plt.xlim(0, FIGURE_SIZE)
        plt.ylim(0, FIGURE_SIZE)
        x = [c.x for c in pool]
        y = [c.y for c in pool]
        plt.scatter(x, y, s=10, c='blue', marker='o')

        plt.title("2D Creature Trait Simulator")
        plt.xlabel("X Axis")
        plt.ylabel("Y Axis")
        plt.show()