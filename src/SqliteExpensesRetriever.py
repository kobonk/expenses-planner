import os
import time
import sqlite3
from src.Expense import Expense

class SqliteExpensesRetriever():
    
    def __init__(self, database_path, expenses_table_name):
        self.__database_path = database_path
        self.__expenses_table_name = expenses_table_name

    def retrieve_incoming_expenses(self):
        """Returns future Expenses"""
        rows = self.__get_rows("""SELECT * FROM {table_name} 
                        WHERE deadline >= {current_time}""".format(
                            table_name=self.__expenses_table_name,
                            current_time=time.time()
                        ))

        return self.__get_expenses_table(rows)

    def retrieve_unpaid_expenses(self):
        """Returns past and future unpaid Expenses"""
        rows = self.__get_rows("""SELECT * FROM {table_name} 
                        WHERE done = '{is_done}'
                        ORDER BY deadline ASC""".format(
                            table_name=self.__expenses_table_name,
                            current_time=time.time(),
                            is_done=int(False)
                        ))

        return self.__get_expenses_table(rows)

    def __get_rows(self, query):
        connection = self.__get_database_connection()
        cursor = connection.cursor()
        
        cursor.execute(query)

        return cursor.fetchall()

    def __get_expenses_table(self, rows):
        expenses = []

        for row in rows:
            expenses.append(self.__convert_table_row_to_expense(row))

        return expenses

    def __convert_table_row_to_expense(self, table_row):
        return Expense(table_row[0], table_row[1], table_row[2], table_row[3],
                       table_row[4], table_row[5])

    def __get_database_connection(self):
        directory = os.path.dirname(self.__database_path)
        if not os.path.exists(directory):
            os.makedirs(directory)
            
        return sqlite3.connect(self.__database_path)
