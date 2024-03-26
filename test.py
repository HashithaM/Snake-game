class Animal:
    def __init__(self):
        self.num_of_eyes = 2

    def breath(self):
        print("Exhale and Inhale.")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breath(self):
        super().breath()
        print("Do this under water.")

    def swim(self):
        print("Move in water.")


nemo = Fish()
nemo.swim()
nemo.breath()
print(nemo.num_of_eyes)
