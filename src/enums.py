"""The module contains a set of global enumerables"""

def enum(**enums):
    return type("Enum", (), enums)

Weekdays = enum(
    Sunday=1,
    Monday=2,
    Tuesday=3,
    Wednesday=4,
    Thursday=5,
    Friday=6,
    Saturday=7
)

TimeUnits = enum(
    Day="d",
    Week="w",
    Month="m",
    Year="y"
)

PlanTypes = enum(
    DayOfMonth="dom",
    WeekdayOfMonth="wom",
    BackDayOfMonth="bdom"
)
