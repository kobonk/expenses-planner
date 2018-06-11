"""The module contains API for command-line user interactions"""
import uuid
from datetime import datetime
from src.Expense import Expense

class CommandLineInputProvider:
    """Interprets user input from the console"""
    def create_expense(self):
        """Creates a new Expense instance from the user input"""
        name = input("Expense name:")
        cost = input("Cost:")
        deadline = input("Deadline (YYYY-MM-DD):")
        plan_id = uuid.uuid4()

        return Expense(uuid.uuid4(), name, cost,
                       self.__convert_date_string_to_timestamp(deadline),
                       plan_id)

    def __convert_date_string_to_timestamp(self, date_string):
        """Converts date (YYYY-MM-DD) to a number"""
        year, month, day = map(int, date_string.split("-"))
        date = datetime(year, month, day)

        return date.timestamp()
