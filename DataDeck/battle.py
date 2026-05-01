from ex0 import AquaFactory, FlameFactory

def main():
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    Sandeed = flame_factory.create_base("Sandeed")
    Jalmud = flame_factory.create_evolved("Jalmud")
    Roma7 = aqua_factory.create_base("Roma7")
    Samhar = aqua_factory.create_evolved("Samhar")

    print("Testing factory")
    print(Sandeed.describe())
    print(Sandeed.attack())
    print(Jalmud.describe())
    print(Jalmud.attack())
    print("\nTesting factory")
    print(Roma7.describe())
    print(Roma7.attack())
    print(Samhar.describe())
    print(Samhar.attack())
    print("\nTesting battle")
    print(f"{Sandeed.describe()} vs {Roma7.describe()}")
    print(Sandeed.attack())
    print(Roma7.attack())

if __name__ == "__main__":
    main()