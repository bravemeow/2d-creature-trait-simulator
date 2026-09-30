
class Trait:

    def __init__(self, speed: float, vision: float, metabolism: float, size: float, energy_capacity: float):
        self.speed = speed
        self.vision = vision
        self.metabolism = metabolism
        self.size = size
        self.energy_capacity = energy_capacity

    def __str__(self):
        msg = (
            f"Speed: {self.speed} "
            f"Vision: {self.vision} "
            f"Metabolism: {self.metabolism} "
            f"Size: {self.size} "
            f"Energy_capacity: {self.energy_capacity}"
        )
        return msg