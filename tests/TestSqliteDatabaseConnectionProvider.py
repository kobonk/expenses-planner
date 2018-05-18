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
        self.provider = SqliteDatabaseConnectionProvider(self.database_path)

    def tearDown(self):
        self.database_path = None
        self.provider = None

    @mock.patch("src.SqliteDatabaseConnectionProvider.os")
    @mock.patch("src.SqliteDatabaseConnectionProvider.sqlite3")
    def test_connection_failure(self, mock_sqlite, mock_os):
        """Verifies if code fails gracefully in case of no connection"""

        mock_os.path.dirname.return_value = "fake directory"
        mock_os.path.exists.return_value = False

        self.provider.get_connection()

        mock_os.path.dirname.assert_called_with(self.database_path)
        mock_os.makedirs.assert_called_with("fake directory")

        mock_sqlite.connect.assert_called_with(self.database_path)

if __name__ == "__main__":
    unittest.main()
