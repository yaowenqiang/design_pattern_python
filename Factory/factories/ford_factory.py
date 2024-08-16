from .abs_factory import AbstractFactory
from autos.fordfusion import FordFusion

class FordFactory(AbstractFactory):
    def create_auto(self):
        self.ford = ford = FordFusion()
        ford.name = 'Ford Fusion'
        return ford