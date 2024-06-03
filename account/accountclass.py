import json
from datetime import datetime

class BankAccounts:
    def __init__(self):
        self.accounts = {}

    def create_new_bank_account(self, username, client_number):

        balance = float(input("Enter initial balance: "))
        opening_date = datetime.now()


        if username in self.accounts:

            number_of_accounts = len(self.accounts[username])+1
        else:

            self.accounts[username] = []
            number_of_accounts = 1


        account_number = (number_of_accounts * 100000000) + client_number
        new_account = {
            "account_number": account_number,
            "balance": balance,
            "opening_date": opening_date.strftime("%Y-%m-%d %H:%M:%S"),  # Преобразование даты в строку
        }

        self.accounts[username].append(new_account)

        print(f"New bank account created successfully! Account number: {account_number}")


        self.saveaccount_to_file()

    def check_customer_accounts(self, username):
        """
        Checks if a customer has any associated accounts.
        Returns True if the customer has accounts, False otherwise.
        """
        try:
            with open("accounts_data.txt", "r") as file:
                for line in file:
                    account_data = json.loads(line.strip())
                    if account_data["username"] == username:
                        return True

            return False
        except FileNotFoundError:
            print("Accounts file not found.")
            return False

    def get_customer_accounts(self, username):

        try:
            with open("accounts_data.txt", "r") as file:
                accounts_list = []
                for line in file:
                    account_data = json.loads(line.strip())
                    if account_data["username"] == username:
                        accounts_list.append(account_data)
                return accounts_list
        except FileNotFoundError:
            print("Accounts file not found.")
            return []

    def saveaccount_to_file(self):
        with open("accounts_data.txt", "w") as file:
            for username, accounts in self.accounts.items():
                for account in accounts:
                    json.dump({"username": username, "account": account}, file)
                    file.write("\n")

    def load_accounts_file(self):
        self.accounts = {}
        try:
            with open("accounts_data.txt", "r") as file:
                for line in file:
                    account_data = json.loads(line.strip())
                    username = account_data["username"]
                    account = account_data["account"]
                    if username not in self.accounts:
                        self.accounts[username] = []
                    self.accounts[username].append(account)
        except FileNotFoundError:
            print("Accounts file not found.")

    def list_bank_accounts_admin(self, username):
        self.load_accounts_file()
        accounts = self.get_customer_accounts(username)
        if accounts:
            for account_info in accounts:
                account = account_info['account']
                print(f"Account Number: {account['account_number']}, opening_date: {account['opening_date']}")
        else:
            print("No accounts found.")
    def list_bank_accounts(self, username):
        self.load_accounts_file()
        accounts = self.get_customer_accounts(username)
        if accounts:
            for account_info in accounts:
                account = account_info['account']
                print(f"Account Number: {account['account_number']}, Balance: {account['balance']}")
        else:
            print("No accounts found.")

    def show_balance(self, username):
        self.load_accounts_file()
        accounts = self.get_customer_accounts(username)

        if accounts:
            if len(accounts) == 1:
                print(f"Balance: {accounts[0]['account']['balance']}")
            else:
                print("Choose an account to view balance:")
                for i in range(1, len(accounts) + 1):
                    account_info = accounts[i - 1]
                    account = account_info['account']
                    print(f"{i}. Account Number: {account['account_number']}")
                choice = int(input("Enter your choice: ")) - 1
                if 0 <= choice < len(accounts):
                    print(f"Balance: {accounts[choice]['account']['balance']}")
                else:
                    print("Invalid choice.")
        else:
            print("No accounts found.")

    def update_account(self, updated_account_info):
        for username, accounts in self.accounts.items():
            for acc in accounts:
                if acc['account_number'] == updated_account_info['account']['account_number']:
                    acc['balance'] = updated_account_info['account']['balance']
                    break
        self.saveaccount_to_file()

    def withdraw(self, username):
        accounts_list = self.get_customer_accounts(username)

        if not accounts_list:
            print("No accounts found.")
            return

        if len(accounts_list) == 1:
            account_info = accounts_list[0]
            account = account_info['account']
            print(f"Account Number: {account['account_number']}, Balance: {account['balance']}")
            amount = float(input("Enter amount to withdraw: "))
            if account['balance'] >= amount:
                account['balance'] -= amount
                print(f"Withdrawal successful! New balance: {account['balance']}")
                self.update_account({'username': username, 'account': account})
            else:
                print("Insufficient funds.")
            return
        else:
            print("Choose account for withdrawal:")
            for i in range(1, len(accounts_list) + 1):
                account_info = accounts_list[i - 1]
                account = account_info['account']
                print(f"{i}. Account Number: {account['account_number']}, Balance: {account['balance']}")

            account_index = int(input("Enter the number of the account from which to withdraw: ")) - 1

            if 0 <= account_index < len(accounts_list):
                selected_account_info = accounts_list[account_index]
                selected_account = selected_account_info['account']
                amount = float(input("Enter amount to withdraw: "))
                if selected_account['balance'] >= amount:
                    selected_account['balance'] -= amount
                    print(f"Withdrawal successful! New balance: {selected_account['balance']}")
                    self.update_account({'username': username, 'account': selected_account})
                else:
                    print("Insufficient funds.")
            else:
                print("Invalid account selection.")
            return

    def deposit(self, username):
        accounts_list = self.get_customer_accounts(username)

        if not accounts_list:
            print("No accounts found.")
            return

        if len(accounts_list) == 1:
            account_info = accounts_list[0]
            account = account_info['account']
            print(f"Account Number: {account['account_number']}, Balance: {account['balance']}")
            amount = float(input("Enter amount to deposit: "))
            account['balance'] += amount
            print(f"Deposit successful! New balance: {account['balance']}")
            self.update_account({'username': username, 'account': account})
            return
        else:
            print("Choose account for deposit: ")
            for i in range(1, len(accounts_list) + 1):
                account_info = accounts_list[i - 1]
                account = account_info['account']
                print(f"{i}. Account Number: {account['account_number']}, Balance: {account['balance']}")

            account_index = int(input("Enter the number of the account to deposit into: ")) - 1

            if 0 <= account_index < len(accounts_list):
                selected_account_info = accounts_list[account_index]
                selected_account = selected_account_info['account']
                amount = float(input("Enter amount to deposit: "))
                selected_account['balance'] += amount
                print(f"Deposit successful! New balance: {selected_account['balance']}")
                self.update_account({'username': username, 'account': selected_account})
            else:
                print("Invalid account selection.")
            return
accounts = BankAccounts()