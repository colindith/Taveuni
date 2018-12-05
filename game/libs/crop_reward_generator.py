import logging

import numpy as np

from game.models import CropSpecies

logger = logging.getLogger(__name__)


def default_generator(reward_choices_list, **kwargs):
    print(f'reward_choices_list: {reward_choices_list}')
    if not reward_choices_list:
        logger.error(f'base_bet_set_generator Error: reward_choices_list not defined.')
        return
    length = kwargs.get('length', 1)
    sort = kwargs.get('sort')

    reward_choose_list = np.random.choice(reward_choices_list, size=length, replace=False)

    if sort:
        reward_choose_list.sort()

    reward_list = [reward_choose.generate_item() for reward_choose in reward_choose_list]
    print(f'reward_list: {reward_list}')
    return reward_list
