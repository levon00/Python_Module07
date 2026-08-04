from ..CreatureFactory import CreatureFactory
from .Healing import Sproutling, Bloomelle

class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> "Sproutling":
        return Sproutling()
    
    def create_evolved(self) -> "Bloomelle":
        return Bloomelle()
    