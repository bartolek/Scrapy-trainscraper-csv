import json

with open(r'C:\Users\lasko\Desktop\scrapy\trainscraper\trains.json') as f:
   data = json.load(f)

for i in range (0,len(data)):
   if len(data[i]["Number"].split()) > 1:
      print(data[i]["Number"].split()[1])
   else:
      print(data[i]["Number"])