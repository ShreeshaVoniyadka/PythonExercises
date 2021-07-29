import openpyxl
workbook=openpyxl.load_workbook("")
sheet =workbook.active
#change title
sheet.title=""
#print sheet with specifics
print(sheet['A1'],"value")
#....blah blah more values similar to above
#saving excel file
workbook.save("")
