import time

from visualization import visualize_simulation
from fight_functions import find_all_pairs_about_to_clash, calculate_n_of_rivals, \
    carry_out_clashes, implement_results


def run_simulation(humans, zombies, map2d):
    t = 0
    while True:
        t += 1
        # time.sleep(.5)
        if t % 1 == 0:
            visualize_simulation(humans, zombies, map2d, t)

        # Choose new position
        humans_displacements = []
        for human in humans:
            delta_x, delta_y = human.choose_new_position(zombies)
            humans_displacements.append((delta_x, delta_y))

        zombies_displacements = []
        for zombie in zombies:
            delta_x, delta_y = zombie.choose_new_position(humans)
            zombies_displacements.append((delta_x, delta_y))

        # Move
        for human, displacement in zip(humans, humans_displacements):
            human.move(*displacement)

        for zombie, displacement in zip(zombies, zombies_displacements):
            zombie.move(*displacement)

        # Fight
        clash_pairs = find_all_pairs_about_to_clash(humans, zombies)
        rivals_number = calculate_n_of_rivals(humans, zombies, clash_pairs)
        victories, loosers = carry_out_clashes(humans, zombies, clash_pairs, rivals_number, t)
        implement_results(humans, zombies, victories, loosers)

        if len(humans) < 1 or len(zombies) < 1 or t > 1000:
            visualize_simulation(humans, zombies, map2d, t, clf=False)
            print(f"Ludzi: {len(humans)}")
            print(f"Zombie: {len(zombies)}")
            break

    return 1
