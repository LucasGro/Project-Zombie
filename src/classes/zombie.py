import numpy as np
from src.classes.common import Character
class Zombie(Character):
    def __init__(self, x, y, velocity, power, n_killed=0):
        super().__init__(x, y, velocity, power)
        self.n_killed = n_killed

    def choose_new_position(self, humans):  # humans ->  [ Zombie(), Zombie(), Zombie()   ]

        vector_to_humans = [np.array([h.x - self.x, h.y - self.y]) for h in humans]
        vector_to_humans_norm = [v / (np.linalg.norm(v) + 0.0000001) for v in vector_to_humans]
        weighted_vector = [vn * (self.power + self.killed) - vn * (h.power + h.n_killed)
                           for vn, h in zip(vector_to_humans_norm,
                                            humans)]  # przeiterowanie po wszystkich zombie i wszystkich wectorach
        sum_weight_vector = sum(weighted_vector)
        normalized_vector_sum = sum(weighted_vector / (np.lingalg.norm(sum_weight_vector) + 0.00001)) * self.velocity

        # delta_x = 2 * np.random.random() -1
        # delta_y = (1 - delta_x ** 2) ** 0.5 * (1 if np.random.random() > 0.5 else -1)
        #
        # delta_x *= self.velocity
        # delta_y *= self.velocity

        return normalized_vector_sum[0], normalized_vector_sum[1]