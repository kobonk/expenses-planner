"""Uses SqlLite to save and update Expenses in the database"""
import sqlite3

class SqliteExpensesPersister:
    """Persists Expenses data in a database"""
    
    def __init__(self, database_path):
        self.__database_path = database_path
        self.__expenses_table_name = "expenses"

        self.__create_expenses_table()
    
    def add_expense(self, expense):
        """Adds a new Expense to database"""

        connection = self.__get_database_connection()
        cursor = connection.cursor()

        cursor.execute("""INSERT INTO {table_name} (
                        expense_id, 
                        name, 
                        cost, 
                        deadline, 
                        plan_id, 
                        done
                    ) VALUES (
                        '{e_id}', 
                        '{e_name}', 
                        {e_cost}, 
                        '{e_deadline}', 
                        '{p_id}', 
                        {e_done})"""
                    .format(
                        table_name=self.__expenses_table_name,
                        e_id=expense.get_expense_id(), 
                        e_name=expense.get_name(),
                        e_cost=expense.get_cost(),
                        e_deadline=expense.get_deadline(),
                        p_id=expense.get_plan_id(),
                        e_done=int(expense.is_done()))
        )

        connection.commit()
        connection.close()

    def update_expense(self, expense):
        """Updates existing Expense in database"""

    def __get_database_connection(self):
        return sqlite3.connect(self.__database_path)

    def __create_expenses_table(self):
        """Creates the Expenses table in the database"""

        connection = self.__get_database_connection()
        cursor = connection.cursor()
        
        # cursor.execute("DROP TABLE IF EXISTS expenses")
        cursor.execute("""CREATE TABLE IF NOT EXISTS {table_name} (
                        expense_id  TEXT PRIMARY KEY, 
                        name TEXT, 
                        cost REAL, 
                        deadline TEXT, 
                        plan_id TEXT, 
                        done INTEGER)"""
                        .format(table_name=self.__expenses_table_name)
        )
        
        connection.commit()
        connection.close()
