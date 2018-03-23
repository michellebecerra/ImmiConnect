from bs4 import BeautifulSoup
import requests

page = requests.get("http://members.calbar.ca.gov/fal/MemberSearch/QuickSearch?FreeText=Charles+Brown&SoundsLike=false")
#http://members.calbar.ca.gov/fal/MemberSearch/QuickSearch?FreeText=Charles+Brown&SoundsLike=false
soup = BeautifulSoup(page.content, 'html.parser')
print soup.prettify()