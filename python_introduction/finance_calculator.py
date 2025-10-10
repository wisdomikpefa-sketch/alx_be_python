monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses
projected_savings = monthly_savings * 12 + (monthly_savings * 0.05 * 12)

print("your monthly_savings are:", monthly_savings)
print("projected savings after one year, with interest, is", projected_savings)

age should be