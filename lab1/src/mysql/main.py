from mysql import connector

import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(os.path.dirname(current))
sys.path.append(parent)

from config import Config

cfg = Config()

# establish connection
cnx = connector.connect(
    host=cfg.MYSQL_HOST,
    user=cfg.MYSQL_USER,
    password=cfg.MYSQL_PASSWORD,
    database=cfg.MYSQL_DATABASE,
    port=cfg.MYSQL_PORT
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
