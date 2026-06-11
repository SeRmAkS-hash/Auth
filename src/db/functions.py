from db.models import Autho,Base
from db.config import engine,session
from sqlalchemy import select
import hashlib

class Setup:
    
    @staticmethod
    async def setup_db():
        async with engine.begin() as connect:
            await connect.run_sync(Base.metadata.drop_all)
            await connect.run_sync(Base.metadata.create_all)
            
class FuncAutho:

    @staticmethod 
    async def check_login(login: str) -> bool:
        async with session.begin() as connect:
            query = (
                select(Autho)
                .filter(Autho.login == login)
            )
            result = await connect.execute(query)
            try:
                result = result.unique().scalars().one()
                if result.login == login:
                    return False
            except:
                return True
        
    @staticmethod 
    async def input_autho(login: str, passw: str) -> str:
        if await FuncAutho.check_login(login):
            autho = Autho(login=login
                        ,passw=hashlib.sha256(passw.encode('utf-8')).hexdigest())
            async with session.begin() as connect:
                connect.add(autho)
                await connect.commit()
                return f'Пользователь {login} зарегистрирован!'
        else:
            return 'Пользователь с таким логином уже существует.'
    
    # test #
    @staticmethod
    async def get_autho(id: int) -> Autho:
        async with session.begin() as connect:
            query = (
                select(Autho)
                .filter(Autho.id == id)
            )
            result = await connect.execute(query)
            result = result.unique().scalars().one()
            autho = Autho(login = result.login
                          ,passw = result.passw)
            await connect.commit()
            return autho
    ###
    
    async def check_autho(login: str, passw: str) -> bool:
        async with session.begin() as connect:
            query = (
                select(Autho)
                .filter(Autho.login == login)
            )
            result = await connect.execute(query)
            result = result.unique().scalars().one()
            if hashlib.sha256(passw.encode('utf-8')).hexdigest() == result.passw:
                return True
            return False

    async def set_refresh(login: str, refresh_token: str):
        async with session.begin() as connect:
            query = (
                select(Autho)
                .filter(Autho.login == login)
            )
            result = await connect.execute(query)
            result = result.unique().scalars().one()
            if result:
                result.refresh_token = hashlib.sha256(refresh_token.encode('utf-8')).hexdigest()
            await connect.commit()
            return f'Пользователь {login} успешно прошел аунтефикацию.'
        
