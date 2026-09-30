from population_builder import PopulationBuilder
from visualizer import Visualizer

def main():
    p = PopulationBuilder()
    init_pool = p.create_initial_population()

    print(init_pool)

    v = Visualizer()

    v.display(init_pool)

if __name__ == "__main__":
    main()