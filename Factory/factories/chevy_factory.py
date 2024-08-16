from .abs_factory import AbstractFactory
from autos.chevyvolt import ChevyVolt

class ChevyFactory(AbstractFactory):
    def create_auto(self):
        self.chevy = chevy = ChevyVolt()
        chevy.name = 'Chevy Volt'
        return chevy