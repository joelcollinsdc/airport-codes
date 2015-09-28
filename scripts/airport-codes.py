#!/usr/bin/env python

#remove id column, remove extraneous quotes, save to airports.csv

import requests
import csv

#r = requests.get('http://ourairports.com/data/airports.csv')

#with open('/tmp/airports.csv','wb') as f:
#  f.write(r.content
outfilepath = "../data/airport-codes.csv"
with open(outfilepath, 'w'): pass

with open('/tmp/airports.csv', 'rb') as infile:
  reader = csv.reader(infile)
  with open(outfilepath, 'w') as outfile:
    writer = csv.writer(outfile, csv.QUOTE_NONE)
    for row in reader:
      #leave off 0 (id), 11 (scheduled_service), 15.. (links)
      writer.writerow((row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],
        row[9], row[10], row[12], row[13], row[14]))