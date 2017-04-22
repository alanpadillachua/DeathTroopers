import mysql.connector


print("Death Troopers")

config = {
    'user': 'root',
    'password': '214334dJ!',
    'host': '127.0.0.1',
    'database': 'grss',
    'raise_on_warnings': True,
}

connector = mysql.connector.connect(**config)

cursor = connector.cursor()

cursor.execute("SHOW COlUMNS FROM jedi_general")

for row in cursor.fetchall():
    print(row[0])

connector.close()
