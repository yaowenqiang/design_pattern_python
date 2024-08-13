import abc

class MyABC(abc.ABC):
    """ Abstract Base Class definition"""

    @abc.abstractclassmethod
    def do_something(self, value):
        """Required method"""
    
    @abc.abstractproperty
    def some_property(self):
        """Required property"""

class MyClass(MyABC):
    def __init__(self, value=None):
        self._myprop = value

    def do_something(self, value):
        self._myprop += value

    @property
    def some_property(self):
        self._myprop
