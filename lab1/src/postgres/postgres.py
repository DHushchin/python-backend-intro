import psycopg2

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(database="db_planes", user="myuser", password="mypassword", host="localhost", port="5432")
print("Database connected successfully")

# Check if the database exists
cur.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'db_planes'")
exists = cur.fetchone()

# If the database doesn't exist, create it
if not exists:
    cur.execute("CREATE DATABASE db_planes")

# Create a table
def create_table():
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS planes
                   (id INT PRIMARY KEY NOT NULL,
                   name TEXT NOT NULL,
                   type_plane TEXT NOT NULL,
                   start_date DATE NOT NULL,
                   operation_date DATE NOT NULL);''')
    conn.commit()
    print("Table created successfully")
    cur.close()

# Insert data into the table
def insert_data(id, name, type_plane, start_date, operation_date):
    cur = conn.cursor()
    cur.execute("INSERT INTO planes (ID, NAME, TYPE_PLANE, START_DATE, OPERATION_DATE) VALUES (%s, %s, %s, %s, %s)", (id, name, type_plane, start_date, operation_date))
    conn.commit()
    print("Data inserted successfully")
    cur.close()

# Retrieve data from the table
def select_data():
    cur = conn.cursor()
    cur.execute("SELECT * FROM planes")
    rows = cur.fetchall()
    for row in rows:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("TYPE_PLANE = ", row[2])
        print("START_DATE = ", row[3],)
        print("OPERATION_DATE = ", row[4], "\n")
    cur.close()

# Update data in the table
def update_data(id, name, type_plane, start_date, operation_date):
    cur = conn.cursor()
    cur.execute("UPDATE planes SET NAME = %s, TYPE_PLANE = %s, START_DATE = %s, OPERATION_DATE = %s WHERE ID = %s", (name, type_plane, start_date, operation_date, id))
    conn.commit()
    print("Data updated successfully")
    cur.close()

# Delete data from the table
def delete_data(id):
    cur = conn.cursor()
    cur.execute("DELETE FROM planes WHERE ID = %s", (id,))
    conn.commit()
    print("Data deleted successfully")
    cur.close()

# Close the database connection
conn.close()
