from ..CreatureFactory import CreatureFactory
from ..Creatures import Flameling
from ..Creatures import Pyrodon


class FlameFactory(CreatureFactory):
    def create_base(self) -> "Flameling":
        return Flameling("Flameling", "Fire")

    def create_evolved(self) -> "Pyrodon":
        return Pyrodon("Pyrodon", "Fire/Flying")
