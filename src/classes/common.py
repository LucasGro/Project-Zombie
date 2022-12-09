class Character:
    def __init__(self, x, y, velocity, power):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.power = power

    def move(self, delta_x, delta_y):
        self.x = x + delta_x
        self.y = y + delta_y
