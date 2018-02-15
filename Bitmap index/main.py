from indexing import Index
import json

with open('students.json', 'r') as data_file:
	students = json.load(data_file)

bitmap_index = Index(students)

bitmap_index.add_index("age>5")