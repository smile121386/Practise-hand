from openpyxl import Workbook

#创建一个工作薄对象,也就是创建一个excel文档
wb = Workbook()

#指定当前显示（活动）的sheet对象
ws = wb.active

# 给A1单元格赋值
ws['A1'] = 42

# 一行添加多列数据
ws.append([1, 2, 3])

# 保存excel
wb.save("sample.xlsx")