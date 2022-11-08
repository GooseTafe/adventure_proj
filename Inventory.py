class Inventory:
    def __init__(self):
        self.items = ["test1", "test2", "test3", "money"]

    # Binary search through inventory
    def search_inventory(self, item):
        sorted_items = sorted(self.items)
        start = 0
        end = len(sorted_items) - 1

        while start <= end:
            middle = int((start + end) / 2)
            midpoint = sorted_items[middle]
            if midpoint > item:
                end = middle - 1
            elif midpoint < item:
                start = middle + 1
            else:
                return midpoint

    def add_item(self, new_item):
        self.items.append(new_item)

    def remove_item(self, removed_item):
        self.items.remove(removed_item)
