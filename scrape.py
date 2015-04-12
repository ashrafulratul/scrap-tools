import requests
from bs4 import BeautifulSoup
import xlsxwriter




# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()

# Widen the first column to make the text clearer.
worksheet.set_column('A:C', 20)

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

# Write some simple text.
worksheet.write('B1', 'Hello')

# Text with formatting.
worksheet.write('A2', 'World', bold)

# Write some numbers, with row/column notation.
worksheet.write(2, 1, 123)
worksheet.write(3, 0, 123.456)

# Insert an image.
worksheet.insert_image('B5', 'logo.png')

workbook.close()





req = requests.get("http://www.houzz.com/professionals/interior-designer/c/Washington--DC/p/0")

soup = BeautifulSoup(req.content)

# print(soup.prettify())

totalRow = soup.find_all("div", { "class" : "whiteCard" })

customList = []

for sr in totalRow:
	title = sr.find_all("a", { "class" : 'pro-title' })[0].text
	phone = sr.find_all("span", { "class" : 'pro-phone' })[0].text

	customList.append([title, phone])





print(customList)
print(len(customList))

 