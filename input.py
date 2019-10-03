from selenium import webdriver
import xlrd
import xlsxwriter

workbook = xlsxwriter.Workbook('containers_generated.xlsx')
worksheet = workbook.add_worksheet()
row = 0
col = 0


loc = "containers.xlsx"
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)
        

browser = webdriver.Chrome("\\Users\simic\Downloads\chromedriver")
browser.get("http://www.ictsi.hr/index.php/en/containers-tracking?fbclid=IwAR3S7tlXrquu090GqzSkA6qKPD86IBi6ThgW84FTwK2lAn-MJwiq9QPXoL4")


for i in range(sheet.nrows):
    sheet.cell_value(i, 0)
    
    text_field = browser.find_element_by_name("unit")

    text_field.send_keys(sheet.cell_value(i, 0))

    submit_button = browser.find_element_by_class_name("readon")
    submit_button.click()
    
    worksheet.write(row, col, sheet.cell_value(i, 0))
    worksheet.write(row, col + 1, 'dedo')
    worksheet.write(row, col + 2, 'bruh')
    worksheet.write(row, col + 3, 'pomalo')
    row += 1
        

workbook.close()