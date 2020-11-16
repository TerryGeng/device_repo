class BaseType:
    def checkedCast(self, *args):
        raise NotImplementedError

    def uncheckedCast(self, *args):
        raise NotImplementedError


class WrapperBase:
    base_type = BaseType

    def __init__(self, base):
        self.base = base

        my_attr = dir(self)
        for attr in dir(base):
            if not attr.startswith("__") and attr not in my_attr:
                self.__setattr__(attr, getattr(base, attr))

    @classmethod
    def checkedCast(cls, proxy, facetOrContext=None, context=None):
        return cls(cls.base_type.checkedCast(proxy, facetOrContext, context))

    @classmethod
    def uncheckedCast(cls, proxy, facet=None):
        return cls(cls.base_type.uncheckedCast(proxy, facet))
