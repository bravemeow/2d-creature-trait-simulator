# 2D Creature Trait Simulator

A simple creature trait simulator by using genetic algorithm.

## Objective

Find adaptive creature traits under different environmental conditions and analyze how survival factors influence the evolution of creature over generations.

## How it works

1. populate initial population
2. each creature owns a chromosome(trait)
3. creatures act based on their trait under each environments
4. calculate fitness (wellness/survived)
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

- food density
- food regeneration rate

## Genetic Algorithm

- Chromosome - Creature traits
- Fitness - Survival (survived time + current energy)
- Selection - Tournament selection (T=3)
- Crossover - Parents traits (Uniform crossover)
- Mutation - One of traits (random -0.5 to +0.5)

