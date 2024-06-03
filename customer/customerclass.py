class Customer:
    def __init__(self):
        self.customers = {}

    def create_new_user(self):
        client_name = input("Enter your name: ")
        address = input("Enter your address: ")
        phone_number = input("Enter your telephone number: ")
        username = input("Enter your Username: ")
        password = input("Enter your password:")
        x = len(self.customers)
        if username not in self.customers:
            self.customers[username] = {
                "client_name": client_name,
                "address": address,
                "phone_number": phone_number,
                "password": password,
                "client_number": x+1
            }
            print(f'Welcome {client_name}')
            self.save_to_file()
        else:
            print("Username exists")

    def update_customer_info(self, username, new_data):
        if username in self.customers:
            self.customers[username].update(new_data)
            print(f"Customer '{username}' information updated successfully.")
            self.save_to_file()
        else:
            print(f"Customer '{username}' not found.")

    def delete_customer(self, username):
        self.load_from_file()
        if username in self.customers:
            del self.customers[username]
            print(f"Customer '{username}' deleted successfully.")
            self.save_to_file()
        else:
            print(f"Customer '{username}' not found.")

    def view_customers_info(self, username):

        data = self.customers[username]
        print(f"Customer Information for '{username}':")
        print(f"Client Name: {data['client_name']}")
        print(f"Address: {data['address']}")
        print(f"Phone Number: {data['phone_number']}")
        print("----------------------------------")

    def save_to_file(self):
        temp_customers = {}
        try:
            with open("customer_data.txt", "r") as file:
                for line in file:
                    username, data = line.strip().split(": ", 1)
                    temp_customers[username] = eval(data)
        except FileNotFoundError:
            print("Customer data file not found.")
            temp_customers = self.customers

        with open("customer_data.txt", "w") as file:
            for username, data in self.customers.items():
                file.write(f"{username}: {data}\n")

    def load_from_file(self):

        try:
            with open("customer_data.txt", "r") as file:
                for line in file:
                    username, data = line.strip().split(": ", 1)
                    self.customers[username] = eval(data)
                return self.customers
        except FileNotFoundError:
            print("Customer data file not found.")



    def login_existing_user(self, username, password):

        if username in self.customers and self.customers[username]["password"] == password:
            print(f"Welcome {self.customers[username]['client_name']}!")

            return True
        else:
            print("Invalid username or password. Please try again.")
            return False

    '''def print_customers(self):
        print(self.customers)'''

    def get_client_number(self, username):
        return self.customers[username]['client_number']


customers = Customer()
