from .creature import Creature
from .models import Sandeed, Jalmud, Roma7, Samhar
from abc import ABC, abstractmethod

class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self, name: str) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self, name: str) -> Creature:
        pass

class FlameFactory(CreatureFactory):
    def create_base(self, name: str) -> Creature:
        return Sandeed(name)

    def create_evolved(self, name: str) -> Creature:
        return Jalmud(name)

class AquaFactory(CreatureFactory):
    def create_base(self, name: str) -> Creature:
        return Roma7(name)

    def create_evolved(self, name: str) -> Creature:
        return Samhar(name)