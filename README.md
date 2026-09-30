# 2D Creature Trait Simulator

A simple creature trait simulator by using genetic algorithm.

## Objective

Find adaptive creature traits under different environmental conditions and analyze how survival factors influence the evolution of creature over generations.

## How it works

1. populate initial population
2. each creature owns a chromosome(trait)
3. creatures act(animate) based on their trait under each environments
4. calculate fitness (survived_time, holding_energy)
5. selection -> crossover -> mutation
6. generate next generation
7. loop from step 3 to step 6 enough amount of times

## Creature traits

- speed
- vision range
- metabolism
- size
- energy_capacity

## Environment parameters

- food distribution/quantity
- food regeneration rate

## Genetic Algorithm

- Chromosome - Creature traits
- Fitness - Survival (survived time + current energy)
- Selection - Tournament selection (T=3)
- Crossover - Parents traits (Uniform crossover)
- Mutation - One of traits (random -0.1 to +0.1)

## Visualization

1. matplotlib 2D scatter plot
2. rendering movements of creatures in 60 frame per sec (FPS)
3. after a fixed amount of time(few seconds), a generation ends
4. visualize next generation... until final generation
5. display the traits of the last generation's creatures
