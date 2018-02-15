from bitmap import BitMap
import json

with open('students.json', 'r') as data_file:
	students = json.load(data_file)

bitmap_index = BitMap(students)

bitmap_index.add_index("age >= 21")
bitmap_index.add_index("firstname == Kamill")

result = bitmap_index.and_op("age >= 21", "firstname == Kamill")
print(result)

result = bitmap_index.or_op("firstname != Anton", "firstname == Kamill")
print(result)