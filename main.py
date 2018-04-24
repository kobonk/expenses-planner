"""This is the main starting point of the application"""
import http.server
import sqlite3
import uuid

from enums import Weekdays, TimeUnits, PlanTypes
from SqliteExpensesPersister import SqliteExpensesPersister
from Expense import Expense

DATABASE_PATH = ".\dbs\expenses-planner.db"

def main():

    expenses_persister = SqliteExpensesPersister(DATABASE_PATH)

    fake_expense = Expense(
        uuid.uuid4(),
        "Another Cell Phone",
        1499.94,
        "2018-04-23",
        uuid.uuid4()
    )

    expenses_persister.add_expense(fake_expense)

main()
