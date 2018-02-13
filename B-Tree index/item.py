class Item:
    # Class that represent an item
    #
    # Attributes:
    #   key     A key of this item
    #   value   A value of this item

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

    def key(self):
        return self.key

    def value(self):
        return self.value
