from ..CreatureFactory import CreatureFactory
from .Transforming import Morphagon, Shiftling

class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> "Shiftling":
        return Shiftling()

    def create_evolved(self) -> "Morphagon":
        return Morphagon()