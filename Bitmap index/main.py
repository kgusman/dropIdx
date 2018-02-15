from indexing import Index
import json

with open('students.json', 'r') as data_file:
	students = json.load(data_file)

bitmap_index = Index(students)

bitmap_index.add_index("age >= 21")
bitmap_index.add_index("name == Kamill")
bitmap_index.and_op("age >= 21", "firstname == Kamill")
bitmap_index.or_op("firstname >= Anton", "firstname == Kamill")