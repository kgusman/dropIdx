class Item:
    # Class that represent an item
    #
    # Attributes:
    #   key     A key of this item
    #   value   A value of this item

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

    def get_key(self):
        return self.key

    def get_value(self):
        return self.value