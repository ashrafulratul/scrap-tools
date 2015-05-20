import requests
from bs4 import BeautifulSoup
import xlsxwriter


# User Input
url = raw_input("Page link:") or ""
totalPage = raw_input("Total Page[1]:") or 1
rowDiff = raw_input("Per Page Data[15]:") or 15
file_name = raw_input("Saved File Name:")
# -----


# Create an new Excel file.
dataBook = xlsxwriter.Workbook('upload/{}.xlsx'.format(file_name))
dataRow = dataBook.add_worksheet()

# Widen the first column to make the text clearer.
dataRow.set_column('A:B', 20)
dataRow.set_column('C:C', 60)

# Add a bold format to use to highlight cells.
bold = dataBook.add_format({'bold': True})


dataRow.write('A1', 'Title', bold)
dataRow.write('B1', 'Phone', bold)
dataRow.write('C1', 'Meta', bold)




rowID = 1
for i in range(int(totalPage)):

	req = requests.get("{}/p/{}".format(str(url), (i*rowDiff)))

	# req = requests.get("http://www.houzz.com/professionals/interior-designer/c/Washington--DC/p/0")

	soup = BeautifulSoup(req.content)

	totalRow = soup.find_all("div", { "class" : "whiteCard" })
	# print(soup.prettify())

	for idx, sr in enumerate(totalRow):

		rowID += 1
		title = sr.find_all("a", { "class" : 'pro-title' })[0].text
		phone = sr.find_all("span", { "class" : 'pro-phone' })[0].text
		description = sr.find_all("div", { "class" : 'pro-description' })[0].text
		meta = sr.find_all("div", { "class" : 'pro-meta' })[0].text

		dataRow.write('A{}'.format(rowID), title)
		dataRow.write('B{}'.format(rowID), phone)
		dataRow.write('C{}'.format(rowID), meta)

	print "{} Page Complete...".format((i+1))


dataBook.close()


 