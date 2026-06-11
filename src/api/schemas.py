from pydantic import BaseModel

class AuthPy(BaseModel):
    
    login: str
    passw: str
    
class AuthFull(AuthPy):
    
    id: int
    token: str