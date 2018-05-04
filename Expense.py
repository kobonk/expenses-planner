"""The module contains Expense class"""

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
        return self.__expense_id

    def get_name(self):
        return self.__name

    def get_cost(self):
        return self.__cost

    def get_deadline(self):
        return self.__deadline

    def get_plan_id(self):
        return self.__plan_id

    def is_done(self):
        return self.__done

    def create_builder(self):
        return Builder(self)

    def to_string(self):
        return "---------\nExpense {id}:\n---------\nName: {name}\nCost: {cost}".format(id=self.__expense_id, name=self.__name, cost=self.__cost)

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
        return self.__expense

    def mark_as_done(self):
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
        self.__expense = Expense(
            self.__expense.get_expense_id(),
            self.__expense.get_name(),
            self.__expense.get_cost(),
            self.__expense.get_deadline(),
            self.__expense.get_plan_id(),
            False
        )
        return self
