import unittest
from unittest.mock import patch
from personal_finance_assistant import main, load_transactions, save_transactions

class TestFinanceProgram(unittest.TestCase):

    @patch('builtins.input', side_effect=[
        '1',  # Choose add a new transaction
        '2023-01-01',  # Date
        'Test Income',  # Transaction description
        'Income',  # Transaction type
        '1000',  # Amount
        '5',  # Exit
    ])
    def test_add_transaction(self, mock_inputs):
        # Test Adding Transaction Functionality
        main()
        transactions = load_transactions()
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0].description, 'Test Income')


if __name__ == '__main__':
    unittest.main()
