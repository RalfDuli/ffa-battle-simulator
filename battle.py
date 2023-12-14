import time
import numpy as np

from military import *


def battle(militaries: list):
    """
    :param militaries: A list of militaries of type Military.

    Simulates a free-for-all battle between a variable number
    of militaries using a generalization of Lanchester's Square
    Law.
    """

    mils = np.array(militaries)

    num_militaries = len(mils)

    military_numbers = []
    military_firepowers = []
    for i in range(num_militaries):
        military_numbers.append(mils[i].get_num_troops())
        military_firepowers.append(mils[i].get_firepower())

    firepower_matrix = np.diag(military_firepowers)

    conflict_matrix = np.ones((num_militaries, num_militaries))
    np.fill_diagonal(conflict_matrix, 0)
    conflict_matrix /= (num_militaries - 1)

    change_in_num_troops = -(conflict_matrix @ firepower_matrix @ military_numbers)
    military_numbers += change_in_num_troops

    is_military_defeated = military_numbers > 0
    military_numbers[~is_military_defeated] = 0


    # is_military_defeated = military_numbers < 0
    # mils = np.array(
    #     [military for military, defeated in zip(mils, is_military_defeated) if not defeated]
    # )
    # military_numbers = military_numbers[~is_military_defeated]

    print('MILITARY NUMBERS:', military_numbers)
    time.sleep(0.2)


battle([Military('A',1000, 1),
        Military('B',2000, 0.5),
        Military('C',600, 2)])
