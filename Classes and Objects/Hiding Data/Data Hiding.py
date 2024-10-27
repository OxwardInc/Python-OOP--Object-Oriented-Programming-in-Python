class Product:
    def __init__(self):
        self.data1 = 10
        self._data2 = 20
    
    def methodA(self):
        pass

    def _methodB(self):
        pass

p = Product()

class Product:
    def __init__(self):
        self.data1 = 10
        self.__data2 = 20
    
    def methodA(self):
        pass

    def __methodB(self):
        pass

p = Product()