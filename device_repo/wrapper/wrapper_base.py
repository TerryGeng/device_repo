class WrapperBase:
    def __init__(self, base):
        self.base = base

    def __getattr__(self, attr):
        if attr not in self.__dict__:
            return getattr(self.base, attr)
        else:
            return self.__dict__[attr]
