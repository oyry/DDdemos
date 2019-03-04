from prettytable import PrettyTable
from Loginfo import log
from Loginfo import request
from Loginfo import excel

logging=log.get_logger()
CASE_NUMBER = 0
CASE_NAME = 1
CASE_URL=2
CASE_QUERYSTRING=3
CASE_DATA =4
CASE_HEADERS =5
CASE_METHOD =6
CASE_CODE =7

"""
SQL_ROW = 0      # 预执行SQL的行号
SQL_COL = 1      # 预执行SQL的列号
"""
FILE_NAME = 'test.xlsx'
class ApiTest:
    """接口测试业务类"""
    filename = FILE_NAME
    def __init__(self):
        pass
    def get_excel_sheet(self, path, module):
        """依据模块名获取sheet"""
        excel.open_excel(path)
        return excel.get_sheet(module)
    def run_test(self, sheet, url):
        """再执行测试用例"""
        rows = excel.get_rows(sheet)
        fail = 0
        for i in range(2, rows):
            testNumber = str(int(excel.get_content(sheet,i,CASE_NUMBER)))
            testName = excel.get_content(sheet,i,CASE_NAME)
            testUrl = excel.get_content(sheet,i,CASE_URL)
            testUrl = url + testUrl
            testQuerystring = excel.get_content(sheet,i,CASE_QUERYSTRING)
            testData = excel.get_content(sheet,i,CASE_DATA)
            testHeaders = eval(excel.get_content(sheet,i,CASE_HEADERS))
            testMethod = excel.get_content(sheet,i,CASE_METHOD)
            testCode = excel.get_content(sheet,i,CASE_CODE)
            actualCode = request.api(testMethod,testUrl,testQuerystring,testData,testHeaders)
            expectCode = str(int(testCode))
            failResults = PrettyTable(["Number", "Method", "Url","Querystring", "Data", "ActualCode", "ExpectCode"])
            failResults.align["Number"] = "l"
            failResults.padding_width = 1
            failResults.add_row([testNumber, testMethod, testUrl,testQuerystring, testData, actualCode, expectCode])
            if actualCode != expectCode:
                logging.info("FailCase %s", testName)
                print("FailureInfo")
                print(failResults)
                fail += 1
            else:
                logging.info("Number %s", testNumber)
                logging.info("TrueCase %s", testName)
        if fail > 0:
            return False
        return True