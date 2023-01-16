import json

with open(r'C:\Users\lasko\Desktop\scrapy\trainscraper\trains.json') as f:
   data = json.load(f)

print(data[0])