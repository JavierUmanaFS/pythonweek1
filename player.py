class Player:
    def __init__(self, name, current_room, items):
        self.name = name
        self.current_room = current_room
        self.items = items

    def inventory(self):
        if len(self.items) > 0:
            print(f"Inventory: {self.items}")
        else:
            print("No items in inventory!")

    def pick_up_item(self, item):
        self.items.append(item)
        print([i.name for i in self.items[0]])

    def drop_item(self, item):
        self.items = [filter(lambda a: a.name is not item.name, self.items)]

        
    def __str__(self):
        return f"Player Name: {self.name}, {self.current_room}"