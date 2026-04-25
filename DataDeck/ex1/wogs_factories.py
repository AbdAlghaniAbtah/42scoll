from ex0.factory import CreatureFactory
from .creatures import Eiqab, Jarih, Zahra, Farasha

class HealingCreatureFactory(CreatureFactory):
    def create_base(self, name: str) -> CreatureFactory:
        return Zahra(name)

    def create_evolved(self, name: str) -> CreatureFactory:
        return Farasha(name)
    
class TransformCreatureFactory(CreatureFactory):
    def create_base(self, name: str) -> CreatureFactory:
        return Jarih(name)

    def create_evolved(self, name: str) -> CreatureFactory:
        return Eiqab(name)
