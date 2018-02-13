import time
import random
import string

from item import Item
from btreeindex import BtreeIndex

# Constants are defined below
DATA_SIZE = 20
LIST_SIZE = 20000


def generate_item_list(_size):
    return [Item(100-x, ''.join(random.choice(string.ascii_letters) for _ in range(DATA_SIZE))) for x in range(_size)]


def search(_item_list, _item):
    for i, p in enumerate(_item_list):
        if p.key == _item.key:
            return i


def build_btree_index(_item_list):
    index = BtreeIndex()
    [index.insert(x, i) for i, x in enumerate(_item_list)]

    return index

item_list = generate_item_list(LIST_SIZE)
item = item_list[random.randint(len(item_list) / 2, len(item_list) - 1)]

start = time.time()
search(item_list, item)
end = time.time()

time_no_index = end - start

btree_index = build_btree_index(item_list)

start = time.time()
btree_index.search(item)
end = time.time()

time_index = end - start

print(time_no_index)
print(time_index)

assert time_index < time_no_index, 'Your implementation sucks!'
