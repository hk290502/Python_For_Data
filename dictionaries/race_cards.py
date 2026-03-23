GP23 = r"C:\WiseOwl\dictionaries\grand_prix_23.csv"

race_events = {}

with open(GP23, 'r') as x:
    content = x.read()
    lines = content.splitlines()
    for line in lines:
        parts = line.split(',')
        race_name = parts[1]
        race_events[race_name] = [parts[0], parts[2], parts[3]]

for key, value in race_events.items():
    print(f"Details for {key}: {value}")
    
input_name = "New York GP"

if input_name in race_events:
    print(race_events)
else:
    print(f"{input_name} not found")

