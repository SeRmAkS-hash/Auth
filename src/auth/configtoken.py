from authx import AuthX,AuthXConfig,RequestToken
from dotenv import load_dotenv
import os

load_dotenv()

class ConfigAutho:
    
    CONFIG = AuthXConfig()
    CONFIG.JWT_TOKEN_LOCATION = ['headers']
    CONFIG.JWT_SECRET_KEY = os.getenv('JWT_SECRET')
    CONFIG.JWT_ACCESS_COOKIE_NAME = 'access_token_cookie'
    CONFIG.JWT_REFRESH_COOKIE_NAME = 'refresh_token_cookie'
    TOKEN = AuthX(CONFIG)
    
class AuthoX(ConfigAutho):
    
    ACCESS: str
    REFRESH: str
    
    def create_access(self,name: str):
        self.ACCESS = self.TOKEN.create_access_token(uid=name)
    
    def create_refresh(self,name: str):
        self.REFRESH = self.TOKEN.create_refresh_token(uid=name)
        
auth = AuthoX()
        
    