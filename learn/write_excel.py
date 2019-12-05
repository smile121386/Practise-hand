import openpyxl


wb = openpyxl.Workbook('a.xlsx')
ws = wb.active
a = ws.cell(row=1, column=1, value=2)
