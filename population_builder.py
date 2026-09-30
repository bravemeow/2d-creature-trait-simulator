from creature import Creature
from trait import Trait
import random as r
from config import FIGURE_SIZE, POPULATION_SIZE

class PopulationBuilder:
    def __init__(self):
        self.pool_size = POPULATION_SIZE
        self.position_min_offset = int(FIGURE_SIZE/POPULATION_SIZE)
        self.randomize_positions()

    def create_initial_population(self) -> list[Creature]:
        pool = []

        for i in range(self.pool_size):
            speed, vision, metabolism, size, energy_capacity = [round(r.random(), 2) for _ in range(5)]
            
            t = Trait(speed, vision, metabolism, size, energy_capacity)
            c = Creature(t)
            c.x = self.positions[i]["x"]
            c.y = self.positions[i]["y"]
            pool.append(c)
        return pool
    
    def generate(self):
        ...


    def randomize_positions(self):
        self.positions = []
        x = r.sample(range(self.position_min_offset, FIGURE_SIZE+1, self.position_min_offset), self.pool_size)
        y = r.sample(range(self.position_min_offset, FIGURE_SIZE+1, self.position_min_offset), self.pool_size)
           
        for i in range(self.pool_size):
             self.positions.append({
                "x": x[i],
                "y": y[i]
            })