import mysql.connector

mydb = mysql.connector.connect(host="10.109.254.41", user="app", passwd="sau03magen", database="LmiPP")

mycursor = mydb.cursor()

mycursor.execute("select * from MainSettings")

for i in mycursor:
    print(i)

        