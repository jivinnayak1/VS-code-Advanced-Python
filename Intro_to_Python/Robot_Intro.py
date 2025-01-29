class Robot:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hey, my name is {self.name} the robot!")

tom = Robot("Tom")
jerry = Robot("Jerry")
print("")
tom.introduce()
print("")
jerry.introduce()
print("")