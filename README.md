# Final Project Report

* Student Name: Chuanxing Zheng
* Github Username: zcx3301
* Semester: FALL 2023
* Course: CS 5001



## Description 
General overview of the project, what you did, why you did it, etc.  
This project is a personal finance assistant written in Python, designed to help users manage and track their daily financial transactions, including income and expenses. The inspiration for this tool comes from the need for personal financial management and aims to provide a simple, intuitive, and user-friendly way to record and analyze one's financial situation. 

Project Contents:   
1. Transaction Record Management: Using the `Transaction` class, users can create and store detailed information about financial transactions, such as date, description, type (income or expense), and amount.  
2. Data Storage and Loading: Utilizing text files as a data storage medium, the `load_transactions` and `save_transactions` functions allow users to persistently store transaction data in files and load this data when needed.  
3. Data Validation: Through the `valid_date` function, ensuring the correct date format of user input enhances the accuracy and reliability of the data.  
4. Adding and Editing Transaction Records: Using the `add_transaction` and `edit_transaction` functions, users can conveniently add new transaction records or modify existing ones.
5. Financial Report Generation: `The generate_report` function provides the ability to generate detailed financial reports, including total income, total expenses, and net savings, helping users better understand and analyze their financial situation. 
6. View Transactions in a Specific Date Range: The `view_transactions_in_range` function allows users to view financial activities within a specified date range, providing a more detailed financial analysis perspective.     

Project Purpose:  
The main purpose of this project is to provide a basic yet comprehensive tool that enables individuals to effectively manage and monitor their financial situation. By offering a way to record, view, and analyze income and expenses, this tool aims to assist users in making wiser financial decisions, enhancing their understanding and control of their personal financial situation. 

Summary:  
This personal finance assistant project, through its simplicity and practicality, aims to help ordinary users better manage and understand their personal finances. While providing relatively basic features, it is powerful enough to meet the fundamental needs of daily personal financial management.


## Key Features
Highlight some key features of this project that you want to show off/talk about/focus on.  

1. Structured Representation of Transaction Data: The project provides a clear and structured representation for transaction data through the `Transaction` class. This makes the creation, storage, and handling of transaction records more intuitive and systematic.
2. Data Persistence: The project utilizes text files as a persistent storage solution, allowing users to save transaction records on disk for future access and analysis. This approach is simple, user-friendly, and does not depend on complex database systems.
3. User Interaction Interface: The project offers a text-based user interface, allowing users to interact with the program through the command line. While this interface is straightforward, it is sufficient for basic financial management tasks.
4. Date Validation Functionality: Ensuring the correct date format for user input is crucial for any financial record system involving dates.
5. Adding and Editing Transaction Records: Users can easily add new transaction records or modify existing ones. This is a core functionality in personal finance management systems, allowing users to continuously update and correct their financial data.
6. Financial Report Generation: The ability to generate financial reports, including total income, total expenses, and net savings, helps users understand their financial situation and make data-driven decisions.
7. Viewing Transactions in a Date Range: Users can view financial transactions within a specific date range, which is particularly useful for tracking financial trends and patterns.

Overall, this project provides individuals with a comprehensive and user-friendly financial management tool through its structured data representation, data persistence, user interface design, date validation, and financial reporting features. These features combined make the tool capable of meeting the basic requirements of daily personal financial management while maintaining operational simplicity.
## Guide
How do we run your project? What should we do to see it in action? - Note this isn't installing, this is actual use of the project.. If it is a website, you can point towards the gui, use screenshots, etc talking about features.   

To run this personal finance assistant project, follow these steps:

1. Environment Setup: Ensure that Python is installed on your computer. Since this project is written in Python, running it requires a Python environment.
2. Obtain the Code: Save the project's code files to your computer. Typically, this includes a `.py` file, such as `personal_finance_assistant.py`
3. Launch the Program:  
   - Open a terminal or command-line interface.  
   - Navigate to the directory containing the project files.
   - Run the command python `personal_finance_assistant.py`
4. Use the Project:  
   - After the program starts, you will see a text menu listing different options, such as adding transactions, editing transactions, viewing financial reports, etc.  
   - Follow the prompts on the screen. For example, choose "1" to add a new transaction, then enter the date, description, type (income/expense), and amount as prompted.   
   - You can edit transaction records, view financial reports, or see transactions within a specific date range by selecting the corresponding menu options.  
   - To exit the program, choose the exit option (e.g., "5").
5. View and Analyze Data:  
-When you add, edit, or view transactions, the program will display relevant information in the terminal or command-line interface.  
-Financial reports will show key financial indicators such as total income, total expenses, and net savings.   
-When viewing transactions within a specific date range, you will see a list of all relevant transactions during that period.
6. Data Storage: All transaction records will be saved in a text file (e.g., `transactions.txt`), which you can view or back up at any time.

## Installation Instructions
If we wanted to run this project locally, what would we need to do?  If we need to get API key's include that information, and also command line startup commands to execute the project. If you have a lot of dependencies, you can also include a requirements.txt file, but make sure to include that we need to run `pip install -r requirements.txt` or something similar.
1. Python Installation:  
   - Ensure that Python is installed on your computer. This project is written in Python, so a Python environment is needed to run it.
2. Download Project Code:  
   - Download the project code to your computer.
3. Install Dependencies (if any):  
   - This project may not require any external libraries as it primarily uses Python's standard library.
4. Run the Project:  
   - Open a terminal or command prompt.
   - Navigate to the directory containing the downloaded Python script.
   - Run the command python personal_finance_assistant.py to launch the program.
5. API Key (if required):  
   - This project does not require any external APIs or keys. It is a standalone application that does not depend on external services.   

Following these steps, you should be able to run this personal finance assistant project locally.


## Code Review
Go over key aspects of code in this section. Both link to the file, include snippets in this report (make sure to use the [coding blocks](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code)).  Grading wise, we are looking for that you understand your code and what you did.  
  
1. Transaction class  
The `Transaction` class is the core of the project, representing a single financial transaction. This class includes basic attributes (such as date, description, type, and amount) and methods to handle this data.
```python
class Transaction:
    def __init__(self, date, description, type, amount):
        self.date = date
        self.description = description
        self.type = type
        self.amount = amount

    def __str__(self):
        return f"{self.date},{self.description},{self.type},{self.amount}"
```

2. Loading and Saving Transactions  
Use the `load_transactions` and `save_transactions` functions to load and save transaction data from and to a file. These functions handle file I/O operations, ensuring data persistence.
```python
def load_transactions() -> list:
    transactions = []
    try:
        with open(TRANSACTIONS_FILE, 'r', encoding='utf-8') as file:
            for line in file:
                transactions.append(Transaction.from_string(line))
    except FileNotFoundError:
        pass
    return transactions

def save_transactions(transactions):
    with open(TRANSACTIONS_FILE, 'w', encoding='utf-8') as file:
        for transaction in transactions:
            file.write(str(transaction) + '\n')
```
3. Adding and Editing Transactions  
The `add_transaction` and `edit_transaction` functions allow users to add new transaction records or edit existing ones. These functions prompt users for necessary data input and update the transaction list accordingly.
```python
def add_transaction(transactions):
    # ... Omitted input and validation parts ...
    transaction = Transaction(date, description, type, amount)
    transactions.append(transaction)
    save_transactions(transactions)

def edit_transaction(transactions):
    # ... Omitted logic for selecting and editing transactions ...
    # Update transaction records and save
    save_transactions(transactions)
```    
4. Generating Financial Reports  
The `generate_report` function is used to generate an overall financial report, displaying total income, total expenses, and net savings, among other information.    
```python
def generate_report(transactions):
    total_income = sum(t.amount for t in transactions if t.type == 'Income')
    total_expense = sum(t.amount for t in transactions if t.type == 'Expense')
    net_savings = total_income - total_expense
     # ... Output report details ...
```
5. Main Function  
The `main` function serves as the entry point of the program, providing a user interface that allows users to choose different operations.
```python
def main():
    transactions = load_transactions()
    while True:
        # ... Display menu and call different functions based on user input ...
        if choice == '1':
            add_transaction(transactions)
        # ... Handling for other options ...

if __name__ == "__main__":
    main()
```
These code snippets showcase the key parts of the project and its workings. From defining basic data structures (`Transaction` class) to handling file I/O operations, user interaction, and report generation, these code segments reflect a deep understanding of the overall structure and functionality of the project.
### Major Challenges
Key aspects could include pieces that your struggled on and/or pieces that you are proud of and want to show off.  
1. Data Persistence and File Handling: Ensuring the secure storage and retrieval of transaction data poses a challenge. Handling file I/O operations requires consideration of various exceptional cases, such as file non-existence or read/write errors. To address this challenge, exception handling mechanisms have been added in the code to ensure that even in the presence of errors, the user experience is minimally impacted.
2. User Input Validation: Ensuring the correct format of user-inputted data, especially for dates and amounts, is a challenge in the `add_transaction` and `edit_transaction` functionalities. Incorrect inputs could lead to program crashes or inaccurate data. By implementing rigorous input validation and error-handling logic, this challenge has been effectively overcome.
3. Code Organization and Structure: As the project's functionality expands, maintaining clear and well-organized code becomes a challenge. To tackle this issue, the code has been modularized, separating different functional logics into distinct functions. This approach enhances code readability and maintainability.
4. Concise yet Powerful User Interface: While the project utilizes a basic command-line interface, it offers rich functionality such as adding, editing, viewing transactions, and generating financial reports. This demonstrates the achievement of robust capabilities even within a straightforward interface.
5. Robust Error Handling: The project's error-handling mechanisms ensure the program's stability when encountering invalid inputs or other runtime errors. For instance, the date validation feature ensures users can only input valid date formats, mitigating potential data errors.
6. Scalability and Modular Design: The code's structure makes it easier to add new features in the future. 

## Example Runs
Explain how you documented running the project, and what we need to look for in your repository (text output from the project, small videos, links to videos on youtube of you running it, etc)

To ensure users can smoothly run and comprehend this personal finance assistant project, I've employed the following documentation and demonstration methods:
1. Detailed README File: Within the project repository, I've provided a comprehensive README file containing an overview of the project, installation guides, usage instructions, and feature descriptions. This file serves as the primary guide for users when initially encountering the project, detailing how to set up and run it.
2. Code Comments: Throughout the project code, I've added thorough comments to explain the workings of key functions and code blocks. These comments are intended to aid in understanding the internal logic of the project, especially for users not familiar with Python or financial applications.
3. Sample Outputs: In the documentation, I've included text output examples from when the project runs. These examples help users anticipate what they should see when using the project and serve as validation for correct operations.
4. Operational Video: I've created a brief video demonstrating how to run and utilize various features of the project, which has been uploaded to YouTube. The link to this video is provided in the README file. This visual demonstration is particularly helpful for understanding the practical operations of the project.  Video link: [code](url :https://www.youtube.com/watch?v=OC1KK_1DRlA)

When exploring my project repository, I recommend focusing on the following:

README File: Begin by reviewing it, as it provides fundamental information and guidance about the project.  

Commented Code: Browse through the code files to understand the project's structure and logic.  

Operationa Video: Watch the YouTube video for an intuitive operational demonstration.  [code](url :https://www.youtube.com/watch?v=OC1KK_1DRlA)

Sample Outputs: Examine the sample outputs to understand the expected results during project runtime.    
## Testing
How did you test your code? What did you do to make sure your code was correct? If you wrote unit tests, you can link to them here. If you did run tests, make sure you document them as text files, and include them in your submission.  
[unit tests](path)  
[integration tests](path)
> _Make it easy for us to know you *ran the project* and *tested the project* before you submitted this report!_


## Missing Features / What's Next
Focus on what you didn't get to do, and what you would do if you had more time, or things you would implement in the future. 
    
In the current version of the Personal Finance Assistant project, while some core features have been implemented, there are still several features and improvements that could be considered for future versions:

1. Graphical User Interface (GUI): The project is currently command-line-based, and a potential enhancement for future versions could be the development of a graphical user interface (GUI). A GUI would offer a more user-friendly and intuitive experience, making data viewing and manipulation more convenient, especially for users not familiar with command-line operations.
2. Data Visualization: Introducing data visualization features, such as generating charts for income and expenses, could be beneficial. This would help users gain a more visual understanding of their financial situation, enabling them to identify trends and patterns.
3. Budget Planning and Reminders: Adding budget planning functionality would allow users to set monthly or yearly budgets and receive reminders when approaching budget limits. This feature could assist users in better controlling their expenses. 

## Final Reflection
Write at least a paragraph about your experience in this course. What did you learn? What do you need to do to learn more? Key takeaways? etc.  

Embarking on the journey of learning programming as a beginner was both exhilarating and challenging. As a new learner entering the world of programming, the initial exposure to Python served as a welcoming introduction to the realm of programming languages. Python's syntax, known for its simplicity and readability, provided a gentle starting point. The process of writing those first lines of code felt like opening a door to a new dimension, where logical structures and problem-solving strategies became the building blocks for creating digital solutions.   
In the early stages, understanding basic concepts like variables, loops, and conditionals felt like navigating a maze of possibilities. The excitement of running that first "Hello, World!" program was accompanied by the realization that this was just the beginning of a vast coding adventure. Understanding the importance of indentation for code blocks and recognizing the significance of docstring added a layer of uniqueness to the learning process.  
To delve deeper into the world of Python and programming, further exploration is required. Completing projects, collaborating with classmates, and finding additional resources will be critical to reinforcing the foundation laid during these initial encounters. The key takeaway from this introduction is the understanding that programming is both an art and a science, and that continued curiosity and practice are essential to unlocking its full potential. As a beginner, the journey has just begun, and the road ahead is challenging.
