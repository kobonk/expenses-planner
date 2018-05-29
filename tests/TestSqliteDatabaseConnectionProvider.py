"""Unit tests for SqliteDatabaseConnectionProvider class"""
# import os
import sys
import unittest

sys.path.append("../")

from unittest import mock
from src.SqliteDatabaseConnectionProvider import SqliteDatabaseConnectionProvider

class TestSqliteDatabaseConnectionProvider(unittest.TestCase):
    """This is a test class for SqliteDatabaseConnectionProvider"""

    def setUp(self):
        self.database_path = "fake database path"
        self.fake_database_directory = "fake directory"
        self.provider = SqliteDatabaseConnectionProvider(self.database_path)

    def tearDown(self):
        self.database_path = None
        self.provider = None

    @mock.patch("src.SqliteDatabaseConnectionProvider.os")
    def test_no_database_file(self, mock_os):
        """Verifies if a new db directory is created in case it doesn't exist"""

        mock_os.path.dirname.return_value = self.fake_database_directory
        mock_os.path.exists.return_value = False
        mock_os.makedirs.return_value = True

        self.provider.get_connection()

        mock_os.makedirs.assert_called_with(self.fake_database_directory)

    @mock.patch("src.SqliteDatabaseConnectionProvider.os")
    @mock.patch("src.SqliteDatabaseConnectionProvider.sqlite3")
    def test_no_sqlite_connection(self, mock_sqlite, mock_os):
        """Verifies if code fails gracefully in case of no connection"""

        mock_os.path.dirname.return_value = self.fake_database_directory
        mock_os.path.exists.return_value = True
        mock_os.makedirs.return_value = True
        mock_sqlite.connect.side_effect = self.__make_sqlite_connect_fail

        with self.assertRaises(OSError) as context:
            self.provider.get_connection()

        self.assertEqual(context.exception.args[0], "Cannot connect!")

    def __make_sqlite_connect_fail(self, database_path):
        """This is a side effect function to make sqlite connection fail"""
        if database_path is self.database_path:
            raise OSError("Cannot connect!")

        return True

if __name__ == "__main__":
    unittest.main()
