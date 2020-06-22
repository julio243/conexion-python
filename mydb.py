import mysql.connector
cnx = mysql.connector.connect(user='root', password = 'julio243', database ='sakila')
cursor = cnx.cursor()
#insertar datos
a=input("inserte nombre: ")
b=input("inserte apellido: ")
sql = ("INSERT INTO actor (first_name,last_name) VALUES (%s,%s)")
data = (a,b)
cursor.execute(sql,data)
cnx.commit()
#mostrar datos
cursor.execute("SELECT * FROM actor")
for row in cursor.fetchall():
    print(row[0],'=',row[1],'-',row[3].strftime('%d/%m/%Y'))