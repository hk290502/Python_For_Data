import openpyxl

# 1. Create the workbook and select the active sheet
workbook_variable = openpyxl.Workbook()
worksheet_variable = workbook_variable.active

# 2. Assign a value to a specific cell (Row 1, Column 1)
# Note: openpyxl uses 1-based indexing (1 is the first row/column)
worksheet_variable.cell(row=1, column=1).value = 33 

# 3. Save using a filename string
workbook_variable.save("my_spreadsheet.xlsx")

# 4. Close the workbook to free up resources
workbook_variable.close()