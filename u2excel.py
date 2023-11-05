import pandas as pd
from faker import Faker

import random


def generate_names(num_names):
    fake = Faker()
    names = set()
    while len(names) < num_names:
        names.add(fake.name())
    return list(names)


def generate_random_email():
    fake = Faker()
    username = fake.user_name()
    domain = fake.domain_name()
    unique_domain = f"{username}@{domain}"
    return unique_domain


def is_unique(email, generated_emails):
    return email not in generated_emails


def uniq_email(num_emails):
    generated_emails = []
    for _ in range(num_emails):
        while True:
            email = generate_random_email()
            if is_unique(email, generated_emails):
                generated_emails.append(email)
                break
    return generated_emails


User_role_dict = {
    "Manager": 100,
    "Developer": 200,
    "Normal User": 300
}


def pick_random_items_from_dict(dictionary, num_items):
    items = random.choices(list(dictionary.items()), k=num_items)
    keys_list, values_list = zip(*items)
    return list(keys_list), list(values_list)


def read_excel_columns_to_dict(file_path, key_column, value_column):
    data = pd.read_excel(file_path)
    key_values_dict = dict(zip(data[key_column], data[value_column]))
    return key_values_dict


excel_file_path = "/Users/rabisankarmondal/1800c2.xlsx"  # Replace with the actual file path
key_column_name = "Name"  # Replace with the name of the key column
value_column_name = "Customer ID"  # Replace with the name of the value column

try:
    result_dict = read_excel_columns_to_dict(excel_file_path, key_column_name, value_column_name)
    # print("Dictionary (Key-Value Pairs):")
    # print(result_dict)
except FileNotFoundError:
    print("Error: The specified Excel file was not found.")
except Exception as e:
    print("An error occurred:", e)

num_rows = 3000
#  how many u2 is set to this function

start_user_id = 2000

names = generate_names(num_rows)
emails = uniq_email(num_rows)
role, role_id = pick_random_items_from_dict(User_role_dict, num_rows)

c2_name, c2_id = pick_random_items_from_dict(result_dict, num_rows)
User_ids = [start_user_id + i for i in range(num_rows)]

data = {

    "User Id": User_ids,
    "Name": names,
    "User Creation Date": "03/17/2022",
    "User Email Id": emails,
    "Customer Id": c2_id,
    "Customer Name": c2_name,
    "User Role Id": role_id,
    "User Role Name": role

}

df = pd.DataFrame(data)

# Exporting to Excel
output_file = "3000u2.xlsx"
df.to_excel(output_file, index=False, engine="openpyxl")

print(f"Dummy data for {num_rows} rows has been generated and saved to {output_file}.")
