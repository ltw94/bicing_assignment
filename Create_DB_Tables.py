#!/usr/bin/env python
# coding: utf-8

# Import relevant Libraries:

# In[2]:


import mysql.connector
import json
import requests


# In[3]:


host = '####.us-east-1.rds.amazonaws.com'
user = '####'
password = '####'


# In[59]:


con = mysql.connector.connect(host = host, user=user, password = password, charset = 'utf8')
cursor = con.cursor()


# Create Database and Tables:

# In[52]:


cursor.execute("CREATE DATABASE assignment_database;")


# In[60]:


cursor.execute("USE assignment_database;")


# In[54]:


cursor.execute("""CREATE TABLE station_data (stationID VARCHAR(200) PRIMARY KEY, 
empty_slots INT, free_bikes INT, ebikes INT, online BOOLEAN, lat_coord FLOAT(8,6), 
long_coord FLOAT(7,6), name VARCHAR(100), timestamp TIMESTAMP);""")


# In[63]:


response = requests.get('http://api.citybik.es/v2/networks/bicing')
data = response.json()

relevant_stations = ["C/ SARDENYA, 292", "AV. DE LA CATEDRAL, 6", "C/ DE NIL FABRA, 16-20", "C/ DE LA SANTACREU, 2 (PL.DE LA VIRREINA)",
                    "PL. DEL NORD, 5", "C/ DEL TORRENT DE LES FLORS, 102", "C/ MONTMANY, 1",
                    "C/ DE BONAVISTA, 14", "C/ DEL CANÓ, 1", "GRAN DE GRÀCIA, 155 (METRO FONTANA)",
                    "PL  JOANIC - C / BRUNIQUER, 59"]

station_list = []
for station in data['network']['stations']:
    if station['name'] in relevant_stations:
        station_list.append(station)


# In[64]:


for station in station_list:
    con = mysql.connector.connect(host = host, user=user, password = password, charset = 'utf8')
    cursor = con.cursor()
    cursor.execute("USE assignment_database;")
    cursor.execute("INSERT INTO station_data(stationID, empty_slots, free_bikes, ebikes, online, lat_coord, long_coord, name, timestamp) VALUES (%s,%s,%s, %s, %s, %s, %s, %s, %s)", (station['id'], station['empty_slots'], station['free_bikes'], station['extra']['ebikes'], station['extra']['online'], station['latitude'], station['longitude'], station['name'], station['timestamp'][:10]+ " " + station['timestamp'][11:19]))
    con.commit()
    cursor.close()   


# In[4]:


con = mysql.connector.connect(host = host, user=user, password = password, charset = 'utf8')
cursor = con.cursor()
cursor.execute("USE assignment_database;")

cursor.execute("SELECT * FROM station_data;")
result = cursor.fetchall()

for i in range(len(result)):
    print(result[i])

