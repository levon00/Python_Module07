from ex1.Creature import Creature
from ..HealCapability import HealCapability

class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> None:
        return "Bloomelle uses Petal Dance!"

    def heal(self) -> None:
        return "Bloomelle heals itself and others for a large amount"
    