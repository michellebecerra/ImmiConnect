from bs4 import BeautifulSoup
import requests
import pandas as pd

##Navigating html page object by object
#page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
#Prints HTML content of the url above
#print page.content
#soup = BeautifulSoup(page.content, 'html.parser')
#print soup.prettify()
#print [type(item) for item in list(soup.children)]
# html = list(soup.children)[2]

# body = list(html.children)[3]

# p = list(body.children)[1]

#Get contents 
#print p.get_text()

####Finding all instances of a tag at once

#print soup.find_all('p')[0].get_text()

####Searching for tags by class and id
# page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
# soup = BeautifulSoup(page.content, 'html.parser')
# #print soup.find_all('p', class_='outer-text')
# print soup.find_all(id="first")[0].get_text()

####Scraping weather data
page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
#print(tonight.prettify())

period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()

img = tonight.find("img")
desc = img['title']

# Description Period Short_Desc Temp
period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
sc_tags = seven_day.select(".tombstone-container .short-desc")
short_descs = [scs.get_text() for scs in sc_tags]
temp_tags = seven_day.select(".tombstone-container .temp")
temps = [tp.get_text() for tp in temp_tags]
descs = [d['title'] for d in seven_day.select(".tombstone-container img")]


# print(short_descs)
# print(temps)
# print(descs)

#### Pandas DataFrame to analyze it

weather = pd.DataFrame({
	"Period": periods,
	"Temperature": temps,
	})
print(weather)


