# ImmiConnect
Script to scrape the search information off the California Bar website. 
Used to verify if an attorney is an active attorney or not. Search by first and last name


## Dependencies
- Install Python 2.7
- Intall BeautifulSoup 4
## Running Script
The script takes in a query name and the output name you would like to name the csv.

To run just go to the directory of the calif.py script
and specify the name you would like to search and the name of the directory of filename (if same directory) of the csv:

>> python calif.py "William Smith" search_results2.csv

Here we are searching for William Smith and the results would be stored in search_results2.csv which can be opened with microsoft excel.
The csv file containes the Name of the attorney, the status of the attorney (active), the bar number, city and admission date. To get more
information on this person the last column "more information" is the url to their profile on the California Bar website. 

Example csv when looking up William Smith:

![csv picture](https://raw.githubusercontent.com/michellebecerra/ImmiConnect/master/search_results2.csv)


