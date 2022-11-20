import columns as columns
from django.shortcuts import render
import psycopg2
import sys
import os
import time
import datetime

# connect to the database
conn = psycopg2.connect("dbname='worldofsharepointdb' user='postgres' host='localhost' password='simonkoo'")
cur = conn.cursor()

# execute select query to get the data from the database table
cur.execute("select * from clanokHome")

# get the data from the database table
rows = cur.fetchall()

# convert data to dictionary format
columns = [desc[0] for desc in cur.description]
results = []
for row in rows:
    results.append(dict(zip(columns, row)))

print(results)
# convert list of dictionaries
# to list of lists

# close the communication with the PostgreSQL
cur.close()

def homePageView(request):
    # HTML je uložené v HomePage/templates/HomePage/HomePage.html
    return render(request, 'HomePage/HomePage.html', {'results': results})


# close the connection
conn.close()