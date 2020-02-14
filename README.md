# Bicing Assignment
Project aim: Connection to Bicing (Barcelona bike share) live api and visualisation of available bikes

### Questions to answer:

###### Context:
The individual lives in a flat at "C/ SARDENYA, 290" and works at the address "AV. DE LA CATEDRAL, 10". They need to be at work at 9am and it takes 10 minutes to get there so they need to be sure that there will always be bikes at C/ SARDENYA, 292 station at 8.50am and that there will be empty slots at AV. DE LA CATEDRAL, 6 station.

##### 1. Could you please write a script or use a tool that would get the required information to confirm the bike and slot availibility? 

##### 2. Where should I move in Gracia based on Bicing availibility for me to be sure to have a bike every morning? 

### Method to answer these questions:
In this repository you will see two python scripts.

The first one is to create a MySQL database and table where to store the live bicing station information provided by the bicing API. AWS RDS was used to create the MySQL instance.

The second is a script to update the table with the live Bicing API station information. To auto-execute this script periodically a Cron Job was created inside an Amazon EC2 instance.

The script to create the Cron Job:

40 2 * * * python /home/ec2-user/Update_Table_Script.py

(As the EC2 instance is in Virgina (-6 hours from Barcelona), the time is set at 2:40am to execute the Cron Job).

All user, passwords and instance addresses have been replaced with '####'.

### Visualisation Solution:
A visualisation for this has been created via Tableau Public:
https://public.tableau.com/profile/laurence.williams#!/vizhome/Bicing_Dashboard/Dashboard1?publish=yes

The user can select between the filtert control: Gracia/Work. Hovering over the relvant stations allows the user to see how many bikes are available and how many are free at the desired stations.

Unfortunately whilst Tableau Desktop allows you to have a live connection to the MySQL database in AWS, Tableau Public does not, therefore the updates in the bike station availability done by the Cron Job in the EC2 server cannot be seen in the Tableau Public Dashboard.

### Further Comments:
For future development of this solution (especially with regards to question 2), the following considerations are worth noting:
- A historical log of the bike station availability can be collected in the MySQL database
- This can then feed into a model providing predictions on bike availability on X day of the week (and by month, etc.), which in turn could generate a recommendation system for the user (or any individual) on which location is best for them to move house.
- Finally, this solution can be scaled to different barrios of Barcelona by using BCN city shapefiles to identify the barrio in which each station resides in.
