monthly_income = int(input("Enter the monthly income:"))
total_monthly_expenses = int(input("Enter your monthly expenses:"))

monthly_savings = monthly_income - total_monthly_expenses 

interest_rate = 0.05

annual_savings = monthly_savings * 12
interest = annual_savings * interest_rate
projected_savings = annual_savings + interest

print(f"Your monthly savings is: {monthly_savings}")
print(f"Your projected annual savings with interest is: {projected_savings}")
