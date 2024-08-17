from .abs_factory import AbsFactory

from autos.gm.spark import ChevySpark
from autos.gm.camaro import ChevyCamaro
from autos.gm.cadillac import CadillacCTS

class GMFactory(AbsFactory):

    @staticmethod
    def create_economy():
        return ChevySpark()

    def create_sport():
        return ChevyCamaro()

    def create_luxury():
        return CadillacCTS()

