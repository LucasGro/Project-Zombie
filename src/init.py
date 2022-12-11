import json
import numpy as np

from classes.human import Human
from classes.zombie import Zombie


def initialize():
    with open("conf/human.json") as f:
        human_config = json.load(f)

    with open("conf/zombie.json") as f:
        zombie_config = json.load(f)

    humans = []
    zombies = []

    for _ in range(human_config["initial_number"]):
        x = np.random.normal(*human_config["x"])
        y = np.random.normal(*human_config["y"])
        velocity = np.random.normal(*human_config["velocity"])
        power = np.random.normal(*human_config["power"])

        single_human = Human(x=x, y=y, velocity=velocity, power=power)
        humans.append(single_human)

    for _ in range(zombie_config["initial_number"]):
        x = np.random.normal(*zombie_config["x"])
        y = np.random.normal(*zombie_config["y"])
        velocity = np.random.normal(*zombie_config["velocity"])
        power = np.random.normal(*zombie_config["power"])

        single_zombie = Zombie(x=x, y=y, velocity=velocity, power=power)
        zombies.append(single_zombie)

    return humans, zombies
