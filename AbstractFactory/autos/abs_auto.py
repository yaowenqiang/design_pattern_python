import abc
class AbsAuto(abc.ABC):
    @abc.abstractmethod
    def start():
        pass


    @abc.abstractmethod
    def stop():
        pass