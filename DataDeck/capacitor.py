from ex1 import HealingCreatureFactory, TransformCreatureFactory

def main():
    print("Testing Creature with healing capability\nbase: ")
    zahra = HealingCreatureFactory().create_base("Zahra")
    farasha = HealingCreatureFactory().create_evolved("Farasha")
    jarih = TransformCreatureFactory().create_base("Jarih")
    eiqab = TransformCreatureFactory().create_evolved("Eiqab")
    print(zahra.describe())
    print(zahra.attack())
    print(zahra.heal())
    print("evolved:")
    print(farasha.describe())
    print(farasha.attack())
    print(farasha.heal())
    print("\nTesting Creature with transform capability\nbase:")
    print(jarih.describe())
    print(jarih.attack())
    print(jarih.transform())
    print(jarih.attack())
    print(jarih.revert())
    print("evolved:")
    print(eiqab.describe())
    print(eiqab.attack())
    print(eiqab.transform())
    print(eiqab.attack())
    print(eiqab.revert())


if __name__ == "__main__":
    main()