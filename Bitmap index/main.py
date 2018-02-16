import time
import random
import string

from item import Item
from bitmap import BitMap

DATA_SIZE = 20
LIST_SIZE = 20000


def generate_item_list(size):
    return [Item(x, ''.join(random.choice(string.ascii_letters) for _ in range(DATA_SIZE))) for x in range(size)]


def search(item_list, item):
    for i, p in enumerate(item_list):
        if p.key == item.key:
            return i


item_list = generate_item_list(LIST_SIZE)
item = item_list[random.randint(len(item_list) / 2, len(item_list) - 1)]

index = BitMap(item_list, ">= 15000")

start = time.time()
search(item_list, item)
end = time.time()

time_no_index = end - start

start = time.time()
index.search(item)
end = time.time()

time_index = end - start

assert time_index < time_no_index, 'Your implementation sucks!'
