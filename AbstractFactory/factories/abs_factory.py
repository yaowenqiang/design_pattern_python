import abc
class AbsFactory(abc.ABC):
    """
    Abstract factory interface
    """
    @abc.abstractmethod
    def create_economy():
        pass

    @abc.abstractmethod
    def create_sport():
        pass

    @abc.abstractmethod
    def create_luxury():
        pass