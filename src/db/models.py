from sqlalchemy.orm import mapped_column,Mapped,DeclarativeBase
from db.config import engine,session
from typing import Optional

class Base(DeclarativeBase):
    pass

class Autho(Base):
    
    __tablename__ = 'autho'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str]
    passw: Mapped[str]
    refresh_token: Mapped[Optional[str]] 
    
