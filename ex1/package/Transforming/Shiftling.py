from ex1.Creature import Creature
from ..TransformCapability import TransformCapability

class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")
        self._is_transformed = False

    def attack(self) -> None:
        if not self._is_transformed:
            return "Shiftling attacks normally."
        else:
            return "Shiftling performs a boosted strike!"
    
    def transform(self) -> None:
        self._is_transformed = True
        return "Shiftling shifts into a sharper form!"
    
    def revert(self) -> None:
        self._is_transformed = False
        return "Shiftling returns to normal."