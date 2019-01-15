class stack:

    def __init__(self):
        self.items = []

    def push(self, new_item):
        self.items += [new_item]
        return True

    def pop(self):
        popped_item = self.items[len(self.items) - 1]
        self.items = self.items[0:len(self.items) - 1]
        return popped_item

    def show(self):  # not needed, just here for debugging
        print(self.items)
        return True
