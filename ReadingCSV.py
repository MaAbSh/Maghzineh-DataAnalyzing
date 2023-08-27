import csv
import Clouds
import Highway

CloudsLog = 0
HighwayLog = 0

with open('results.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        tempStr1 = row[9] # as the details data
        try:
            tempLevel = int(row[3]) # as the trail level
        except:
            tempLevel = 0

        if (row[1]=='ابرهای بارانی' and CloudsLog == 1):
            Clouds.CloudsDecoding.Decoding(tempStr1)

        if (row[1] == 'بزرگراه' and HighwayLog == 1):
            Highway.HighwayDecoding.Decoding(tempStr1,tempLevel)

