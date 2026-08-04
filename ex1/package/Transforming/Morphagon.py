from ex1.Creature import Creature
from ..TransformCapability import TransformCapability

class Morphagon(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Morphagon", "Normal/Dragon")
        self._is_transformed = False

    def attack(self) -> None:
        if not self._is_transformed:
            return "Morphagon attacks normally."
        else:
            return "Morphagon unleashes a devastating morph strike!"
        
    def transform(self) -> None:
        self._is_transformed = True
        return "Morphagon morphs into a dragonic battle form!"
    
    def revert(self) -> None:
        self._is_transformed = False
        return "Morphagon stabilizes its form."
