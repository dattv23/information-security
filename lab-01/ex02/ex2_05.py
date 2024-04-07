number_of_working_hours = float(input("Enter the number of hours worked per week: "))
hourly_wage = float(input("Enter hourly compensation as standard: "))
standard_hours = 44
hours_exceed_standard = max(0, number_of_working_hours - standard_hours)

actually_received = (
    standard_hours * hourly_wage + hours_exceed_standard * hourly_wage * 1.5
)

print(f"The actual amount of money received by the employee: {actually_received}$")
