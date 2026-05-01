from ex0.factory import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy, InvalidStrategyError

def battle(opponents_configs):
    print("*** Tournament ***")
    print(f"{len(opponents_configs)} opponents involved")
    
    players = []
    for factory, strategy in opponents_configs:
        creature = factory.create_base(factory.create_base("").__class__.__name__)
        players.append((creature, strategy))


    for i in range(len(players)):
        for j in range(i + 1, len(players)):
            c1, s1 = players[i]
            c2, s2 = players[j]
            
            print("\n* Battle *")
            print(c1.describe())
            print("vs.")
            print(c2.describe())
            print("now fight!")
            
            try:
                s1.act(c1)
                s2.act(c2)
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return

if __name__ == "__main__":
    # Tournament 0
    print("Tournament 0 (basic)")
    print("[ (Sandeed+Normal), (Zahra+Defensive) ]")
    battle([(FlameFactory(), NormalStrategy()), (HealingCreatureFactory(), DefensiveStrategy())])

    # Tournament 1
    print("\nTournament 1 (error)")
    print("[ (Sandeed+Aggressive), (Zahra+Defensive) ]")
    battle([(FlameFactory(), AggressiveStrategy()), (HealingCreatureFactory(), DefensiveStrategy())])

    # Tournament 2
    print("\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Zahrafawaaw+Defensive), (Transform+Aggressive) ]")
    battle([
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy())
    ])