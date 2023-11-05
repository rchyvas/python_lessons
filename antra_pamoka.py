

# for i in range(5):
#     print(i)

# for i in range(5):
#     print("number", i)

# numbers = [1,2,3,4,5]
# for number in numbers:
#     print("the number from the list is =", number)

# text = "python data science"
# for letter in text:
#     print(letter)

# dictionary = {"a":1,"b":2,"c":3}
# for key in dictionary:
#     print(key, dictionary[key])

# list = [1,2,3,4,5]
# for number in list:
#     if number == 3:
#         break
#     print(number)

# list = [1,2,3,4,5]
# for number in list:
#     if number == 3:
#         continue
#     print(number)

# numbers = [10,20,30,40,50]
# sum = sum(numbers)
# average_no = sum /len(numbers)
# for number in numbers:
#     if number > average_no:
#         print(number)

# list = ["roberta", "gertrūda", "elžbieta"]
# for name in list:
#     print(name)

# list = ["roberta", "gertrūda", "elžbieta"]
# print('\n'.join(list))

# text = "python" [::-1]
# print(text)

# text = "python"
# print(text[-1])

# list = ["here", "lays", "the", "code"]
# for i in list:
#     print(i, end=" ")

# multiplication_table = 10
# for i in range(1, multiplication_table + 1):
#     for j in range(1, multiplication_table + 1):
#         print(i*j, end="\t")
#     print()

# number = 19
# while number <= 20:
#     print(number)
#     number += 1

# number = 1
# while number <= 20:
#     print(number)
#     number += 1

# number = int(input("type in the number = "))
# while number < 0:
#     print("the number is negative")
#     number = int(input("try again = "))
# print("you provided a positive number")

# answer = 5
# guess = int(input("guess the number from 1 to 10 = "))
# while guess != answer:
#     guess = int(input("wrong answer, try again = "))
# print("you've guessed correctly")

# while True:
#     print("----menu----")
#     print("1. print the greeting")
#     print("2. type in the name")
#     print("3. exit")
#
#     choice = input("type in the option from 1 to 3 = ")
#     if choice == "1":
#         print("hello!")
#     elif choice == "2":
#         name = input("type in the name = ")
#         print("the name was added successfully")
#         print(f"your name was changed to {name}")
#     elif choice == "3":
#         print("thank you for using this program, goodbye!")
#         break
#     else:
#         print("error, wrong option chosen. try again")

# secret_word = "love"
# guess = input("guess the word = ")
# while guess != secret_word:
#     guess = input("wrong answer, try again = ")
# print("you've guessed correctly, may you be blessed with it everyday")

# choice = int(input("choose a number from 1 to 10 = "))
# max_number = 1
# while max_number <= 10:
#     result = max_number*choice
#     print(f"{choice} x {max_number} = {result}")
#     max_number += 1

# def greeting():
#     print("hello python")
#
# if __name__== '__main__':
#     greeting()

# def greeting(name):
#     print(f"hello, {name}!")
#
# greeting("roberta")

# def sum(a,b):
#     return a + b
#
# result = sum(5,3)
# print(result)

# def sum(a,b):
#     print(a+b)
#
# sum(5,3)

# def show_menu():
#     print("----menu----")
#     print("1. add a book")
#     print("2. see all the books")
#     print("3. search a book by the title")
#     print("4. exit")
#
# def add_a_book(book_list):
#     title = input("type in the title = ")
#     author = input("type in the author = ")
#     book_list.append({"title": title, "author": author})
#     print(f"the book '{title}' was added successfully")
#
# def see_all_books(book_list):
#     for book in book_list:
#         print(f"name: {book['title']}, author: {book['author']}")
#
# def search_a_book(book_list):
#     needed_title = input("type in the title = ")
#     find_book = [book for book in book_list if needed_title.lower() in book['title'].lower()]
#
#     if find_book:
#         for book in find_book:
#             print(f"name: {book['title']}, author: {book['author']}")
#     else:
#         print(f"book not found")
#
# def main():
#     book_list = []
#
#     while True:
#         show_menu()
#         choice = input("type in the option from 1 to 4 = ")
#         if choice == "1":
#             add_a_book(book_list)
#         elif choice == "2":
#             see_all_books(book_list)
#         elif choice == "3":
#             see_all_books(book_list)
#         elif choice == "4":
#             print("thank you for choosing our service, goodbye!")
#             break
#         else:
#             print("error: wrong input. try again")
#
# if __name__ == '__main__':
#     main()


# bank_accounts = {
#
# }
# def show_menu():
#     print("----bank system----")
#     print("1. create an account")
#     print("2. deposit money")
#     print("3. withdraw money")
#     print("4. check the balance")
#     print("5. close an account")
#     print("6. exit")
#
# def create_account(services):
#     account_owner = input("type in the name = ")
#     opening_balance = int(input("type in the opening balance = "))
#     account_no = len(bank_accounts) + 1
#     bank_accounts[account_no] = {"account_owner": account_owner, "opening_balance": opening_balance}
#     print(f"new account '{account_no}' was created successfully")
#
# def deposit_money(services):
#     account_no = int(input("type in the account number = "))
#     sum = int(input("type in the sum to deposit = "))
#     bank_accounts[account_no]["opening_balance"] += sum
#     print(f"{sum} EU were successfully added to the account")
#
# def withdraw_money(services):
#     account_no = int(input("type in the account number = "))
#     sum = int(input("type in the sum to withdraw = "))
#     if sum <= bank_accounts[account_no]["opening_balance"]:
#         bank_accounts[account_no]["opening_balance"] -= sum
#         print(f"{sum} EU were successfully withdrawn from the account")
#     else:
#         print(f"error: the opening balance is too little")
#
# def check_balance(services):
#     account_no = int(input("type in the account number = "))
#     balance = bank_accounts[account_no]["opening_balance"]
#     print(f"the balance of '{account_no}' is {balance} EU")
#
# def close_account(services):
#         account_no = int(input("type in the account number = "))
#         del bank_accounts[account_no]
#         print(f"bank account no. '{account_no} was closed successfully")
#
# def main():
#     services = []
#
#     while True:
#         show_menu()
#         choice = input("type in the option from 1 to 6 = ")
#         if choice == "1":
#             create_account(services)
#         elif choice == "2":
#             deposit_money(services)
#         elif choice == "3":
#             withdraw_money(services)
#         elif choice == "4":
#             check_balance(services)
#         elif choice == "5":
#             close_account(services)
#         elif choice == "6":
#             print("thank you for choosing our service, goodbye!")
#             break
#         else:
#                 print("error: wrong input. try again")
#
# main()

# def pvm_calculator(price):
#     pvm_rate = 0.21
#     price_with_pvm = price * price * pvm_rate
#     print(f"price with pvm =", price_with_pvm)
# price_without_pvm = int(input("type in the price = "))
# pvm_calculator(price_without_pvm)

# item_list = [
#     {"item": "watermelon", "price": 5.59},
#     {"item": "dragonfruit", "price": 10.99},
#     {"item": "strawberry", "price": 2.59},
#     {"item": "orange", "price": 4.99}
# ]
#
# a = item_list[0]
# b = item_list[1]
# c = item_list[2]
# d = item_list[3]
#
# value = max(a["price"], b["price"], c["price"], d["price"])
#
# if a["price"] == value:
#     print(f"the most expensive item in the list is {a['item']}")
# if b["price"] == value:
#     print(f"the most expensive item in the list is {b['item']}")
# if c["price"] == value:
#     print(f"the most expensive item in the list is {c['item']}")
# if d["price"] == value:
#     print(f"the most expensive item in the list is {d['item']}")

# student_grades = {
#     'math': 10,
#     "english": 10,
#     "geography": 10
# }
#
# if student_grades['math'] <= 5:
#     print("this student has not passed math exam")
# else:
#     print("this student has passed math exam")
# if student_grades['english'] <= 5:
#     print("this student has not passed english exam")
# else:
#     print("this student has passed english exam")
# if student_grades['geography'] <= 5:
#     print("this student has not passed geography exam")
# else:
#     print("this student has passed geography exam")

# client = {
#     "name": "roberta",
#     "age": 27,
#     "city": "kaunas",
#     "telephone": "+370000000000",
#     "acc.balance": 10000
# }
#
# purchase = 50000
# if client["acc.balance"] < purchase:
#     print("insufficient funds")
# else:
#     print("can be purchased")