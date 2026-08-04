from ex0 import Aqua, Flame


def test() -> None:
    print("Testing factory")
    factory1 = Aqua()
    base = factory1.create_base()
    evolved = factory1.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())
    print("\nTesting factory")
    factory2 = Flame()
    base_2 = factory2.create_base()
    evolved_2 = factory2.create_evolved()
    print(base_2.describe())
    print(base_2.attack())
    print(evolved_2.describe())
    print(evolved_2.attack())
    print("\nTesting battle")
    print(base.describe())
    print(" vs.")
    print(base_2.describe())
    print(" fight!")
    print(base.attack())
    print(base_2.attack())


if __name__ == "__main__":
    test()
