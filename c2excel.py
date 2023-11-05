import pandas as pd
from faker import Faker

import random

# Function to generate a list of random names without duplicates
def generate_names(num_names,customer_ids):
    fake = Faker()
    names = list()
    while len(names) < num_names:

        names.append(fake.name()+str(customer_ids))
        customer_ids = customer_ids + 1

    return list(names)

# # Function to generate a list of random emails without duplicates
# def generate_emails(num_emails):
#     fake = Faker()
#
#     emails = set()
#     while len(emails) < num_emails:
#         emails.add(fake.email())
#     return list(emails)

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


# Function to generate a list of random phone numbers without duplicates
# def generate_phone_numbers(num_phone_numbers):
#     fake = Faker()
#     phone_numbers = set()
#     while len(phone_numbers) < num_phone_numbers:
#         phone_numbers.add(fake.phone_number()[0:10])
#     return list(phone_numbers)

def generate_phonenumber():
    return random.randint(10**9, 10**10 - 1)


# Generating the data
num_rows = 1800    # How many data is set to the num_rows variable



start_customer_id = 100
# start_product_id = 1000
start_acv = 500000
phone_numbers = [generate_phonenumber() for _ in range(num_rows)]
names = generate_names(num_rows,start_customer_id)
# emails = generate_emails(num_rows)
emails = uniq_email(num_rows)
# phone_numbers = generate_phone_numbers(num_rows)
customer_ids = [start_customer_id + i for i in range(num_rows)]
# product_ids = [start_product_id + i for i in range(num_rows)]
acv = [start_acv + i for i in range(num_rows)]
# result_string = " ".join(map(str, customer_ids))
# Creating a DataFrame
data = {
    "Product Name": "ELM",
    "Customer ID": customer_ids,
    "Name": names,
    "Customer Creation Date": "03/17/2022",
    "Unique Customer Identifier": customer_ids,
    "Email": emails,
    "Customer Mobile": phone_numbers,
    "Customer Phone": phone_numbers,
    "Customer Address": "India",
    "Customer ACV": acv,
    "Last Payment Date": "03/17/2023",
    "Next Payment Date": "05/23/2023"


}


df = pd.DataFrame(data)

# Exporting to Excel
output_file = "1800c2.xlsx"
df.to_excel(output_file, index=False, engine="openpyxl")

print(f"Dummy data for {num_rows} rows has been generated and saved to {output_file}.")
