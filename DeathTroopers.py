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


add_station = ('INSERT INTO Republic_Station'
               '(STATION_ID, x_axis, y_axis, z_axis)'
               'VALUES (%s ,%s, %s, %s)')
data_station = ('000001', '123.2', '291.9', '12.21')


def insert(query, data):
    try:
        cursor.execute(query, data)
        connector.commit()
    except:
        connector.rollback()

insert(add_station, data_station)

cursor.execute("SELECT * FROM Republic_Station")
for row in cursor.fetchall():
    print(row)

connector.close()
