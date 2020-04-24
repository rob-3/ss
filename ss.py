# Conservative Interest Calculator

# annual
lifetime_average_income = 12549
interest_rate = 6.06
savings_rate = 12.4

early_savings = lifetime_average_income / 2 * (savings_rate / 100)
mid_savings = lifetime_average_income * (savings_rate / 100)
late_savings = lifetime_average_income * 1.5 * (savings_rate / 100)
multiplier = 1 + (interest_rate / 100)
savings = 0

for year in range(21,36):
    savings *= multiplier
    savings += early_savings

for year in range(36,50):
    savings *= multiplier
    savings += mid_savings

for year in range(50,65):
    savings *= multiplier
    savings += late_savings

print(f"Final amount: ${round(savings, 2)}")
print(f"Rate of return: {round(savings/(mid_savings*44)*100, 2)}%")
