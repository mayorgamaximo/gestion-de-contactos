import mysql.connector
ae="safgasfgags"
conexion1=mysql.connector.connect(host="localhost", user="root", passwd="", database="contactos")
cursor1=conexion1.cursor()
sql="insert into contacto(nombre, telefono, correo) values (%s,%s,%s)"
datos=(ae, "3431364868", "yamil@gmail.com")
cursor1.execute(sql, datos)
conexion1.commit()
conexion1.close()  