january_csv = r"C:\WiseOwl\files_and_folders\January.csv"
febuary_csv = r"C:\WiseOwl\files_and_folders\February.csv"
march_csv = r"C:\WiseOwl\files_and_folders\March.csv"
april_csv = r"C:\WiseOwl\files_and_folders\April.csv"

csv_files = [january_csv, febuary_csv, march_csv, april_csv]

for csv_file in csv_files:
    with open(csv_file, 'r') as x:
        lines = x.read().splitlines()
        for line in lines[1:]: 
            parts = line.split(",")
            print(f"On {parts[0]} spent {parts[1]} in {parts[2]}")