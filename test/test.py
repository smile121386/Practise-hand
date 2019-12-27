import openpyxl


wb = openpyxl.load_workbook('test.xlsx')
ws = wb['login_info']
wb.remove(ws)
wb.create_sheet('login_info')
wb.save('test.xlsx')
