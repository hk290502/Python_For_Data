# The UK's Prime Ministers in the 21st century
prime_ministers = (
    "Tony Blair", "Gordon Brown",
    "David Cameron", "Theresa May",
    "Boris Johnson", "Liz Truss",
    "Rishi Sunak", "Placeholder Name"
)

pm_list = list(prime_ministers)

num_items = len(pm_list)

pm_list[num_items - 1] = "Your Name"

pm_list.sort()

for position, name in enumerate(pm_list, start=1):
    print(f"PM number {position} is {name}")