import xlrd
workbook = None

def open_excel(path):
     global workbook
     if (workbook == None):
        workbook = xlrd.open_workbook(path, on_demand=True)

def get_sheet(sheetName):
     global workbook
     return workbook.sheet_by_name(sheetName)

def get_rows(sheet):
    return sheet.nrows

def get_content(sheet, row, col):
    return sheet.cell(row, col).value

def release(path):
    global workbook
    workbook.release_resources()
    del workbook