import dotenv
import os

# Load environment variables from .env file

dotenv.load_dotenv()

# Define a configuration class
class Config:
    def __init__(self):
        self.mysql_config()
        self.postgres_config()
        self.sqlite_config()
    
    # Define MySQL configurations
    def mysql_config(self):
        self.MYSQL_HOST = os.environ.get('MYSQL_HOST')
        self.MYSQL_USER = os.environ.get('MYSQL_USER')
        self.MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
        self.MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE')
        self.MYSQL_PORT = os.environ.get('MYSQL_PORT')
        
    # Define PostgreSQL configurations
    def postgres_config(self):
        self.POSTGRES_HOST = os.environ.get('POSTGRES_HOST')
        self.POSTGRES_USER = os.environ.get('POSTGRES_USER')
        self.POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
        self.POSTGRES_DATABASE = os.environ.get('POSTGRES_DATABASE')
        self.POSTGRES_PORT = os.environ.get('POSTGRES_PORT')
        
    # Define SQLite configurations
    def sqlite_config(self):
        self.SQLITE_DATABASE = os.environ.get('SQLITE_DATABASE')