from inspect import getmembers, isclass, isabstract
import autos

class AutoFactory:
    autos = {}

    def __init__(self) -> None:
        self.load_autos()
    
    def load_autos(self):
        classes = getmembers(autos, 
                             lambda m: isclass(m) and not isabstract(m))
        for name, _type in classes:
            if isclass(_type) and issubclass(_type, autos.AbsAuto):
                self.autos.update([[name, _type]])
    
    def create_instance(self, carname):
        if carname in self.autos:
            return self.autos[carname]()
        else:
            return autos.NullCar(carname)