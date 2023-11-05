#
#
# def maximum(a, b, c):
#     if (a >= b) and (a >= c):
#         largest = a
#
#     elif (b >= a) and (b >= c):
#         largest = b
#     else:
#         largest = c
#
#     return largest
#
#
#
# a = 10
# b = 14
# c = 12
# print(maximum(a, b, c))


# a = 10
# b= 7
# c = 8
# if (a >= b) and (a >= c):
#   print("a is largest",a)
# elif (b >= a) and (b >= c):
#    print("b is largest")
# else:
#   print("c is largest")


# prime number
#
# n = int(input("ENTER NUMBER: "))
# flag = 0
# for i in range(2,n):
#     if(n%i == 0):
#         flag = 1
#         break
#
# if(flag == 1):
#     print(n,"is not prime")
# else:
#     print(n,"is prime")


# n = int(input("ENTER NUMBER: "))
# fact =1
# if(n<0):
#     print("wrong input")
# elif(n==0):
#     print("The factorial of",n,"is",fact)
# else:
#     for i in range(1,n+1):
#         fact = fact*i
#
#     print("The factorial of",n,"is",fact)


# a = 370
# n = a
# count = 0
# while(n>0):
#     count = count+1
#     n = n//10
#
# num = a
# s = 0
#
# while(num>0):
#     d = num % 10
#     s = s + (d ** count)
#     num = num//10
#
# if(s==a):
#     print(a,"is a armstrong number")
# else:
#     print(a, "is not a armstrong number")
#
# n = int(input("enter how many terms: "))
#
# a,b = 0,1
#
# if(n<=0):
#     print("wrong input")
# elif(n==1):
#     print(a)
# else:
#     for i in range(1,n+1):
#         print(a)
#         c= a+b
#         a = b
#         b= c


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#
# for x, y in thisdict.items():
#   print(x, y)
#
# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }
#
# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }
# print(myfamily["child2"]["name"])
#
#
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# print(thisdict)

# def my_function(name):
#     print(name)
#
#
# def my_function():
#     print("Rabi")
#
#
# my_function('Debolina')

import random

#
# def userid_role(num_items, my_dict):
#     key = value = []
#
#     for i in range(num_items):
#         random_key = random.choice(list(my_dict.keys()))
#         random_value = my_dict[random_key]
#         key.append(random_key)
#         value.append(random_value)
#     return key, value
#
# if __name__ == "__main__":
#     my_dict = {
#         "apple": 1,
#         "banana": 2,
#         "orange": 3,
#         "grape": 4,
#         "watermelon": 5
#     }
#     key = value = []
#     key, value = userid_role(10,my_dict)
#
#     print(type(key))
#     print(len(key))

#
# def roleid(numemails, role_id, role_name):
#     key = value = set()
#     for i in range(numemails):
#         a = random.randrange(0, len(role_id))
#         key.add(role_id[a])
#         value.add(role_name[a])
#         # print(role_id[a])
#         # print(role_name[a])
#
#     return key
#
# arr = [1,2,3]
# arr2 = ["Helo","ab","cd"]
# no = 3
# key1 = roleid(no, arr, arr2)
# print(key1)
# # print(value11)
# # print(type(key1))
# # roleid(no,arr,arr2)

# import random
#
# # Sample dictionary with 3 items
# my_dict = {
#     "apple": 1,
#     "banana": 2,
#     "orange": 3
# }
#
# def pick_random_items_from_dict(dictionary, num_items):
#     items = random.choices(list(dictionary.items()), k=num_items)
#     keys_list, values_list = zip(*items)
#     return list(keys_list), list(values_list)
#
#
# num_items_to_pick = 2
#
# keys_list, values_list = pick_random_items_from_dict(my_dict, num_items_to_pick)
#
# print("Picked Keys:")
# print(keys_list)
#
# print("\nPicked Values:")
# print(values_list)

# import pandas as pd
#
#
# def read_excel_columns_to_dict(file_path, key_column, value_column):
#     data = pd.read_excel(file_path)
#     key_values_dict = dict(zip(data[key_column], data[value_column]))
#     return key_values_dict
#
#
# excel_file_path = "/Users/rabisankarmondal/5c2.xlsx"  # Replace with the actual file path
# key_column_name = "Name"  # Replace with the name of the key column
# value_column_name = "Customer ID"  # Replace with the name of the value column
#
# try:
#     result_dict = read_excel_columns_to_dict(excel_file_path, key_column_name, value_column_name)
#     # print("Dictionary (Key-Value Pairs):")
#     print(result_dict)
# except FileNotFoundError:
#     print("Error: The specified Excel file was not found.")
# except Exception as e:
#     print("An error occurred:", e)
#
#
# def pick_random_items_from_dict(dictionary, num_items):
#     items = random.choices(list(dictionary.items()), k=num_items)
#     keys_list, values_list = zip(*items)
#     return list(keys_list), list(values_list)
#
#
# num_rows = 10
# role, role_id = pick_random_items_from_dict(result_dict, num_rows)
# print(role)
# print(role_id)
#
import random

def generate_phonenumber():
    return random.randint(10**9, 10**10 - 1)

num_numbers_to_generate = 100

random_numbers = [generate_phonenumber() for _ in range(num_numbers_to_generate)]

print("Generated Random 10-Digit Numbers:")
for number in random_numbers:
    print(number)
print(len(random_numbers))


#
# import random
#
# def generate_unique_random_numbers(num_numbers, num_digits):
#     # Generate a list of all possible 10-digit numbers
#     all_numbers = list(range(10**(num_digits - 1), 10**num_digits))
#
#     # Sample 20 unique random numbers from the list
#     random_numbers = random.sample(all_numbers, num_numbers)
#
#     return random_numbers
#
# if __name__ == "__main__":
#     num_random_numbers = 20
#     num_digits_per_number = 10
#
#     random_numbers = generate_unique_random_numbers(num_random_numbers, num_digits_per_number)
#
#     print("Generated Random Numbers:")
#     print(random_numbers)
