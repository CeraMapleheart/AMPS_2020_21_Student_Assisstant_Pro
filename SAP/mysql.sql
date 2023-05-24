import mysql.connector

cnx = mysql.connector.connect(user='Roshni', password='123456780', host='localhost', database='student_assistant_pro')
cursor = cnx.cursor()

def create_table():
    table_name = "notes"
    query = "CREATE TABLE IF NOT EXISTS {} (id INT AUTO_INCREMENT PRIMARY KEY, note_content TEXT)".format(table_name)
    cursor.execute(query)
    cnx.commit()
    print("Table created: {}".format(table_name))

def insert_data(note):
    table_name = "notes"
    query = "INSERT INTO {} (note_content) VALUES (%s)".format(table_name)
    values = (note,)
    cursor.execute(query, values)
    cnx.commit()
    print("Data inserted: {}".format(note))

def retrieve_data():
    table_name = "notes"
    query = "SELECT * FROM {}".format(table_name)
    cursor.execute(query)
    notes = cursor.fetchall()
    print("Notes:")
    for note in notes:
        print("- ", note[1])

def close_connection():
    cursor.close()
    cnx.close()
    print("Connection closed")

create_table()
insert_data("Social Science")
insert_data("Physical Education")
retrieve_data()
close_connection()
