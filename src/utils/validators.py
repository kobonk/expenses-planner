"""The module contains validation functions for various input values"""

from datetime import datetime

def check_if_is_string(name, value):
    """Raises an exception if value is not a string"""
    if not isinstance(value, str):
        raise ValueError("{name} must be a string".format(name=name))

def check_if_is_not_empty(name, value):
    """Raises an exception is value is empty"""
    if not value:
        raise ValueError("{name} must not be empty".format(name=name))

def check_if_is_non_empty_string(name, value):
    """Raises an exception if value is an empty string"""
    check_if_is_not_empty(name, value)
    check_if_is_string(name, value)

def check_if_is_numeric(name, value):
    """Raises an exception if value is not numeric"""
    try:
        float(value)
    except ValueError:
        raise ValueError("{name} must be a number".format(name=name))

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
        raise ValueError("{name} must match the pattern '{value_format}'"
                        .format(name=name, value_format=value_format))
