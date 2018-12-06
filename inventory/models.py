import collections

from django.db import models

from item.models import Item


class Inventory(models.Model):
    UNDEFINED = 0
    NOT_FULL = 1
    FULL = 2
    STATUS_OPTIONS = (
        (UNDEFINED, 'Undefined'),
        (NOT_FULL, 'Not_full'),
        (FULL, 'Full'),
    )

    max_slot = models.IntegerField(default=12)

    def insert_item(self, item):
        print(item)
        if not isinstance(item, Item):
            return False

        first_blank_slot = self.is_not_full()
        print(f'first_blank_slot: {first_blank_slot}')
        if not first_blank_slot:
            return False
        first_blank_slot.item = item
        first_blank_slot.save()
        print('return True')
        return True

    def insert_item_list(self, item_list):
        if not isinstance(item_list, collections.Iterable):
            return False
        item_list = list(item_list)
        while len(item_list) != 0:
            # TODO: Handle the case that bags' full before all the items inserted into it
            print('in while loop')
            item = item_list.pop()
            if not self.insert_item(item):
                return False
        return True

    def fetch_item(self, slot: 'Slot'):
        # return Item object if the action success, else False
        if slot not in self.slots:
            return False
        if not slot.item:
            return False
        item = slot.item
        slot.item = None
        return item

    def is_not_full(self):
        # return False if there is no blank slot, else return the first blank slot
        first_blank_slot = self.slots.all().filter(item__isnull=True).order_by('id').first()
        if first_blank_slot:
            return first_blank_slot
        return False


class Slot(models.Model):
    inventory = models.ForeignKey(Inventory, related_name='slots', on_delete=models.CASCADE)
    item = models.OneToOneField(Item, related_name='slot', blank=True, null=True,
                                on_delete=models.SET_NULL)


