import numpy as np
from src.classes.common import Character


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

        vector_to_zombies = [np.array([z.x - self.x, z.y - self.y]) for z in zombies]
        vector_to_zombies_norm = [v / (np.linalg.norm(v) + 0.0000001) for v in vector_to_zombies]
        weighted_vector = [vn * (self.power + self.n_killed) - vn * (z.power + z.n_infected)
                           for vn, z in zip(vector_to_zombies_norm, zombies)]
        sum_weight_vector = sum(weighted_vector)
        normalized_vector_sum = sum_weight_vector / (np.lingalg.norm(sum_weight_vector) + 0.00001) * self.velocity

        # delta_x = 2 * np.random.random() -1
        # delta_y = (1 - delta_x ** 2) ** 0.5 * (1 if np.random.random() > 0.5 else -1)
        #
        # delta_x *= self.velocity
        # delta_y *= self.velocity

        return normalized_vector_sum[0], normalized_vector_sum[1]


human = Human(0, 0, 5, 5)
zombies = [(10, 12), (12, 14)]
