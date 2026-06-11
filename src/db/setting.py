import os
from dotenv import load_dotenv

load_dotenv()

class Setting:
     
    DB_HOST = os.getenv('DB_HOST')
    DB_NAME = os.getenv('DB_NAME')
    DB_PASS = os.getenv('DB_PASS')
    DB_USER = os.getenv('DB_USER')
    DB_PORT = os.getenv('DB_PORT')
    
    MODE = os.getenv('MODE')
    
    def connect(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
setting = Setting()