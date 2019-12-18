import openpyxl


def read_login_data():
    wb = openpyxl.load_workbook('test_data.xlsx')
    ws = wb['login_data']
    test_data = []
    for i in list(ws.rows)[1]:
        test_data.append(i.value)
    return test_data


