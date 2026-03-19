
    
muppet_csv = r"C:\WiseOwl\files_and_folders\muppet.csv"

with open(muppet_csv, 'r') as x:
    content = x.read()
    lines = content.splitlines()
    print(lines)  