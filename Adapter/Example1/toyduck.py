from Adapter.Example1.sparrow import Sparrow
from Adapter.Example1.plastictoyduck import PlasticToyDuck
from Adapter.Example1.birdadapter import BirdAdapter



class ToyDuck:
    def squeak(self):
        pass


if __name__ == '__main__':
    sparrow = Sparrow()
    toy_duck = PlasticToyDuck()
    bird_adapter = BirdAdapter(sparrow)

    sparrow.fly()
    sparrow.make_sound()

    toy_duck.squeak()
    bird_adapter.squeak()