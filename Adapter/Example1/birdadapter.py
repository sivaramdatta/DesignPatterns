from Adapter.Example1.toyduck import ToyDuck


class BirdAdapter(ToyDuck):
	
	def __init__(self,bird):
		self.bird = bird

	def squeak(self):
		self.bird.make_sound()
