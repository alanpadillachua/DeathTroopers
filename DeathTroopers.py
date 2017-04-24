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


def insert(query, data):
    try:
        cursor.execute(query, data)
        connector.commit()
    except:
        connector.rollback()


def insert_station():
    add_station = ('INSERT INTO Republic_Station'
                   '(STATION_ID, x_axis, y_axis, z_axis)'
                   'VALUES (%s,%s,%s,%s)')
    data_station = ('1', '10023.2', '29001.9', '120.21')
    insert(add_station, data_station)


def insert_rooms():
    num = 1
    add_rooms = ('INSERT INTO rooms'
                 '(STATION_ID,Room_Number)'
                 'VALUES (%s,%s)')
    while num <= 50:
        # print(num)
        data_rooms = ('1', '%d' % num)
        insert(add_rooms, data_rooms)
        num += 1


def insert_training_room():
    num = 1
    add_training_room = ('INSERT INTO training_room'
                         '(statid,RmNumber,Capacity,Available)'
                         'VALUES (%s,%s,%s,%s)')

    while num <= 25:
        data_training_room = ('1', '%d' % num, '25', '1')
        insert(add_training_room, data_training_room)
        num += 1


def insert_briefing_room():
    num = 26
    add_briefing_room = ('INSERT INTO briefing_room'
                         '(STATION_ID,Room_Number,Capacity,Availability)'
                         'VALUES (%s,%s,%s,%s)')
    while num <= 50:
        data_briefing_room = ('1', '%d' % num, '25', '1')
        insert(add_briefing_room,data_briefing_room)
        num += 1


def insert_landing_station():
    add_landing_station = ('INSERT INTO landing_station'
                           '(Lstation_ID,GRRS_ID,Amount_of_FDocks,Amount_of_Docks,Amount_of_IUDocks)'
                           'VALUES (%s,%s,%s,%s,%s)')
    data_landing_station = ('1313', '1', '20', '40', '20')
    insert(add_landing_station,data_landing_station)


def insert_landing_dock():
    num = 1
    add_landing_dock = ('INSERT INTO landing_dock'
                        '(LStation_ID,Dock_Number,isAvailable,Rental_Price)'
                        'VALUES (%s,%s,%s,%s)')
    while num <= 40:
        data_landing_dock = ('1313', '%d' % num, '1', '23')
        insert(add_landing_dock, data_landing_dock)
        num += 1
# insert_station()
# insert_rooms()
# insert_training_room()
# insert_briefing_room()
# insert_landing_station()
insert_landing_dock()

cursor.execute("SELECT * FROM landing_dock")
for row in cursor.fetchall():
    print(row)

connector.close()
