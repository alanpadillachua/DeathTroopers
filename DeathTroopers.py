import mysql.connector
import random


# print("Death Troopers")

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


def insert_mission():
    mission_type_file = "MissionTypes.txt"
    mission_goal_file = "Missions.txt"
    with open(mission_type_file) as f:
        mission_type_list = f.readlines()  # read the lines into list
        mission_type_clean_list = [x.strip() for x in mission_type_list]  # remove new line character at the end of each line
    with open(mission_goal_file) as f:
        mission_goal_list = f.readlines()
        mission_goal_clean_list = [x.strip() for x in mission_goal_list]  # remove new line character at the end of each line
    # for line in mission_type_clean_list:  # for each line in the list
    #     print(line)  # print the line
    add_mission = ('INSERT INTO mission'
                   '(MID_number, Goal,briefingTime_Length,trainingTime_Length,Mission_Type,JAmount_of_Credits)'
                   'VALUES (%s, %s, %s, %s, %s, %s)')
    mission_num = 1
    for i in range(0, 40):
        # print('index ' + str(i) + ' ' + mission_type_clean_list[i] + ' | ' + mission_goal_clean_list[i])
        data_mission = ('%s' % str(mission_num + i), '%s' % mission_goal_clean_list[i],
                        '20', '20', '%s' % mission_type_clean_list[i], '1000')
        insert(add_mission, data_mission)


def insert_jedi():
    jedi_call_signs_file = 'JediCallsigns.txt'
    jedi_names_file = 'JediNames.txt'
    jedi_light_saber_colors_file = 'JediLSColors.txt'

    with open(jedi_call_signs_file) as file:
        jedi_call_signs_list = file.readlines()
        jedi_call_signs_clean_list = [x.strip() for x in jedi_call_signs_list]
    with open(jedi_names_file) as file:
        jedi_names_list = file.readlines()
        jedi_names_clean_list = [x.strip() for x in jedi_names_list]
    with open(jedi_light_saber_colors_file) as file:
        jedi_light_saber_list = file.readlines()
        jedi_light_saber_clean_list = [x.strip() for x in jedi_light_saber_list]

    add_jedi = ('INSERT INTO jedi_general'
                '(JCall_Sign,JName,JLS_Color,Lstation_ID,M_id,JAmount_of_Credits,JDate_Time_Available)'
                'VALUES (%s,%s,%s,%s,%s,%s,%s)')

    mission_num = 1
    for i in range(0, 20):
        data_jedi = ('%s' % jedi_call_signs_clean_list[i],
                     '%s' % jedi_names_clean_list[i],
                     '%s' % jedi_light_saber_clean_list[i],
                     '1313',
                     '%s' % str(mission_num + i),  # assign it mission in order
                     '%s' % str(random.randrange(100, 5000)),  # random credit amount
                     '2223-04-24 12:12:00')
        insert(add_jedi, data_jedi)




# insert_station()
# insert_rooms()
# insert_training_room()
# insert_briefing_room()
# insert_landing_station()
# insert_landing_dock()
# insert_mission()
# insert_jedi()

cursor.execute("SELECT * FROM jedi_general")
for row in cursor.fetchall():
    print(row)

connector.close()
