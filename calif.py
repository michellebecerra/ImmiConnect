#Author Michelle Becerra
#For ImmiConnect

from bs4 import BeautifulSoup
import requests
import csv
import sys

#Using GET request, searches the California Bar website for a specific attorney
def scrape_website(query, output):

	nameQuery = query;

	page = requests.get("http://members.calbar.ca.gov/fal/MemberSearch/QuickSearch?FreeText=" + nameQuery);

	soup = BeautifulSoup(page.content, 'html.parser')

	table = soup.find('table', attrs={'id':'tblAttorney'})

	table_body = table.find('tbody')

	rows = table_body.find_all('tr')

	write_to_csv(output, rows)

#Parses the results of all the attorneys with that name but only writes the active attorneys
#to the specified csv output name
def write_to_csv(output, data):	
	rows = data

	with open(output, 'w') as csvFile:
		fields =['Name', 'Status', 'Number', 'City', 'Admission Date', 'More Details']
		writer = csv.writer(csvFile)
		writer.writerows([fields])
		#Print to CSV
		for row in rows:
			colData = row.find_all('td')
			colData = [ele.text.strip() for ele in colData]
			#More info link to href
			more_details = "http://members.calbar.ca.gov/fal/Member/Detail/" + colData[2]
			colData.append(more_details)
			if "Active" in colData:
				writer.writerows([colData])

#Passes the query name and the output directory of csv files to methods above.
if __name__ == '__main__':
	query = sys.argv[1]
	outputDir = sys.argv[2]

	scrape_website(query,outputDir)
