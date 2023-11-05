# import os
# import shutil

# print("here lays the code")

# age = 27
# print(age)

# age = 27
# print("age " +str(age))

# name = "roberta"
# age = "27"
# print("my name's " + name + " and i'm " + age)

# name = "roberta"
# age = "27"
# does_roberta_code = False
# print("my name's " + name + " and i'm " + age, does_roberta_code)

# name = "roberta"
# age = "27"
# roberta_temperature = 35.7
# print("my name's " + name + " and i'm " + age, roberta_temperature)

# name = "roberta"
# age = "27"
# does_roberta_code = False
# print(type(name))

# name = "roberta"
# age = "27"
# does_roberta_code = False
# print(type(does_roberta_code))

# fruits = ["dragonfruit", "watermelon", "kiwi", "orange"]
# print(fruits)

# fruits = ["dragonfruit", "watermelon", "kiwi", "orange"]
# print(type(fruits))

# fruits = ["dragonfruit", "watermelon", "kiwi", "orange"]
# print(fruits[0])

# fruits in this example go from 0 to 3 [0, 1, 2, 3]

# fruits = ["dragonfruit", "watermelon", "kiwi", "orange"]
# length = len(fruits)
# print(length)

# fruits = ["dragonfruit", "watermelon", "kiwi", "orange"]
# print(fruits[:2])

# fruits = ["dragonfruit", "watermelon", "kiwi", "orange"]
# print(fruits[1:2])

# fruits = ["dragonfruit", "watermelon", "kiwi", "orange"]
# print(fruits[2:2])

# fruits = ["dragonfruit", "watermelon", "kiwi", "orange"]
# print(fruits[2:3])

# fruits = ["dragonfruit", "watermelon", "kiwi", "orange"]
# print(fruits[2:4])

# fruits = ["dragonfruit", "watermelon", "kiwi", "orange"]
# add_fruit = fruits.append("strawberry")
# print(fruits)

# fruits = ["dragonfruit", "watermelon", "kiwi", "orange"]
# fruits.insert(0, "strawberry")
# print(fruits)

# fruits = ["dragonfruit", "watermelon", "kiwi", "orange"]
# change_meaning = fruits[3] = "dragonfruit"
# print(fruits)

# fruits = ["dragonfruit", "watermelon", "kiwi", "orange"]
# change_meaning = fruits[0] = "strawberry"
# print(fruits)

# fruits = ["dragonfruit", "watermelon", "kiwi", "orange"]
# fruits.remove("kiwi")
# print(fruits)

# fruits = ["dragonfruit", "watermelon", "kiwi", "orange"]
# fruits.pop(2)
# print(fruits)

# fruits = []
# fruits.append("strawberry")
# fruits.insert(2, "orange")
# fruits[1] = "dragonfruit"
# print(fruits)

# dictionary = {
#     "name": "roberta",
#     "age": 27,
#     "city": "kaunas"
# };
# print(dictionary)

# dictionary = {
#     "name": "roberta",
#     "age": 27,
#     "city": "kaunas"
# };
# print(dictionary["city"])

# dictionary = {
#     "name": "roberta",
#     "age": 27,
#     "city": "kaunas"
# };
# dictionary["is_student"] = True
# print(dictionary)

# dictionary = {
#     "name": "roberta",
#     "age": 27,
#     "city": "kaunas"
# };
# del dictionary["city"]
# print(dictionary)

# students = {
#     "roberta":{
#         "age": 27,
#         "city": "kaunas",
#         "occupation": "translator"
#     },
#     "gertrūda":{
#         "age": 25,
#         "city": "vilnius",
#         "occupation": "actress"
#     },
#     "elžbieta":{
#         "age": 20,
#         "city": "warsaw",
#         "occupation": "lawyer"
#     }
# };
# print(students["roberta"])

# students = [
#     {
#         "name": "roberta",
#         "age": 27,
#         "city": "kaunas",
#         "occupation": "translator"
#     },
#     {
#         "name": "gertrūda",
#         "age": 25,
#         "city": "vilnius",
#         "occupation": "actress"
#     },
#     {
#         "name": "elžbieta",
#         "age": 20,
#         "city": "warsaw",
#         "occupation": "lawyer"
#     }
# ];
# print(students[1])

# students = [
#     {
#         "name": "roberta",
#         "age": 27,
#         "city": "kaunas",
#         "occupation": "translator"
#     },
#     {
#         "name": "gertrūda",
#         "age": 25,
#         "city": "vilnius",
#         "occupation": "actress"
#     },
#     {
#         "name": "elžbieta",
#         "age": 20,
#         "city": "warsaw",
#         "occupation": "lawyer"
#     }
# ];
#
# new_student = {
#         "name": "liuka",
#         "age": 30,
#         "city": "klaipėda",
#         "occupation": "graphic designer"
# }
#
# students.append(new_student)
# print(students)

# age = 15
# if age >= 18:
#     print("the person is an adult")
# else:
#     print("the person is not an adult")

# age = 15
# if age >= 18:
#     print("the person is an adult")
# elif age > 13:
#     print("the person is a teenager")
# else:
#     print("the person is not an adult")

# age = 15
# if age >= 18 and age < 10:
#     print("the person is a child")
# elif age > 10:
#     print("the person is a teenager")
# else:
#     print("the person is an adult")

# fruits = []
# if not fruits:
#     print("fruit list is empty")
# elif "dragonfruit" in fruits:
#     print("dragonfruit")
# else:
#     print("fruit not found")

# age = 15
# has_id = True
#
# if age >= 18:
#     if has_id:
#         print("this person can vote")
#     else:
#         print("this person needs an id to vote")
#
# else:
#     print("this person can not vote")

# item_list = ['fruits', 'vegetables', 'pastries', 'dairy']
# print(f'choose an item from the list: "{item_list}"')
#
# item_categories = ['fruits', 'vegetables', 'pastries', 'dairy']
#
# items = {
#     'fruits': ['dragonfruit', 'watermelon'],
#     'vegetables': ['potatoes', 'cabbage'],
#     'pastries': ['bread', 'doughnuts'],
#     'dairy': ['eggs', 'cheese']
# }
#
# needed_category = 'fruits'
# needed_item = 'shoes'
#
# if needed_category in item_categories:
#     if needed_item in items[needed_category]:
#         print(f"'{needed_item}' is in stock")
#         if needed_item not in items[needed_category]:
#             print(f"'{needed_item}' is not in the category")
#     else:
#         print(f"'{needed_item}' does not exist")
# else:
#     print(f"'{needed_category}' category does not exist")

# list = [
# {
#         "name": "roberta",
#         "age": 20
#     },
#     {
#         "name": "gertrūda",
#         "age": 15
#     },
#     {
#         "name": "elžbieta",
#         "age": 10
#     }
# ]
#
# age = list[1]["age"]
# name = list[1]["name"]
#
# if age > 18:
#     print(f"{name} is of legal age")
# elif age > 12:
#         print(f"{name} is a teenager")
# else:
#     print(f"{name} is a child")

# employee = {
#         "name": "elžbieta",
#         "salary": 5180,
#         "occupation": "lawyer"
# }
#
# if employee["occupation"] == "lawyer":
#     employee["salary"] *= 1.10
# print(employee)

# books = [
#     {"name": "title one", "year_of_publication": 2015},
#     {"name": "title two", "year_of_publication": 2016},
#     {"name": "title three", "year_of_publication": 2017},
#     {"name": "title four", "year_of_publication": 2018},
# ]
#
# book_by_year = int(input("type in the year of publication = "))
# book = books[0]
#
# try:
#     if book["year_of_publication"] == book_by_year:
#         print(f"the book released in {book_by_year} is '{book[0]['name']}'")
#     elif book["year_of_publication"] == book_by_year:
#         print(f"the book released in {book_by_year} is '{book[1]['name']}'")
#     elif book["year_of_publication"] == book_by_year:
#         print(f"the book released in {book_by_year} is '{book[2]['name']}'")
#     elif book["year_of_publication"] == book_by_year:
#         print(f"the book released in {book_by_year} is '{book[3]['name']}'")
#     else:
#         print(f"no book found")
# except ValueError:
#     print("error: wrong input")

# current_catalogue = os.getcwd()
# print(current_catalogue)

# needed_folder = input("type in the name of a folder you want to access = ")
#
# try:
#     content = os.listdir(needed_folder)
#     print(" ".join(content))
# except FileNotFoundError:
#     print(f"folder not found")

# new_catalogue = input("type in the catalogue location = ")
# change_catalogue = os.chdir(new_catalogue)
#
# try:
#     content = os.listdir(new_catalogue)
#     print(" ".join(content))
# except FileNotFoundError:
#     print(f"folder not found")

# current_catalogue = os.getcwd()
# new_catalogue = input("type in the catalogue location = ")
# change_catalogue = os.chdir(new_catalogue)
#
# try:
#     change_catalogue = os.chdir(new_catalogue)
#     if os.getcwd() == new_catalogue:
#         print(f"current catalogue was successfully changed to {new_catalogue}")
#     content = os.listdir(new_catalogue)
#     print(" ".join(content))
# except FileNotFoundError:
#     print(f"folder not found")

# EXTENSION_MAP ={
#     '.pdf': "documents",
#     '.txt': "documents",
#     '.jpeg': "images",
#     '.jpg': "images",
#     '.png': "images",
#     '.gif': "images"
# }
#
# filename = input("type in the name of the file you want to organize = ")
# file_extension = os.path.splitext(filename)[1]
#
# try:
#     if os.path.exists(filename) and file_extension in EXTENSION_MAP:
#         directory_name = EXTENSION_MAP[file_extension]
#
#         if not os.path.exists(directory_name):
#             os.makedirs(directory_name)
#
#
#         shutil.move(filename, os.path.join(directory_name, filename))
#         print(f"{filename} has been moved to {directory_name}")
#
#     else:
#         print(f"the file does not exist or its extension is not recognized")
# except PermissionError:
#     print(f"error: permission to move {filename} was not granted")