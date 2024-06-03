from customer.customerclass import customers
from account.accountclass import accounts
def customer_screen(customers):
    while True:
        print("Welcome to XYZ Bank Customer Portal!")
        print("-------------------------------")
        print("Choose from the below options:")
        print("1. Create New Login")
        print("2. Existing Customer")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Creating new login...")
            customers.create_new_user()

        elif choice == "2":
            print("Logging in as an existing customer...")
            username = input("Enter your Username: ")
            password = input("Enter your password: ")
            if customers.login_existing_user(username, password):

                while True:
                    print("-------------------------------")
                    print("Choose from the below options:")
                    print("1. Create New Bank Account")
                    print("2. List Bank Accounts")
                    print("3. Show Balance")
                    print("4. Withdraw")
                    print("5. Deposit")
                    print("6. Back to Main Menu")
                    choice = input("Enter your choice: ")

                    if choice == "1":
                        print("Creating new bank account...")
                        number = int(customers.get_client_number(username))
                        accounts.create_new_bank_account(username, number)
                    elif choice == "2":
                        print("Listing bank accounts...")
                        accounts.list_bank_accounts(username)
                    elif choice == "3":
                        print("Showing balance...")
                        accounts.show_balance(username)
                    elif choice == "4":
                        print("Withdrawing money...")
                        accounts.withdraw(username)
                    elif choice == "5":
                        print("Depositing money...")
                        accounts.deposit(username)
                    elif choice == "6":
                        print("Returning to main menu.")
                        break
                    else:
                        print("Invalid choice. Please enter a valid option.")
        elif choice == "3":
            print("Returning to main menu.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def admin_screen():
    print("Welcome to XYZ Bank Admin Portal!")
    print("-------------------------------")
    while True:
        print("1. Login")
        print("2. Previous menu")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter admin username: ")
            password = input("Enter admin password: ")
            # Perform admin login validation here
            if username == "admin" and password == "admin":
                admin_actions(customers, accounts)
                break
            else:
                print("Invalid admin credentials.")
        elif choice == "2":
            print("Returning to previous menu.")
            break
        elif choice == "3":
            print("Exiting the application. Goodbye!")
            exit()
        else:
            print("Invalid choice. Please enter a valid option.")

def admin_actions(customers, accounts):

    while True:
        print("-------------------------------")
        print("Choose from the below options:")
        print("1. View all customer information")
        print("2. Delete a customer")
        print("3. Update customer information")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            username_to_view = input("Enter username of the customer to view: ")
            if username_to_view in customers.customers:
                customers.view_customers_info(username_to_view)
                if accounts.check_customer_accounts(username_to_view):
                    print(f"Accounts for '{username_to_view}':")
                    """"# Retrieve and print customer accounts (without balance)
                    for account in accounts.get_customer_accounts(username_to_view):
                        print(
                            f"Account Number: {account.get('account_number', 'N/A')}, Opening Date: {account.get('opening_date', 'N/A')}")
                                        """

                    accounts.list_bank_accounts_admin(username_to_view)
                else:
                    print(f"No accounts found for '{username_to_view}'")
            else:
                print("Customer not found.")

        elif choice == "2":
            username_to_delete = input("Enter username of the customer to delete: ")
            if username_to_delete not in customers.customers:
                print("Customer not found.")
            elif accounts.check_customer_accounts(username_to_delete):
                print("Customer has accounts.")
            else:
                customers.delete_customer(username_to_delete)

        elif choice == "3":
            username_to_update = input("Enter username of the customer to update: ")
            if username_to_update in customers.customers:
                new_data = {
                        "client_name": input("Enter new client name: "),
                        "address": input("Enter new address: "),
                        "phone_number": input("Enter new phone number: ")
                          }
                customers.update_customer_info(username_to_update, new_data)
            else:
                print("Customer not found.")
        elif choice == "4":
            print("Returning to main menu.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


def main_screen():
    print("Welcome to XYZ Bank!")
    print("-------------------------------")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")

def main():
    customers.load_from_file()
    accounts.load_accounts_file()

    while True:
        main_screen()
        choice = input("Who are you? Enter the number: ")
        if choice == "1":
            customer_screen(customers)
        elif choice == "2":
            admin_screen()
        elif choice == "3":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()