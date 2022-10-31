from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, list_inventory):
        self._list_inventory = list_inventory
        self._index = 0

    def __next__(self):
        try:
            data = self._list_inventory[self._index]
        except IndexError:
            raise StopIteration()
        else:
            self._index += 1
            return data
