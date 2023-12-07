import unittest
from personal_finance_assistant import Transaction, add_transaction ,valid_date

class TestFinanceAssistant(unittest.TestCase):

    def test_transaction_creation(self):
        transaction = Transaction("2023-04-01", "Groceries", "Expense", 50.0)
        self.assertEqual(transaction.date, "2023-04-01")
        self.assertEqual(transaction.description, "Groceries")
        self.assertEqual(transaction.type, "Expense")
        self.assertEqual(transaction.amount, 50.0)

    def test_transaction_str(self):
        transaction = Transaction("2023-04-01", "Rent", "Expense", 800.0)
        self.assertEqual(str(transaction), "2023-04-01,Rent,Expense,800.0")

    def test_valid_date(self):
        self.assertTrue(valid_date("2023-04-01"))
        self.assertFalse(valid_date("2023-02-30"))  # Invalid date
        self.assertFalse(valid_date("04-01-2023"))  # Incorrect format

