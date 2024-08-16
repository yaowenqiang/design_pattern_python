from importlib import import_module
from inspect import getmembers, isclass, isabstract
from .abs_factory import AutoFactory

def load_factory(factory_name):
    try:
        factory_module = import_module(f'.{factory_name}', 'factories')
    except ImportError:
        factory_module = import_module(f'.{null_factory}', 'factories')
    
    classes = getmembers(factory_module, 
                         lambda m: isclass(m) and not isabstract(m))
    for name, _class in classes:
        if isclass(_class) and issubclass(_class, AutoFactory):
            return _class
    return AutoFactory
