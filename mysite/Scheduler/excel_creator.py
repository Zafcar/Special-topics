import sys
import xlsxwriter
sys.path.append('../')

from Specialtopic.admin import Student_databaseResource, System_databaseResource

def trial():
    dataset = Student_databaseResource().export()
    dataset = str(dataset.csv).split('\r\n')
    del dataset[-1]
    
    
    book = xlsxwriter.Workbook('Example2.xlsx')
    sheet = book.add_worksheet()
    row = 0



    for value in dataset:
        col_1, col_2 = value.split(",")
        sheet.write(row, 0, col_1)
        sheet.write(row, 1, col_2)
        row += 1
    book.close()
    
