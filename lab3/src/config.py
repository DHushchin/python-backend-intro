import dotenv
import os

# Load environment variables from .env file

dotenv.load_dotenv()

# Define a configuration class
class Config:
    def __init__(self):
        self.postgres_config()
        
    # Define PostgreSQL configurations
    def postgres_config(self):
        self.MONGO_URI = os.environ.get('MONGO_URI')
        self.MONGO_DATABASE = os.environ.get('MONGO_DATABASE')
        