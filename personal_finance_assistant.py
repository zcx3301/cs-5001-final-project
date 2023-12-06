from datetime import datetime


class Transaction:
    def __init__(self, date, description, type, amount):
        """
        Initialize the properties of the transaction object.

        Args:
            date (str): The transaction date in the format YYYY-MM-DD.
            description (str): The transaction description.
            type (str): The transaction type, can be 'Income' or 'Expense'.
            amount (float): The transaction amount.
        """
        self.date = date
        self.description = description
        self.type = type
        self.amount = amount

    def __str__(self):
        """
        Return the string representation of the transaction object.
        """
        return f"{self.date},{self.description},{self.type},{self.amount}"

    @staticmethod
    def from_string(s):
        """
        Create a Transaction object from a string.

        Args:
            s(str): The string representation of the transaction in the format "date,description,type,amount".

        Returns:
            Transaction: The Transaction object created from the string.
        """
        date, description, type, amount = s.strip().split(',')
        return Transaction(date, description, type, float(amount))


TRANSACTIONS_FILE = 'transactions.txt'


def load_transactions() -> list:
    """
    Load transactions stored in a file.

    Returns:
        list: A list containing Transaction objects.
    """
    transactions = []
    try:
        with open(TRANSACTIONS_FILE, 'r', encoding='utf-8') as file:
            for line in file:
                transactions.append(Transaction.from_string(line))
    except FileNotFoundError:
        pass
    return transactions


def save_transactions(transactions):
    """
    Save transactions to a file.

    Args:
        transactions (list): A list containing Transaction objects.

    Return：
        None
    """
    with open(TRANSACTIONS_FILE, 'w', encoding='utf-8') as file:
        for transaction in transactions:
            file.write(str(transaction) + '\n')


def valid_date(date_str):
    """
    Check the validity of a date string.

    Args:
        date_str (str): The date string to be checked in the format YYYY-MM-DD.

    Returns:
        bool: True if the date string is valid, False otherwise.
    """
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def view_transactions_in_range(transactions):
    """
    View income and expenses within a specific date range.

    Args:
            transactions (list): A list containing Transaction objects.

    Returns:
        None
    """
    while True:
        start_date = input("Enter the start date (format: YYYY-MM-DD): ")
        if valid_date(start_date):
            break
        else:
            print("Invalid date format. Please enter again.")

    while True:
        end_date = input("Enter the end date (format: YYYY-MM-DD): ")
        if valid_date(end_date):
            break
        else:
            print("Invalid date format. Please enter again.")

    filtered_transactions = [t for t in transactions if start_date <= t.date <= end_date]
    total_income = sum(t.amount for t in filtered_transactions if t.type == 'Income')
    total_expense = sum(t.amount for t in filtered_transactions if t.type == 'Expense')
    net_savings = total_income - total_expense

    print("\nFinancial report from {} to {}:".format(start_date, end_date))
    print("Total income: {:.2f}, Total expense: {:.2f}, Net savings: {:.2f}".format(total_income, total_expense, net_savings))


def add_transaction(transactions):
    """Add a new transaction record.

    Args:
        transactions (list): A list containing Transaction objects.

    Returns:
        None
    """
    while True:
        date = input("Enter the transaction date (format: YYYY-MM-DD): ")
        if valid_date(date):
            break
        else:
            print("Invalid date format. Please enter again.")

    description = input("Enter the transaction description: ")

    while True:
        type = input("Enter the transaction type (Income/Expense): ")
        if type in ['Income', 'Expense']:
            break
        else:
            print("Invalid transaction type. Please enter 'Income' or 'Expense'.")

    while True:
        try:
            amount = float(input("Enter the amount: "))
            break
        except ValueError:
            print("Invalid amount entered. Please enter again.")

    transaction = Transaction(date, description, type, amount)
    transactions.append(transaction)
    save_transactions(transactions)
    print("Transaction record added.")


def generate_report(transactions):
    """
    Generate a financial report.

    Args:
        transactions (list): A list containing Transaction objects.

    Returns:
        None
    """
    total_income = sum(t.amount for t in transactions if t.type == 'Income')
    total_expense = sum(t.amount for t in transactions if t.type == 'Expense')
    net_savings = total_income - total_expense

    print("\nFinancial report:")
    print("Total income: {:.2f}, Total expense: {:.2f}, Net savings: {:.2f}\n".format(total_income, total_expense,
                                                                                      net_savings))
    print("Detailed transaction records:")
    for transaction in transactions:
        print("Date: {}, Description: {}, Type: {}, Amount: {:.2f}".format(transaction.date, transaction.description,
                                                                           transaction.type, transaction.amount))


def edit_transaction(transactions):
    """
    Edit a transaction record for a specific date.

    Args:
        transactions (list): A list containing Transaction objects.

    Returns:
        None
    """
    print("Edit transaction record")
    date = input("Enter the date of the transaction to edit (format: YYYY-MM-DD): ")
    matched_transactions = [t for t in transactions if t.date == date]

    if not matched_transactions:
        print("No transactions found for the specified date.")
        return

    for i, transaction in enumerate(matched_transactions):
        print(f"{i + 1}. {transaction}")

    choice = int(input("Select the transaction number to edit: "))
    if choice < 1 or choice > len(matched_transactions):
        print("Invalid choice.")
        return

    transaction = matched_transactions[choice - 1]

    new_date = input(f"New date [{transaction.date}]: ") or transaction.date
    new_description = input(f"New description [{transaction.description}]: ") or transaction.description
    new_type = input(f"New type (Income/Expense) [{transaction.type}]: ") or transaction.type
    new_amount = input(f"New amount [{transaction.amount}]: ") or transaction.amount

    transaction.date = new_date
    transaction.description = new_description
    transaction.type = new_type
    transaction.amount = float(new_amount)

    save_transactions(transactions)
    print("Transaction record updated.")


def main():
    """
    Main function for the program.
    """
    transactions = load_transactions()

    while True:
        print("\nPersonal Finance Assistant")
        print("1. Add a new transaction")
        print("2. Edit a transaction record")
        print("3. View financial report")
        print("4. View income and expenses in a specific date range")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            add_transaction(transactions)
        elif choice == '2':
            edit_transaction(transactions)
        elif choice == '3':
            generate_report(transactions)
        elif choice == '4':
            view_transactions_in_range(transactions)
        elif choice == '5':
            print("Thank you for using the Personal Finance Assistant. Goodbye!")
            break
        else:
            print("Invalid input. Please enter again.")


if __name__ == "__main__":
    main()
