"""The module is responsible for displaying Expenses data"""

class ExpensesRenderer:
    """This is an abstract class which provides proper interface"""

    def render(self, expenses):
        """The method should display the list of expenses"""
        raise Exception("Not Implemented")
