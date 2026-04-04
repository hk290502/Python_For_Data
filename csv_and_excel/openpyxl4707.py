import openpyxl


workbook_variable = openpyxl.Workbook()
worksheet_variable = workbook_variable.active


worksheet_variable.cell(row=1, column=1).value = 33 

workbook_variable.save("my_spreadsheet.xlsx")

workbook_variable.close()