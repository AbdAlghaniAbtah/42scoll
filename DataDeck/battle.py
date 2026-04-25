from ex0 import AquaFactory, FlameFactory

def main():
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    char1 = flame_factory.create_base("Sandeed")
    char2 = flame_factory.create_evolved("Jalmud")
    char3 = aqua_factory.create_base("Roma7")
    char4 = aqua_factory.create_evolved("Samhar")

    print("Testing factory")
    print(char1.describe())
    print(char1.attack())
    print(char2.describe())
    print(char2.attack())
    print("\nTesting factory")
    print(char3.describe())
    print(char3.attack())
    print(char4.describe())
    print(char4.attack())
    print("\nTesting battle")
    print(f"{char1.describe()} vs {char3.describe()}")
    print(char1.attack())
    print(char3.attack())
    
if __name__ == "__main__":
    main()