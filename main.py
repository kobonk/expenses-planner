"""This is the main starting point of the application"""
import os

from src.input_provider.CommandLineInputProvider import CommandLineInputProvider
from src.renderer.TexttableExpensesRenderer import TexttableExpensesRenderer
from src.SqliteExpensesRetriever import SqliteExpensesRetriever

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
DATABASE_PATH = r"{DIR_PATH}\dbs\expenses-planner.db".format(**locals()).replace("\\", "\\\\")
EXPENSES_TABLE_NAME = "expenses"

def main():
    """Main application entry point"""
    os.system("cls" if os.name == "nt" else "clear")

    expenses_retriever = SqliteExpensesRetriever(DATABASE_PATH, EXPENSES_TABLE_NAME)
    expenses = expenses_retriever.retrieve_unpaid_expenses()
    renderer = TexttableExpensesRenderer()

    if expenses:
        renderer.render_expenses(expenses)
    else:
        print("No unpaid Expenses found.")

    expense = CommandLineInputProvider().create_expense()
    print("\n\n")
    renderer.render_expense(expense)

main()
