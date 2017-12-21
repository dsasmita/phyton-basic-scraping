import json
import datetime
from kompas.view import scrapKompas


print("Result 1")
print(datetime.datetime.now())
data = scrapKompas("http://indeks.kompas.com/news/2017-12-20/")
print(json.dumps(data))
print(datetime.datetime.now())