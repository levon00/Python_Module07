from ..CreatureFactory import CreatureFactory
from ..Creatures import Aquabub
from ..Creatures import Torragon


class AquaFactory(CreatureFactory):
    def create_base(self) -> "Aquabub":
        return Aquabub("Aquabub", "Water")

    def create_evolved(self) -> "Torragon":
        return Torragon("Torragon", "Water")
