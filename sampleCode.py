import _mysql_connector
print("hello world")
cnx = _mysql_connector.connect(user='root', database ='grrs')
cursor = cnx.cursor()
