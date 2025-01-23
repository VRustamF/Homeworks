import inspect
from pprint import pprint

def introspection_info(obj):
    type_obj = type(obj).__name__
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and (attr[0:2]) != "__"]
    methods = [mthds for mthds in dir(obj) if callable(getattr(obj, mthds))]
    module_name = inspect.getmodule(obj).__name__ if inspect.getmodule(obj) is not None else 'builtins'

    info = {
        'type': type_obj,
        'attributes': attributes,
        'methods': methods,
        'module': module_name
    }

    return info

class RndmClass:
    def __init__(self):
        self.rndm_int = 100

    def my_method(self):
        return "Its my method"

my_obj = RndmClass()
object_info = introspection_info(my_obj)
str_info = introspection_info("Hello world!")
int_info = introspection_info(100)

pprint(object_info)
print()
pprint(str_info)
print()
pprint(int_info)
