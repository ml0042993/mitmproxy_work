import openpyxl


def control_xlsx():
    wb = openpyxl.load_workbook("mitmproxy_work\exam.xlsx")
    # sheet = wb.worksheets[0]
    sheet = wb['Sheet1']
    aaa = list(sheet.rows)[2]
    for row in list(sheet.rows)[4]:
        for i in row:
            if isinstance(i.value, str):
                print(i.value)
control_xlsx()