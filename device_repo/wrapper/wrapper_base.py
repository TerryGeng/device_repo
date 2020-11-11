class BaseType:
    def checkedCast(self, *args):
        raise NotImplementedError

    def uncheckedCast(self, *args):
        raise NotImplementedError


class WrapperBase:
    base_type = BaseType

    def __init__(self, base):
        self.base = base

    def __getattr__(self, attr):
        if attr not in self.__dict__:
            return getattr(self.base, attr)
        else:
            return self.__dict__[attr]

    @classmethod
    def checkedCast(cls, proxy, facetOrContext=None, context=None):
        return cls(cls.base_type.checkedCast(proxy, facetOrContext, context))

    @classmethod
    def uncheckedCast(cls, proxy, facet=None):
        return cls(cls.base_type.uncheckedCast(proxy, facet))
