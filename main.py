"""This is the main starting point of the application"""
import http.server
import os
import re
import sqlite3
import time
import uuid

from src.enums import Weekdays, TimeUnits, PlanTypes
from src.Expense import Expense
from src.renderer.TexttableExpensesRenderer import TexttableExpensesRenderer
from src.SqliteExpensesRetriever import SqliteExpensesRetriever

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
DATABASE_PATH = r"{DIR_PATH}\dbs\expenses-planner.db".format(**locals()).replace("\\", "\\\\")
EXPENSES_TABLE_NAME = "expenses"

def main():
    expenses_retriever = SqliteExpensesRetriever(DATABASE_PATH, EXPENSES_TABLE_NAME)
    expenses = expenses_retriever.retrieve_incoming_expenses()

    renderer = TexttableExpensesRenderer()
    renderer.render_expenses(expenses)
    renderer.render_expense(expenses[0])

main()
