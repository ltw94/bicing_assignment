#!/usr/bin/env python
# coding: utf-8

# In[22]:


import mysql.connector
import requests

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
        
host = '####.us-east-1.rds.amazonaws.com'
user = '####'
password = '####'
        
for station in station_list:
    con = mysql.connector.connect(host = host, user=user, password = password, charset = 'utf8')
    cursor = con.cursor()
    try:
        #time_stamp = station['timestamp'][11:19]
        cursor.execute("USE assignment_database;")
        cursor.execute("UPDATE station_data SET empty_slots = {}, free_bikes = {}, ebikes = {}, online = {}, timestamp = {} WHERE stationID = {};".format(station['empty_slots'], station['free_bikes'], station['extra']['ebikes'], station['extra']['online'], "'"+station['timestamp'][:10]+ " " + station['timestamp'][11:19]+"'", "'"+station['id']+"'"))
        file_name = "success_log.txt"
        output = open(file_name, "w")
        output.write("Done")
        con.commit()
        cursor.close()
    
    except Exception as e:
        file_name = "fail_log.txt"
        output = open(file_name, "w")
        output.write(str(e))
        con.commit()
        cursor.close()

