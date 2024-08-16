import abc
class AbsAuto(abc.ABC):

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @abc.abstractmethod
    def start(self):
        pass
    @abc.abstractmethod
    def stop(self):
        pass