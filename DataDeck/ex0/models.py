
from .creature import Creature

class Sandeed(Creature):
    def __init__(self, name: str):
        super().__init__(name, "Fire")
    
    def attack(self) -> str:
        return f"{self.name}  uses Flamethrower!"
    

class Jalmud(Creature):
    def __init__(self, name: str):
        super().__init__(name, "Fire/Flying")
    def attack(self) -> str:
        return f"{self.name} uses fire tornado!"
    
class Roma7(Creature):
    def __init__(self, name: str):
        super().__init__(name, "Water")

    def attack(self) -> str:
        return f"{self.name} uses Water Claw !"
    
class Samhar(Creature):
    def __init__(self, name: str):
        super().__init__(name, "Water/Flying")
    
    def attack(self) -> str:
        return f"{self.name} uses Water rockets"
