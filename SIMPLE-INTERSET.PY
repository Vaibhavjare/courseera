def simple_interest(principal, rate, time):
    # Calculate simple interest
    SI = (principal * rate * time) / 100
    return SI

def compound_interest(principal, rate, time):
    # Calculate compound interest
    amount = principal * (1 + rate / 100) ** time
    CI = amount - principal
    return CI

# Get user input for principal, rate, and time
print("Interest Calculation")
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period in years: "))

# Calculate Simple Interest
SI = simple_interest(principal, rate, time)
print(f"\nThe Simple Interest is: {SI:.2f}")

# Calculate Compound Interest
CI = compound_interest(principal, rate, time)
print(f"\nThe Compound Interest is: {CI:.2f}")
