from trait import Trait

class Creature:
    def __init__(self, trait: Trait):
        self.trait = trait
        self.energy = trait.energy_capacity

        self.alive = True
        self.x = 0
        self.y = 0

    def __str__(self):
        msg = (
            f"Trait: {self.trait}, "
            f"alive: {self.alive}, "
            f"x_position: {self.x}, "
            f"y_position: {self.y} "
        )
        return msg