from collections import MutableMapping
import json
from model.toolkit import WRpickle


class MetaDict(MutableMapping):
    """A dictionary that applies an arbitrary key-altering
       function before accessing the keys"""

    def __init__(self, *args, **kwargs):
        self.store = dict()
        self.update(dict(*args, **kwargs))  # use the free update to set keys

    def __getitem__(self, key):
        return self.store[key]

    def __setitem__(self, key, value):
        self.store[key] = value

    def __delitem__(self, key):
        del self.store[key]

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)

    def __str__(self):
        return  self.store.__str__()

class Singleton(type):
        _instances = {}
        def __call__(cls, *args, **kwargs):
            if cls not in cls._instances:
                cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
            return cls.__instances[cls]
"""
#python2
class MyClass(BaseClass):
        __metaclass__ = Singleton
#python3
class MyClass(BaseClass, metaclass = Singleton):
"""

def singleton(class_):
    instance = {}
    def getinstance(*args,**kwargs):
        if class_ not in instance:
            instance[class_] = class_(*args,**kwargs)
        return instance[class_]
    return getinstance


@singleton
class SETTING(MetaDict):
    """docstring for PickContext"""
    def __init__(self, ParaDict = {}):
        MetaDict.__init__(self)
        if not ParaDict:
            print("set SETTING to default")
        getSettingID = json.dumps(ParaDict)


    def getSetting(self):








