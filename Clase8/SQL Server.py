import pymssql

conn = pymssql.connect(
    server='localhost',
    user='Leandro',
    password='Leogl.098786',
    database='Mi Base de Datos'
)

cursor = conn.cursor()
cursor.execute('SELECT TOP 5 * FROM Clientes')
for row in cursor.fetchall():
    print(row)
conn.close()








