"""The module contains validation functions for various input values"""

from datetime import datetime

def check_if_is_string(name, value):
    """Raises an exception if value is not a string"""
    if not isinstance(value, str):
        raise Exception("{name} must be a string".format(name=name))

def check_if_is_non_empty_string(name, value):
    """Raises an exception if value is an empty string"""
    check_if_is_string(name, value)

    if not value:
        raise Exception("{name} must not be empty".format(name=name))

def check_if_is_date_string(name, value, value_format):
    """Raises an exception if value is not a properly formatted date string"""
    check_if_is_non_empty_string(name, value)

    def create_date_pattern():
        """Creates a date pattern string for strptime method"""
        if value_format == "YYYY-MM-DD":
            return "%y-%m-%d"

    try:
        datetime.strptime(value, create_date_pattern())
    except ValueError:
        raise Exception("{name} must match the pattern '{value_format}'"
                        .format(name=name, value_format=value_format))
