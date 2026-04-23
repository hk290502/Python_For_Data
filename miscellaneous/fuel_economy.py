def greet_user(name):
    print(f"Hello, {name}!")

def calculate_gallons(distance, mpg):
    return distance / mpg

def calculate_cost(gallons, price_per_gallon):
    return gallons * price_per_gallon

# Main script
name = input("Enter your name: ")
distance = int(input("Enter trip distance (miles): "))
mpg = float(input("Enter fuel economy (mpg): "))
price_per_gallon = float(input("Enter petrol price (£/gallon): "))

gallons = calculate_gallons(distance,mpg)
trip_cost = calculate_cost(gallons, price_per_gallon)

print()
greet_user(name)
print(f"Gallons needed: {gallons}")
print(f"Trip cost: £{trip_cost}")