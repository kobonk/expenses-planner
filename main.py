"""This is the main starting point of the application"""
import http.server
import os
import re
import sqlite3
import time
import uuid

from src.enums import Weekdays, TimeUnits, PlanTypes
from src.SqliteExpensesPersister import SqliteExpensesPersister
from src.SqliteExpensesRetriever import SqliteExpensesRetriever
from src.Expense import Expense

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
DATABASE_PATH = r"{DIR_PATH}\dbs\expenses-planner.db".format(**locals()).replace("\\", "\\\\")
EXPENSES_TABLE_NAME = "expenses"

def main():

    expenses_persister = SqliteExpensesPersister(DATABASE_PATH, EXPENSES_TABLE_NAME)
    expenses_retriever = SqliteExpensesRetriever(DATABASE_PATH, EXPENSES_TABLE_NAME)

    fake_expense = Expense(
        uuid.uuid4(),
        "Another Cell Phone",
        1499.94,
        time.time(),
        uuid.uuid4()
    )

    # expenses_persister.add_expense(fake_expense)
    expenses = expenses_retriever.retrieve_incoming_expenses()

    for expense in expenses:
        print(expense.to_string())

main()
