import requests
import pprint

pp = pprint.PrettyPrinter(indent=2)

item = ""
APP_ID = "PatrickS-ewalk-PRD-6cd49746d-31c9e839"
url = "http://svcs.ebay.com/services/search/FindingService/v1?\
OPERATION-NAME=findCompletedItems&\
SERVICE-VERSION=1.7.0&\
SECURITY-APPNAME={}&\
RESPONSE-DATA-FORMAT=JSON&\
REST-PAYLOAD&\
keywords=Ritter+evening+dress&\
categoryId=156955&\
itemFilter(0).name=Condition&\
itemFilter(0).value=3000&\
itemFilter(1).name=FreeShippingOnly&\
itemFilter(1).value=false&\
itemFilter(2).name=SoldItemsOnly&\
itemFilter(2).value=true&\
sortOrder=PricePlusShippingLowest&\
paginationInput.entriesPerPage=2".format(APP_ID)
r = requests.get(url)
pp.pprint(r.json())
