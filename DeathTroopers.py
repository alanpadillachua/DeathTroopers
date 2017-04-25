import mysql.connector
import random

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


def do_query(query, data):
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
    do_query(add_station, data_station)


def insert_rooms():
    num = 1
    add_rooms = ('INSERT INTO rooms'
                 '(STATION_ID,Room_Number)'
                 'VALUES (%s,%s)')
    while num <= 50:
        # print(num)
        data_rooms = ('1', '%d' % num)
        do_query(add_rooms, data_rooms)
        num += 1


def insert_training_room():
    num = 1
    add_training_room = ('INSERT INTO training_room'
                         '(statid,RmNumber,Capacity,Available)'
                         'VALUES (%s,%s,%s,%s)')

    while num <= 25:
        data_training_room = ('1', '%d' % num, '25', '1')
        do_query(add_training_room, data_training_room)
        num += 1


def insert_briefing_room():
    num = 26
    add_briefing_room = ('INSERT INTO briefing_room'
                         '(STATION_ID,Room_Number,Capacity,Availability)'
                         'VALUES (%s,%s,%s,%s)')
    while num <= 50:
        data_briefing_room = ('1', '%d' % num, '25', '1')
        do_query(add_briefing_room, data_briefing_room)
        num += 1


def insert_landing_station():
    add_landing_station = ('INSERT INTO landing_station'
                           '(Lstation_ID,GRRS_ID,Amount_of_FDocks,Amount_of_Docks,Amount_of_IUDocks)'
                           'VALUES (%s,%s,%s,%s,%s)')
    data_landing_station = ('1313', '1', '20', '40', '20')
    do_query(add_landing_station, data_landing_station)


def insert_landing_dock():
    num = 1
    add_landing_dock = ('INSERT INTO landing_dock'
                        '(LStation_ID,Dock_Number,isAvailable,Rental_Price)'
                        'VALUES (%s,%s,%s,%s)')
    while num <= 40:
        data_landing_dock = ('1313', '%d' % num, '1', '23')
        do_query(add_landing_dock, data_landing_dock)
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
        do_query(add_mission, data_mission)


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
        do_query(add_jedi, data_jedi)


def insert_spaceship():
    add_spaceship = ('INSERT INTO spaceship'
                     '(JCall_Sign,SS_ID)'
                     'VALUES (%s,%s)')
    get_jedi_call_signs = 'SELECT jcall_sign FROM jedi_general'
    cursor.execute(get_jedi_call_signs)
    call_sign_list = list(cursor.fetchall())
    num = 1770
    for line in call_sign_list:
        data_spaceship = ('%s' % line[0],
                          '%d' % num)
        do_query(add_spaceship, data_spaceship)
        num += 1


def pop_must_dock():
    get_ss_id = 'SELECT SS_ID FROM spaceship'
    cursor.execute(get_ss_id)
    ssid_list = list(cursor.fetchall())

    ssid_length = len(ssid_list)
    get_empty_docks = 'SELECT Dock_Number FROM landing_dock WHERE isAvailable = 1 LIMIT ' + str(ssid_length)
    cursor.execute(get_empty_docks)
    dock_number_list = list(cursor.fetchall())
    add_must_dock = ('INSERT INTO must_dock'
                     '(SS_ID, Dock_Number) VALUES (%s, %s)')
    for i in range(0, ssid_length):
        data_must_dock = ('%s' % ssid_list[i],
                          '%s' % dock_number_list[i])
        # print(data_must_dock)
        do_query(add_must_dock, data_must_dock)

    # update landing_dock isAvailable to 0
    get_dock_num = 'SELECT Dock_Number FROM must_dock'
    cursor.execute(get_dock_num)
    dock_list = list(cursor.fetchall())
    length = len(dock_list)
    for i in range(0, length):
        update_landing_dock = 'UPDATE landing_dock SET isAvailable = 0 WHERE Dock_Number = ' + '%s' % dock_list[i]
        cursor.execute(update_landing_dock)
        connector.commit()  # commit changes


def pop_must_pay_fee():
    get_jedi_call_signs = 'SELECT jcall_sign FROM spaceship'
    cursor.execute(get_jedi_call_signs)
    call_sign_list = list(cursor.fetchall())

    get_station_id = 'SELECT LStation_ID FROM landing_dock WHERE isAvailable = 0 '
    cursor.execute(get_station_id)
    station_id_list = list(cursor.fetchall())

    get_price = 'SELECT Rental_price from landing_dock WHERE isAvailable = 0'
    cursor.execute(get_price)
    price_list = list(cursor.fetchall())

    add_must_pay_fee = ('INSERT INTO must_pay_fee'
                        '(JGCS_ID, LSID, Fee_Amt)'
                        ' VALUES (%s,%s,%s)')
    for i in range(0, len(call_sign_list)):
        must_pay_data = ('%s' % call_sign_list[i],
                         '%s' % station_id_list[i],
                         '%s' % price_list[i])
        do_query(add_must_pay_fee, must_pay_data)


def insert_mission_package():
    get_mission_id = 'SELECT MID_number FROM mission'
    cursor.execute(get_mission_id)
    mission_id_list = list(cursor.fetchall())

    add_mission_package = ('INSERT INTO mission_package'
                           '(M_id, MP_id, Fuel_Amount, Max_Credits) '
                           'VALUES (%s,%s,%s,%s)')
    mp_id = 1
    for item in mission_id_list:
        package_data = ('%s' % item[0],
                        '%s' % str(mp_id),
                        '5000', '7000')
        do_query(add_mission_package, package_data)
        mp_id += 1


def insert_co_pilot():
    get_mp_id = 'SELECT MP_id FROM mission_package'
    cursor.execute(get_mp_id)
    mpid_list = list(cursor.fetchall())

    pilot_file = 'PilotSpecialty.txt'
    with open(pilot_file) as file:
        pilot_specialty_list = file.readlines()
        pilot_clean_list = [x.strip() for x in pilot_specialty_list]

    add_co_pilot = ('INSERT INTO co_pilot'
                    '(Co_ID, MP_ID, PSpecialty, PDate_TIme_Availble) '
                    'VALUES (%s,%s,%s,%s)')
    co_id = 1
    for i in range(0, 20):
        data_pilot = ('%s' % str(co_id + i),
                      '%s' % mpid_list[i],
                      '%s' % pilot_clean_list[i],
                      '%s' % '2223-04-24 12:12:00')
        do_query(add_co_pilot,data_pilot)


def insert_droid():
    get_mp_id = 'SELECT MP_id FROM mission_package'
    cursor.execute(get_mp_id)
    mpid_list = list(cursor.fetchall())

    droid_name_file = 'DroidNames.txt'
    droid_roles_file = 'DroidRoles.txt'
    droid_specialty = 'DroidSpecialty.txt'

    with open(droid_name_file) as file:
        droid_name_list = file.readlines()
        droid_name_clean_list = [x.strip() for x in droid_name_list]
    with open(droid_roles_file) as file:
        droid_roles_list = file.readlines()
        droid_roles_clean_list = [x.strip() for x in droid_roles_list]
    with open(droid_specialty) as file:
        droid_specialty_list = file.readlines()
        droid_specialty_clean_list = [x.strip() for x in droid_specialty_list]
    add_droid = ('INSERT INTO droid'
                 '(Dname, MP_id, Dtype, DHP, DSpecialty, DDate_Time_Available)'
                 'VALUES (%s,%s,%s,%s,%s,%s)')
    for i in range(0, len(droid_name_list)):
        data_droid = ('%s' % droid_name_clean_list[i],
                      '%s' % mpid_list[i],
                      '%s' % droid_roles_clean_list[i],
                      '%s' % str(random.randrange(75, 100, 5)),
                      '%s' % droid_specialty_clean_list[i],
                      '2223-04-24 12:12:00')
        do_query(add_droid, data_droid)


def insert_clonetroopers():
    get_mp_id = 'SELECT MP_id FROM mission_package'
    cursor.execute(get_mp_id)
    mpid_list = list(cursor.fetchall())

    clone_callsigns_file = 'CloneCallsigns.txt'
    clone_names_file = 'CloneNames.txt'
    clone_role_file = 'CloneRoles.txt'

    with open(clone_callsigns_file) as file:
        callsign_list = file.readlines()
        callsign_clean_list = [x.strip() for x in callsign_list]
    with open(clone_names_file) as file:
        names_list = file.readlines()
        names_clean_list = [x.strip() for x in names_list]
    with open(clone_role_file) as file:
        role_list = file.readlines()
        role_clean_list = [x.strip() for x in role_list]
    add_clonetroop = ('INSERT INTO clonetrooper_unit'
                      '(CCall_Sign, MP_id, CName, CSpecialty, CDate_Time_Available)'
                      'VALUES (%s,%s,%s,%s,%s)')
    for i in range(0, len(callsign_list)):
        data_clonetroop = ('%s' % callsign_clean_list[i],
                           '%s' % mpid_list[i],
                           '%s' % names_clean_list[i],
                           '%s' % role_clean_list[i],
                           '2223-04-24 12:12:00')
        do_query(add_clonetroop, data_clonetroop)


def pop_must_brief():
    get_callsign_jedi = 'SELECT JCall_Sign FROM jedi_general'
    cursor.execute(get_callsign_jedi)
    jedi_callsign_list = list(cursor.fetchall())

    get_missionid_jedi = 'SELECT M_id FROM jedi_general'
    cursor.execute(get_missionid_jedi)
    jedi_mid_list = list(cursor.fetchall())

    mpid_list = []
    for i in range(0, len(jedi_mid_list)):
        get_mpid = 'SELECT MP_id FROM mission_package WHERE M_id = ' + '%s' % jedi_mid_list[i]
        cursor.execute(get_mpid)
        mpid_list.extend(cursor.fetchone())
    copilot_list = []
    droid_list = []
    clonetrooper_list = []
    for i in range(0, len(mpid_list)):
        get_copilot = 'SELECT Co_ID FROM co_pilot WHERE MP_ID = ' + '%s' % mpid_list[i]
        cursor.execute(get_copilot)
        copilot_list.extend(cursor.fetchone())
        get_droid = 'SELECT Dname FROM droid WHERE MP_id = ' + '%s' % mpid_list[i]
        cursor.execute(get_droid)
        droid_list.extend(cursor.fetchone())
        get_clonetrooper = 'SELECT CCall_Sign FROM clonetrooper_unit WHERE MP_id = ' + '%s' % mpid_list[i]
        cursor.execute(get_clonetrooper)
        clonetrooper_list.extend(cursor.fetchone())
    get_empty_breif_room = 'SELECT Room_Number FROM briefing_room WHERE Availability = 1 LIMIT ' + '%s' % str(len(mpid_list))
    cursor.execute(get_empty_breif_room)
    briefing_room_list = list(cursor.fetchall())

    add_must_brief = ('INSERT INTO must_brief'
                      '(JCall_Sign, DName, Co_ID, CCall_Sign, Room_Number)'
                      'VALUES (%s,%s,%s,%s,%s)')
    for i in range(0, len(mpid_list)):
        data_must_brief = ('%s' % jedi_callsign_list[i],
                           '%s' % droid_list[i],
                           '%s' % copilot_list[i],
                           '%s' % clonetrooper_list[i],
                           '%s' % briefing_room_list[i])
        do_query(add_must_brief, data_must_brief)

    for i in range(0, len(briefing_room_list)):
        update_room = 'UPDATE Briefing_Room SET Availability = 0 WHERE Room_Number = ' + '%s' % briefing_room_list[i]
        cursor.execute(update_room)
        connector.commit()

def pop_must_train():
    get_callsign_jedi = 'SELECT JCall_Sign FROM jedi_general'
    cursor.execute(get_callsign_jedi)
    jedi_callsign_list = list(cursor.fetchall())

    get_missionid_jedi = 'SELECT M_id FROM jedi_general'
    cursor.execute(get_missionid_jedi)
    jedi_mid_list = list(cursor.fetchall())

    mpid_list = []
    for i in range(0, len(jedi_mid_list)):
        get_mpid = 'SELECT MP_id FROM mission_package WHERE M_id = ' + '%s' % jedi_mid_list[i]
        cursor.execute(get_mpid)
        mpid_list.extend(cursor.fetchone())
    copilot_list = []
    clonetrooper_list = []
    for i in range(0, len(mpid_list)):
        get_copilot = 'SELECT Co_ID FROM co_pilot WHERE MP_ID = ' + '%s' % mpid_list[i]
        cursor.execute(get_copilot)
        copilot_list.extend(cursor.fetchone())
        get_clonetrooper = 'SELECT CCall_Sign FROM clonetrooper_unit WHERE MP_id = ' + '%s' % mpid_list[i]
        cursor.execute(get_clonetrooper)
        clonetrooper_list.extend(cursor.fetchone())
    get_empty_training_room = 'SELECT RmNumber FROM training_room WHERE Available = 1 LIMIT ' + '%s' % str(
        len(mpid_list))
    cursor.execute(get_empty_training_room)
    training_room_list = list(cursor.fetchall())

    add_must_train = ('INSERT INTO must_train'
                      '(JCall_Sign, Co_ID, CCall_Sign, Room_Number)'
                      'VALUES (%s,%s,%s,%s)')
    for i in range(0, len(mpid_list)):
        data_must_train = ('%s' % jedi_callsign_list[i],
                           '%s' % copilot_list[i],
                           '%s' % clonetrooper_list[i],
                           '%s' % training_room_list[i])
        do_query(add_must_train, data_must_train)

    for i in range(0, len(training_room_list)):
        update_room = 'UPDATE training_room SET Available = 0 WHERE RmNumber = ' + '%s' % training_room_list[i]
        cursor.execute(update_room)
        connector.commit()

insert_station()
insert_rooms()
insert_training_room()
insert_briefing_room()
insert_landing_station()
insert_landing_dock()
insert_mission()
insert_jedi()
insert_spaceship()
pop_must_dock()
pop_must_pay_fee()
insert_mission_package()
insert_co_pilot()
insert_droid()
insert_clonetroopers()
pop_must_brief()
pop_must_train()

# cursor.execute("SELECT * FROM training_room")
# for row in cursor.fetchall():
#     print(row)


connector.close()
