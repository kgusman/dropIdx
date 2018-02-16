import time
import random
import string

from item import Item
from hashindex import HashIndex
from hashindex import HashIndex_no_duplicates

# Constants are defined below
DATA_SIZE = 20
LIST_SIZE = 20


def generate_item_list(_size):
    return [Item(x, ''.join(random.choice(string.ascii_letters) for _ in range(DATA_SIZE))) for x in range(_size)]


def search(_item_list, _item):
    for i, p in enumerate(_item_list):
        if p.key == _item.key:
            return i


def build_hash_index(_item_list):
    index = HashIndex()
    [index.insert(x, i) for i, x in enumerate(_item_list)]

    return index

item_list = generate_item_list(LIST_SIZE)

index = random.randint(len(item_list) / 2, len(item_list) - 1)
item1 = item_list[index]
item2 = item_list[index + 1]

hash_index = build_hash_index(item_list)

#Measuring raw search time is too boring, let's try to measure search + remove + search time
#Assuming we should reconstruct whole hash index on removal (no lazy deletion)
start = time.time()
index1 = search(item_list, item1)
index2 = search(item_list,item2)
del item_list[index1]
index3 = search(item_list,item2)
end = time.time()
print(index1)
print(index2)
print(index3)

time_no_index = end - start
print("Elapsed time for no Index: " + str(time_no_index))


start = time.time()
index1 = hash_index.search(item1)
index2 = hash_index.search(item2)
hash_index.remove(item1)
index3 = hash_index.search(item2)
end = time.time()
print(index1)
print(index2)
print(index3)

time_index = end - start

print("Elapsed time for Dict Index: " + str(time_index))
try:
    print("Faster by factor of: " + str(time_no_index/time_index))
except ZeroDivisionError:
    print("IT'S OVER 9000")
    
    
assert time_index < time_no_index, 'Your implementation sucks!'
