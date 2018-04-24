"""This is the main starting point of the application"""
import http.server
import sqlite3
import uuid

from enums import Weekdays, TimeUnits, PlanTypes
from SqliteExpensesPersister import SqliteExpensesPersister
from Expense import Expense

database_path = ".\dbs\expenses-planner.db"

expenses_persister = SqliteExpensesPersister(database_path)

fake_expense = Expense(
    uuid.uuid4(),
    "Another Cell Phone",
    1499.94,
    "2018-04-23",
    uuid.uuid4()
)

expenses_persister.add_expense(fake_expense)
