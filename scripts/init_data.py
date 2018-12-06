import logging

from map.models import Map, Cell
from inventory.models import Inventory, Slot
from game.models import Crop, CropSpecies, CropSpeciesRewardDetail
from item.models import Item, ItemPrototype, KIT, SEED

logger = logging.getLogger(__name__)


def create_map():
    map = Map.objects.create()
    return map


def create_cell(map, x_size, y_size):
    cell_list = []

    for x in range(x_size):
        for y in range(y_size):
            cell_dict = {
                'map': map,
                'position_x': x,
                'position_y': y
            }
            cell = Cell(**cell_dict)
            cell_list.append(cell)

    Cell.objects.bulk_create(cell_list)
    logger.info(f'Create cells success!')


def create_inventory():
    inventory = Inventory.objects.create()
    return inventory


def create_slot(inventory):
    max_slot = inventory.max_slot
    for i in range(max_slot):
        Slot.objects.create(inventory=inventory)
    logger.info(f'Create slots success!')


def create_crop_species():
    crop_species_dict = {
        'name': '向日葵',
        'code': 'flower_001',
        'base_ripening_age': 75,
        'base_growing_speed': 1,
        'reward_generator': None
    }
    CropSpecies.objects.create(**crop_species_dict)
    crop_species_dict = {
        'name': '葡萄',
        'code': 'fluit_001',
        'base_ripening_age': 100,
        'base_growing_speed': 1,
        'reward_generator': None
    }
    CropSpecies.objects.create(**crop_species_dict)


def create_crop():
    cs_names = ['向日葵', '葡萄']
    cs_list = list(CropSpecies.objects.filter(name__in=cs_names).distinct('name'))
    for cs in cs_list:
        cs.create_crop()


def create_item_prototype():
    item_prototype_list = [
        {
            'name': '青龍偃月刀',
            'code': 'long_sword_001',
            'type': KIT,
            'store_price': 1000,
            'sold_price': 500,
            'reules': {'values': {'crop_species': 'flower_001'}},

        }, {
            'name': '向日葵種子',
            'code': 'seed_001',
            'type': SEED,
            'store_price': 2000,
            'sold_price': 1000,
        }, {
            'name': '葡萄種子',
            'code': 'seed_002',
            'type': SEED,
            'store_price': 2000,
            'sold_price': 1000,
            'reules': {'values': {'crop_species': 'fruilt_001'}},
        }
    ]
    ItemPrototype.objects.bulk_create(
        [ItemPrototype(**item_prototype_dict) for item_prototype_dict in item_prototype_list]
    )


def create_item():
    item_list = [
        {
            'name': '青龍偃月刀',
            'code': 'long_sword_001',
            'type': KIT,
            'store_price': 1000,
            'sold_price': 500,
        }, {
            'name': '向日葵種子',
            'code': 'seed_001',
            'type': SEED,
            'store_price': 2000,
            'sold_price': 1000,
            'values': {'crop_species': 'flower_001'},
        }, {
            'name': '葡萄種子',
            'code': 'seed_002',
            'type': SEED,
            'store_price': 2000,
            'sold_price': 1000,
            'values': {'crop_species': 'fluit_001'},
        }
    ]
    Item.objects.bulk_create(
        [Item(**item_dict) for item_dict in item_list]
    )


def create_crop_reward_detail():
    reward_list = [
        {
            'crop_species': CropSpecies.objects.get(code='flower_001'),
            'item_prototype': ItemPrototype.objects.get(code='seed_001'),
        }, {
            'crop_species': CropSpecies.objects.get(code='fluit_001'),
            'item_prototype': ItemPrototype.objects.get(code='seed_002')
        }
    ]
    CropSpeciesRewardDetail.objects.bulk_create([
        CropSpeciesRewardDetail(**reward_dict) for reward_dict in reward_list
    ])


def init_bag():
    items = Item.objects.all()
    for item in items:
        Inventory.objects.first().insert_item(item)
    logger.info(f'Init bag success!')


def main():
    map = create_map()
    create_cell(map, 5, 5)

    inventory = create_inventory()
    create_slot(inventory)

    create_crop_species()
    create_crop()

    create_item_prototype()
    create_item()

    create_crop_reward_detail()

    init_bag()