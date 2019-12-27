import openpyxl


def read_test_data(sheet):
    wb = openpyxl.load_workbook('test_data.xlsx')
    ws = wb[sheet]
    list = []
    test_data = []
    for i in ws.rows:
        for row in i:
            list.append(row.value)
        test_data.append(list)
        list = []
    return test_data


def write_approver_data(approver):
    wb = openpyxl.load_workbook('test_data.xlsx')
    ws = wb['approver_list']
    ws.append(approver)
    wb.save('test_data.xlsx')


def clear_test_sheet(sheet):
    wb = openpyxl.load_workbook('test_data.xlsx')
    ws = wb[sheet]
    wb.remove(ws)
    wb.create_sheet(sheet)
    wb.save('test_data.xlsx')

