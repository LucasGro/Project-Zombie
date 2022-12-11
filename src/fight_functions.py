import numpy as np
from classes.zombie import Zombie


def find_all_pairs_about_to_clash(humans, zombies):
    '''
    The function will accept these two lists as arguments
    and return a list of pairs of characters that will have to fight.
    The criterion for a given human-zombie pair to fight in a given iteration is
    that the distance between them is less than a certain value, 3.
    Character identifiers are their indices on the lists.

    Args:
        humans (list or tuple): a list of humans with their current position
        zombies (list or tuple): a list of zombies with their current position

    Returns:
        (list of tuple): returns list of humans and zombies who will have to fight

    >>> humans = [(1, 0), (10, 40), (0, 1)]
    >>> zombies = [(30, 50), (0, 0)]
    >>> find_all_pairs_about_to_clash(humans, zombies)
    [(0, 1), (2, 1)]
    '''

    list_out = []
    for h, human in enumerate(humans):
        for z, zombie in enumerate(zombies):
            dist = ((zombie.x - human.x) ** 2 + (zombie.y - human.y) ** 2) ** 0.5
            if dist <= 3:
                list_out.append((h, z))
    return list_out


def calculate_n_of_rivals(humans, zombies, clash_pairs):
    '''

    >>> humans = [(1, 0), (10, 40), (0, 1)]
    >>> zombies = [(30, 50), (0, 0)]
    >>> clash_pairs = [(0, 1), (2, 1)]
    >>> calculate_n_of_rivals(humans, zombies, clash_pairs)
    {'humans': [1, 0, 1], 'zombies': [0, 2]}
    '''

    result = {"humans": [0 for h in humans], "zombies": [0 for z in zombies]}
    for cp in clash_pairs:
        result["humans"][cp[0]] += 1
        result["zombies"][cp[1]] += 1

    return result


def carry_out_clashes(humans, zombies, clash_pairs, rivals_number, t):
    """
    Calculates number of humans' victories and zombies which lost a battle
    """

    victories = {"humans": [0 for _ in humans], "zombies": [0 for _ in zombies]}
    loosers = {"humans": [], "zombies": []}
    single_iter_human_victories = 0
    single_iter_zombie_victories = 0
    for pair in clash_pairs:
        h = pair[0]
        z = pair[1]
        result \
            = np.sign((humans[h].power + humans[h].n_killed) / rivals_number["humans"][h]
                      - (zombies[z].power + zombies[z].n_infected) / rivals_number["zombies"][z])

        if result == 1:
            victories["humans"][h] += 1
            loosers["zombies"].append(z)
            print(f"human winner in {t} iteration")
            single_iter_human_victories += 1
        else:
            victories["zombies"][z] += 1
            loosers["humans"].append(h)
            print(f"zombie winner in {t} iteration")
            single_iter_zombie_victories += 1

    return victories, loosers


def implement_results(humans, zombies, victories, loosers):
    """
    For each character performs an action such as a battle with an opponent.
    Returns the state of characters after all fights.
    """

    # Increase n_killed and n_infected
    for human, human_result in zip(humans, victories["humans"]):
        human.n_killed += human_result

    for zombie, zombie_result in zip(zombies, victories["zombies"]):
        zombie.n_infected += zombie_result

    # Remove killed zombies and turn infected humans into zombies
    # killed_zombies = loosers["zombies"].copy()
    killed_zombies = list(set(loosers["zombies"]))
    killed_zombies.sort(reverse=True)
    # killed_zombies.reverse()

    for zombie_index in killed_zombies:
        zombies.pop(zombie_index)

    # ---
    infected_humans = list(set(loosers["humans"]))
    infected_humans.sort(reverse=True)

    for human_index in infected_humans:
        h = humans[human_index]
        humans.pop(human_index)
        zombies.append(Zombie(x=h.x, y=h.y, velocity=h.velocity, power=h.power))

