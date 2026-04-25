
from ex0 import AquaFactory, FlameFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    NormalStrategy, 
    AggressiveStrategy, 
    DefensiveStrategy, 
    InvalidStrategyError
)

def main():
    sandeed = FlameFactory().create_base("Sandeed")
    zahra = HealingCreatureFactory().create_base("Zahra")
    strategy_sandeed = NormalStrategy()
    strategy_zahra = DefensiveStrategy()
    print("Tournament 0 (basic)")
    print("[(Sandeed+Normal), (zahra+Defensive)]")
    print("*** Tournament ***")
    print("2 opponents involved\n")
    print(sandeed.describe() + " vs " + zahra.describe())
    print("now fight!")
    print(strategy_sandeed.act(sandeed, zahra))
    print(strategy_zahra.act(zahra, sandeed))
    
    
if __name__ == "__main__":
    main()