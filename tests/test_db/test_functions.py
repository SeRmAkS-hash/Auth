import pytest,pytest_asyncio
from src.db.functions import FuncAutho
from src.db.config import session,engine
from src.db.setting import setting
from src.db.models import Autho,Base
from src.auth.configtoken import auth
 
@pytest_asyncio.fixture(scope='session',autouse=True)
async def setup_db():
    async with engine.begin() as connect:
        await connect.run_sync(Base.metadata.drop_all)
        await connect.run_sync(Base.metadata.create_all)
        assert setting.MODE == 'Test'

@pytest.mark.usefixtures('setup_db')
class TestFuncAutho:
    
    @pytest.fixture(scope='session')
    def autho(self):
        autho = Autho(login = 'sermaks'
                      ,passw = 'qwerty0')
        return autho
    
    @pytest.mark.asyncio(loop_scope = 'session')
    async def test_input_autho(self,autho):
        comments = await FuncAutho.input_autho(autho.login,autho.passw)
        assert comments == f'Пользователь {autho.login} зарегистрирован!'
        result = await FuncAutho.get_autho(id=1)
        assert result.login == autho.login
        
    @pytest.mark.asyncio(loop_scope = 'session')
    async def test_check_autho(self,autho):
        result = await FuncAutho.check_autho(autho.login,autho.passw)
        assert True == result
        
    @pytest.mark.asyncio(loop_scope = 'session')
    async def test_set_refresh(self):
        login = 'sermaks'
        auth.create_refresh(login)
        result = await FuncAutho.set_refresh(login = 'sermaks'
                                            ,refresh_token = auth.REFRESH)
        assert result == f'Пользователь {login} успешно прошел аунтефикацию.'
    