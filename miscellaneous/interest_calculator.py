def greet_user(name):
    print(f"Hello, {name}!")

def calculate_interest(principal, rate, years):
    return (principal * rate * years)/100

def calculate_final_amount(principal, interest):
    return principal + interest

name = str(input("Enter your name: "))
principal = int(input("\nEnter principal (£): "))
years = int(input("Enter years: "))
rate = float(input("\nEnter annual interest rate (%): "))

interest  = calculate_interest(principal, rate, years)
final =  calculate_final_amount(principal, interest)

print()
greet_user(name)
print(f"Interest earned: £{interest}")
print(f"Final Amount: £{final}")
    