"""The module uses Texttable library to display Expenses"""
from texttable import Texttable
from src.renderer.ExpensesRenderer import ExpensesRenderer

class TexttableExpensesRenderer(ExpensesRenderer):
    """The class displays Expenses as a table"""

    def render_expenses(self, expenses):
        """Displays a list of Expenses in a table"""
        table = Texttable()
        table.set_cols_align(["l", "r", "r"])
        table.header(["Name", "Cost", "Deadline"])
        table.set_cols_dtype(["t", "f", "t"])
        table.set_precision(2)
        table.set_deco(Texttable.HEADER | Texttable.HLINES)

        for expense in expenses:
            table.add_row([expense.get_name(), expense.get_cost(), expense.get_deadline_string()])

        print(table.draw())

    def render_expense(self, expense):
        """Displays a single Expense in a table"""
        table = Texttable()
        table.set_cols_align(["l", "l"])
        table.set_precision(2)
        table.set_deco(Texttable.HLINES)
        table.add_row(["Id:", expense.get_expense_id()])
        table.add_row(["Name:", expense.get_name()])
        table.add_row(["Cost:", expense.get_cost()])
        table.add_row(["Deadline:", expense.get_deadline_string()])
        table.add_row(["Done:", expense.is_done_string()])

        print(table.draw())
