"""The module is responsible for displaying Expenses data"""

class ExpensesRenderer:
    """This is an abstract class which provides proper interface"""

    def render_expenses(self, expenses):
        """The method should display the list of expenses"""
        raise Exception("Not Implemented")

    def render_expense(self, expense):
        """The method should display the details of an expenses"""
        raise Exception("Not Implemented")
