# Expenses Planner

## Expense

    expense_id: String
    name: String
    cost: Double
    deadline: Date
    done: Boolean
    plan_id: String

## TimeUnits (Enum)

    Day
    Week
    Month
    Year

## Weekdays (Enum)

    Sunday
    Monday
    Tuesday
    Wednesday
    Thursday
    Friday
    Saturday

## PlanTypes (Enum)

    DayOfMonth
    WeekdayOfMonth
    EndDayOfMonth

## Repetition
Repeat the occurence every **[amount]** of **[type]** - i.e. every 2 days.

    amount: Integer
    type: <TimeUnits>

## ManualExpensePlanner
The user adds a single Expense manually.

    addExpense(name, cost, deadline): Expense

## AutomaticExpensePlanner
The user plans an Expense, which is later on repeated automatically.

    scheduleExpenses(name, cost, plan): Expense

    __calculateDate(year, month): Date
    
## Plan

    id: String
    startDate: Date
    type: <PlanTypes>
    repetition: Repetition
