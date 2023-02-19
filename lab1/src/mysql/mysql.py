import mysql.connector

# establish connection
cnx = mysql.connector.connect(
  host="localhost",
  user="username",
  password="password",
  database="db_planes"
)

# create cursor
cursor = cnx.cursor()

# create DB
cursor.execute("CREATE DATABASE IF NOT EXISTS db_planes")

# create table
table_name = "planes"
create_table_query = """
CREATE TABLE {} (
  id INT(11) NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  type_plane VARCHAR(255) NOT NULL,
  start_date DATE NOT NULL,
  operation_date DATE NOT NULL,
  PRIMARY KEY (id)
)
""".format(table_name)
cursor.execute(create_table_query)

# commit changes and close connection
cnx.commit()
cursor.close()
cnx.close()