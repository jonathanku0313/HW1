import csv

cwb_filename = '107000129.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)

station = [ 'C0A880', 'C0F9A0', 'C0G640', 'C0R190', 'C0X260']
temp = []
station_max = []
target_data = []

data = list(filter(lambda item: item['station_id'] in station, data))

for id in station:
    temp = list(filter(lambda item: item['station_id'] == id, data))
    temp = list(sorted(temp, key = lambda item: item['TEMP'], reverse = True))
    station_max.append(temp[0])

for t in station_max:
   if t['TEMP'] == '-99.000' or ['TEMP'] == '-999.000':
      target_data.append([t['station_id'], 'None'])
   else:
      target_data.append([t['station_id'], float(t['TEMP'])])

print(target_data)
