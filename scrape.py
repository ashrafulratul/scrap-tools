import requests
from bs4 import BeautifulSoup
import xlsxwriter


req = requests.get("http://www.houzz.com/professionals/interior-designer/c/Washington--DC/p/0")

soup = BeautifulSoup(req.content)

# print(soup.prettify())

totalRow = soup.find_all("div", { "class" : "whiteCard" })


# Create an new Excel file.
dataBook = xlsxwriter.Workbook('demo.xlsx')
dataRow = dataBook.add_worksheet()

# Widen the first column to make the text clearer.
dataRow.set_column('A:B', 20)
dataRow.set_column('C:C', 60)

# Add a bold format to use to highlight cells.
bold = dataBook.add_format({'bold': True})


dataRow.write('A1', 'Title', bold)
dataRow.write('B1', 'Phone', bold)
dataRow.write('C1', 'Meta', bold)



for idx, sr in enumerate(totalRow):

	idx += 2
	title = sr.find_all("a", { "class" : 'pro-title' })[0].text
	phone = sr.find_all("span", { "class" : 'pro-phone' })[0].text
	description = sr.find_all("div", { "class" : 'pro-description' })[0].text
	meta = sr.find_all("div", { "class" : 'pro-meta' })[0].text

	dataRow.write('A{}'.format(idx), title)
	dataRow.write('B{}'.format(idx), phone)
	dataRow.write('C{}'.format(idx), meta)



dataBook.close()


 