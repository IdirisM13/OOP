class Camera:
    def camera_method(self):
        print("Это родительский метод из класса Camera")

class Radio:
    def radio_method(self):
        print("Это родительский метод из класса Radio")

class CellPhone(Camera, Radio):
    def cell__phone_method(self):
        print("Это дочерний метод из ксласса CellPhone")
obj = CellPhone()
obj.cell__phone_method()
obj.camera_method()
obj.radio_method()

