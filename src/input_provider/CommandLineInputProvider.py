"""The module contains API for command-line user interactions"""
import uuid
from datetime import datetime
from src.Expense import Expense
from src.utils.validators import check_if_is_non_empty_string, check_if_is_numeric

class CommandLineInputProvider:
    """Interprets user input from the console"""
    def create_expense(self):
        """Creates a new Expense instance from the user input"""
        name = self.__get_name_input()
        cost = self.__get_cost_input()
        deadline = input("Deadline (YYYY-MM-DD):")
        plan_id = uuid.uuid4()

        return Expense(uuid.uuid4(), name, cost,
                       self.__convert_date_string_to_timestamp(deadline),
                       plan_id)

    def __get_name_input(self):
        """Retrieves the name of the Expense from the user"""
        name = input("Expense name: ")

        try:
            check_if_is_non_empty_string("Expense name", name)
        except ValueError as exception:
            print("ERROR: {exception}".format(exception=exception))
            self.__get_name_input()

        return name

    def __get_cost_input(self):
        """Retrieves the cost of the Expense from the user"""
        cost = input("Cost:")

        try:
            check_if_is_numeric("Cost", cost)
        except ValueError as exception:
            print("ERROR: {exception}".format(exception=exception))
            self.__get_cost_input()

    def __convert_date_string_to_timestamp(self, date_string):
        """Converts date (YYYY-MM-DD) to a number"""
        year, month, day = map(int, date_string.split("-"))
        date = datetime(year, month, day)

        return date.timestamp()
