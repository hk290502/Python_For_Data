import openpyxl

# Open the workbook containing the list of plants
workbook = openpyxl.load_workbook("csv_and_excel/plants.xlsx")

# Get a reference to the first sheet (called Sheet1)
sheet = workbook["Sheet1"]

# Get a reference to cell A2
current_cell = sheet["A2"]

print("Plants not in stock")
print("-" * 20)

# Keep going down until you hit a blank cell
while current_cell.value is not None:
    # Check the value 7 columns to the right (column A + 7 = column H)
    offset_cell = current_cell.offset(0, 7)
    
    # If this cell is "No", print out this plant's name
    if offset_cell.value == "No":
        print(current_cell.value)
    
    # Move down one row
    current_cell = current_cell.offset(1, 0)

workbook.close()
