import json
import numpy as np
from classes.human import Human
from classes.zombie import Zombie


def initialize():
    with open("../conf/human.json", "r") as file:
        human_config = json.load(file)

    with open("../conf/zombie.json", "r") as file:
        zombie_config = json.load(file)

    human_list = []
    zombie_list = []

    for i in range(human_config["initial_number"]):
        # x = np.random.normal(human_config["x"][0], human_config["x"][1])
        x = np.random.normal(*human_config["x"])
        y = np.random.normal(*human_config["y"])
        velocity = np.random.normal(*human_config["velocity"])
        power = np.random.normal(*human_config["power"])
        h = Human(x, y, velocity, power)
        human_list.append(h)


    for i in range(zombie_config["initial_number"]):
        # x = np.random.normal(zombie_config["x"][0], zombie_config["x"][1])
        x = np.random.normal(*zombie_config["x"])
        y = np.random.normal(*zombie_config["y"])
        velocity = np.random.normal(*zombie_config["velocity"])
        power = np.random.normal(*zombie_config["power"])
        z = Zombie(x, y, velocity, power)
        zombie_list.append(z)

    return human_list, zombie_list


print(initialize())
