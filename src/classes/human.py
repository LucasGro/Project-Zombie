class Human(Character):
    def __init__(self, x, y, velocity, power, n_killed=0):
        super().__init__(x, y, velocity, power)
        self.n_killed = n_killed

    def __str__(self):
        return "Human"

    def __repr__(self):
        return f"Human(x={self.x}, y={self.y}, velocity={self.velocity}, power={self.power}, " \
               f"n_killed={self.n_killed})"

    def choose_new_position(self, zombies):  # zombies ->  [ Zombie(), Zombie(), Zombie()   ]
        delta_x = random.random() * self.velocity
        delta_y = random.random() * self.velocity
        return delta_x, delta_y