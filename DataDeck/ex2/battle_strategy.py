from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.Creatures_abilities import HealCapability, TransformCapability

class InvalidStrategyError(Exception):
    pass

class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass
    @abstractmethod
    def act(self, creature: Creature):
        pass

class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True
    
    def act(self, creature: Creature):
        try:
            if not self.is_valid(creature):
                raise InvalidStrategyError(f"Invalid Creature '{creature.name}' for this normal strategy")
        except InvalidStrategyError as e:
            print(e)
            return
        print(creature.attack())
        
class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)
    
    def act(self, creature: Creature):
        try:
            if not self.is_valid(creature):
                raise InvalidStrategyError(f"Invalid Creature '{creature.name}' for this aggressive strategy")
        except InvalidStrategyError as e:
            print(e)
            return
        
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())
class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)
    
    def act(self, creature: Creature) -> None:
        try:
            if not self.is_valid(creature):
                raise InvalidStrategyError(f"Invalid Creature '{creature.name}' for this defensive strategy")
        except InvalidStrategyError as e:
            print(e)
            return
        print(creature.attack())
        print(creature.heal())