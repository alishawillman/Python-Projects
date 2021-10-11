



#Creating a protected variable

class Protected:
    def __init__(self):
        self._protectedVar = 0

obj = Protected()
obj._protectedVar = "Hello World,"
print(obj._protectedVar)


#Creating a private variable

class Protected:
    def __init__(self):
        self.__privateVar = "My name is Alisha!"

        
    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.privateVar = private

obj = Protected()
obj.getPrivate()
            
