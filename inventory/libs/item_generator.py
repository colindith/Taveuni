import logging

import numpy as np

from inventory.models import Item

logger = logging.getLogger(__name__)


def default_generator(item_prototype, **kwargs):
    print(f'item_prototype: {item_prototype}')

    item_dict = {
        'name': item_prototype.name,
        'code': item_prototype.code,
        'type': item_prototype.type,
        'store_price': item_prototype.store_price,
        'sold_price': item_prototype.sold_price,
        'values': kwargs.get('values')
    }

    return Item.objects.create(**item_dict)
