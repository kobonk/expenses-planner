"""The module contains Expense class"""
import time

class Expense:
    """The class is a model for a single planned Expense"""

    def __init__(self, expense_id, name, cost, deadline, plan_id, done=False):
        self.__expense_id = expense_id
        self.__name = name
        self.__cost = cost
        self.__deadline = deadline
        self.__plan_id = plan_id
        self.__done = done

    def get_expense_id(self):
        """Returns the id of the Expense"""
        return self.__expense_id

    def get_name(self):
        """Returns the name of the Expense"""
        return self.__name

    def get_cost(self):
        """Returns the cost of the Expense"""
        return self.__cost

    def get_deadline(self):
        """Returns the deadline (seconds since epoch) of the Expense"""
        return self.__deadline

    def get_plan_id(self):
        """Returns the id of the plan applied to the Expense"""
        return self.__plan_id

    def is_done(self):
        """Returns true if the planned Expense has been paid"""
        return self.__done

    def is_done_string(self):
        """Returns Yes if the Expense has been paid and No if otherwise"""
        if self.__done:
            return "Yes"

        return "No"

    def create_builder(self):
        """Creates an instance of a Builder object"""
        return Builder(self)

    def get_deadline_string(self):
        """Returns the deadline in form of user-friendly string"""
        return time.ctime(self.__deadline)

    def to_string(self):
        """Returns a string representation of Expense object"""
        return ("------------------------------------------------------\n"
                "Expense {id}:\n"
                "------------------------------------------------------\n"
                "Name: {name}\n"
                "Cost: {cost}\n"
                "Deadline: {deadline}"
               ).format(id=self.__expense_id, name=self.__name,
                        cost=self.__cost, deadline=self.get_deadline_string())

class Builder:
    """Builds a new instance of Expense"""

    def __init__(self, expense):
        self.__expense = Expense(
            expense.get_expense_id(),
            expense.get_name(),
            expense.get_cost(),
            expense.get_deadline(),
            expense.get_plan_id(),
            expense.is_done()
        )

    def build(self):
        """Returns the built instance of Expense"""
        return self.__expense

    def mark_as_done(self):
        """Marks the Expense as done (paid)"""
        self.__expense = Expense(
            self.__expense.get_expense_id(),
            self.__expense.get_name(),
            self.__expense.get_cost(),
            self.__expense.get_deadline(),
            self.__expense.get_plan_id(),
            True
        )
        return self

    def mark_as_not_done(self):
        """Marks the Expense as not done (not paid)"""
        self.__expense = Expense(
            self.__expense.get_expense_id(),
            self.__expense.get_name(),
            self.__expense.get_cost(),
            self.__expense.get_deadline(),
            self.__expense.get_plan_id(),
            False
        )
        return self
