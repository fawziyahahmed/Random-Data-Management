import random  # Importing the random module for generating random data
import string  # Importing the string module for string manipulation

class DataCollector:
    def __init__(self):
        self.data = {}  # Initializing an empty dictionary to store generated data

    def generate_random_string(self, length=8):
        # Generating a random string of specified length using ascii letters and digits
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    def generate_sample_data(self, num_records):
        # Generating sample data for a specified number of records
        for i in range(num_records):
            # Generating random data for each record including username, password, birthdate, address, SSN, product purchased, and salesperson
            username = self.generate_random_string()
            password = self.generate_random_string()
            birthdate = f"{random.randint(1, 12)}-{random.randint(1, 28)}-{random.randint(1950, 2000)}"
            street_name = self.generate_random_string().capitalize()  # Capitalizing street name
            house_number = random.randint(100, 9999)  # Generating a random house number
            address = f"{house_number} {street_name} St."  # Creating address format with house number and street name
            ssn = ''.join(random.choices(string.digits, k=9))
            product_purchased = {
                "orderID": f"ID-{self.generate_random_string(6)}",
                "productID": f"ID-{self.generate_random_string(8)}",
                "quantity": random.randint(1, 10),
                "date_of_order": f"{random.randint(1, 12)}/{random.randint(1, 28)}/{random.randint(2000, 2023)}",
                "region": random.choice(["North", "South", "East", "West"])
            }
            salesperson = f"SalesID-{self.generate_random_string(6)}"
            # Storing generated data in the dictionary
            self.data[username] = {
                "password": password,
                "birthdate": birthdate,
                "address": address,
                "ssn": ssn,
                "productPurchased": product_purchased,
                "salesperson": salesperson
            }
            # Printing the generated data for each record
            print(f"Generated Record {i+1}:")
            print(f"Username: {username}")
            print(f"Password: {password}")
            print(f"Birthdate: {birthdate}")
            print(f"Address: {address}")
            print(f"SSN: {ssn}")
            print("Product Purchased:")
            for key, value in product_purchased.items():
                print(f"\t{key}: {value}")
            print(f"Salesperson: {salesperson}")
            print()

    def get_user_by_state(self, state):
        # Retrieving users based on the state they reside in
        return [user for user, info in self.data.items() if info['address'].split()[-2] == state]

    def get_user_by_salesperson(self, salesperson_id):
        # Retrieving users based on the salesperson handling them
        return [user for user, info in self.data.items() if info['salesperson'] == salesperson_id]

# Usage
collector = DataCollector()
collector.generate_sample_data(3)  # Generate 3 sample records

# Example searches
users_in_mi = collector.get_user_by_state("MI")
print("Users in MI:", users_in_mi)

users_handled_by_salesperson = collector.get_user_by_salesperson("SalesID-ABC123")
print("Users handled by salesperson ABC123:", users_handled_by_salesperson)