"""The module uses Texttable library to display Expenses"""
from texttable import Texttable
from src.renderer.ExpensesRenderer import ExpensesRenderer

class TexttableExpensesRenderer(ExpensesRenderer):
    """The class displays Expenses as a table"""

    def render(self, expenses):
        """Displays as Texttable containing Expenses"""
        table = Texttable()
        table.add_row(["Name", "Cost", "Deadline"])

        for expense in expenses:
            table.add_row([expense.get_name(), expense.get_cost(), expense.get_deadline_string()])

        print(table.draw())
