from ex1.Creature import Creature
from ..HealCapability import HealCapability

class Sproutling(Creature, HealCapability):
    def __init__(self):
        super().__init__("Sproutling", "Grass")

    def attack(self) -> None:
        return "Sproutling uses Vine Whip!"

    def heal(self) -> None:
        return "Sproutling heals itself for a small amount"
