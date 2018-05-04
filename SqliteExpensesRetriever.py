from Expense import Expense
import os
import time
import sqlite3

class SqliteExpensesRetriever():
    
    def __init__(self, database_path, expenses_table_name):
        self.__database_path = database_path
        self.__expenses_table_name = expenses_table_name

    def retrieve_incoming_expenses(self):
        connection = self.__get_database_connection()
        cursor = connection.cursor()
        
        cursor.execute("""SELECT * FROM {table_name} 
                        WHERE deadline <= {current_time}""".format(
                            table_name=self.__expenses_table_name,
                            current_time=time.time()
                        ))

        rows = cursor.fetchall()
        expenses = []

        for row in rows:
            print(row)
            expenses.append(Expense(row[0], row[1], row[2], row[3], row[4], row[5]))

        return expenses

    def __get_database_connection(self):
        directory = os.path.dirname(self.__database_path)
        if not os.path.exists(directory):
            os.makedirs(directory)
            
        return sqlite3.connect(self.__database_path)
