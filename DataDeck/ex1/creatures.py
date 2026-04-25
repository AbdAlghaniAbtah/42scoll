from ex0.creature import Creature
from .Creatures_abilities import HealCapability, TransformCapability

class Zahra(Creature, HealCapability):
    def __init__(self, name: str):
        super().__init__(name, "Grass")
    
    def attack(self) -> str:
        return f"{self.name} uses Leaf Blade!"
    
    def heal(self) -> str:
        return f"{self.name} heals itself for a small amount"

class Farasha(Creature, HealCapability):
    def __init__(self, name: str):
        super().__init__(name, "Grass/Fairy")

    def attack(self) -> str:
        return f"{self.name} uses Solar Beam!"

    def heal(self) -> str:
        return f"{self.name}  heals itself and others for a large amount"

class Jarih(Creature, TransformCapability):
    def __init__(self, name: str):
        Creature.__init__(self, name, "Normal")
        TransformCapability.__init__(self)

    def transform(self) -> str:
        self._is_transformation = True
        return f"{self.name} transforms into its alternate form!"
    def revert(self) -> str:
        self._is_transformation = False
        return f"{self.name} reverts to its original form!"
    def attack(self) -> str:
        if self._is_transformation:
            return f"{self.name} unleashes a devastating Supernova Strike!"
        
        return f"{self.name} It launches fiery meteors from its wings."

class Eiqab(Creature, TransformCapability):
    def __init__(self, name: str):
        Creature.__init__(self ,name, "Super")
        TransformCapability.__init__(self)

    def transform(self) -> str:
        self._is_transformation = True
        return f"{self.name} transforms into its alternate form!"

    def revert(self) -> str:
        self._is_transformation = False
        return f"{self.name} reverts to its original form!"
    def attack(self) -> str:
        if self._is_transformation:
            return f"{self.name} sounds the cry of vanishing"
        
        return f"{self.name} unleashes Fiery claws of justice"