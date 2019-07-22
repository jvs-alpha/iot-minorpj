import sqlite3

database = sqlite3.connect("data.db")
cursor = database.cursor()
command = '''
CREATE TABLE DATA( ID INT NOT NULL PRIMARY KEY,
NAME VARCHAR(20) NOT NULL,
UPLOAD_DATE DATE);
'''
cursor.execute(command)
database.commit()
database.close()
