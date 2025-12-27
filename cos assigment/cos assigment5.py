single_brackets = [
    (0.10, 0, 8350),
    (0.15, 8351, 33950),
    (0.25, 33951, 82250),
    (0.28, 82251, 171550),
    (0.33, 171551, 372950),
    (0.35, 372951, None)
]

joint_brackets = [
    (0.10, 0, 16700),
    (0.15, 16701, 67900),
    (0.25, 67901, 137050),
    (0.28, 137051, 208850),
    (0.33, 208851, 372950),
    (0.35, 372951, None)
]

separate_brackets = [
    (0.10, 0, 8350),
    (0.15, 8351, 33950),
    (0.25, 33951, 68525),
    (0.28, 68526, 104425),
    (0.33, 104426, 186475),
    (0.35, 186476, None)
]

head_brackets = [
    (0.10, 0, 11950),
    (0.15, 11951, 45500),
    (0.25, 45501, 117450),
    (0.28, 117451, 190200),
    (0.33, 190201, 372950),
    (0.35, 372951, None)
]

# Function to calculate tax based on income and brackets
def calculate_tax(income, brackets):
    tax = 0.0
    prev_upper = 0
    for rate, lower, upper in brackets:
        if income <= prev_upper:
            break
        if upper is None:
            # Highest bracket
            tax += (income - prev_upper) * rate
        else:
            taxable_in_bracket = min(income, upper) - prev_upper
            if taxable_in_bracket > 0:
                tax += taxable_in_bracket * rate
        prev_upper = lower - 1 if upper is not None else lower
    return tax

# Main program
print("2009 US Federal Income Tax Calculator")
print("Filing statuses:")
print("0 - Single")
print("1 - Married Filing Jointly or Qualifying Widow(er)")
print("2 - Married Filing Separately")
print("3 - Head of Household")

# Input filing status
while True:
    try:
        status = int(input("\nEnter filing status (0-3): "))
        if status in [0, 1, 2, 3]:
            break
        else:
            print("Please enter a number between 0 and 3.")
    except ValueError:
        print("Please enter a valid number.")

# Input taxable income
while True:
    try:
        income = float(input("Enter taxable income: $"))
        if income >= 0:
            break
        else:
            print("Income cannot be negative.")
    except ValueError:
        print("Please enter a valid number.")

# Select brackets based on status
if status == 0:
    brackets = single_brackets
    status_name = "Single"
elif status == 1:
    brackets = joint_brackets
    status_name = "Married Filing Jointly or Qualifying Widow(er)"
elif status == 2:
    brackets = separate_brackets
    status_name = "Married Filing Separately"
else:
    brackets = head_brackets
    status_name = "Head of Household"

# Calculate tax
tax = calculate_tax(income, brackets)

# Output result
print(f"\nFor {status_name} with taxable income ${income:,.2f}:")
print(f"Federal income tax owed: ${tax:,.2f}")