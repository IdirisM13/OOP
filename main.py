# public
# private -> __
# protect -> _


class Person:
    def __init__(self):
        self.name = "Asan"#  public
        self.__password = "12345" # private
        self._year = 2000 #protect

    def get_password(self):
        return self.__password

    def set_password(self, password):
            self.__password = password

obj = Person()
print(obj.name)
print(obj._year)
print(obj.get_password())
obj.set_password("123")
print(obj.get_password())
