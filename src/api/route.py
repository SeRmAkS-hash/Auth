from fastapi import APIRouter,Request,Response,Depends
from api.schemas import AuthPy
from db.functions import FuncAutho
from auth.configtoken import auth,RequestToken

route = APIRouter(prefix='/api/v1/Authorization',tags=['Auth'])
route_test = APIRouter(prefix='/Test',tags=['EndPointforTest'])

@route.post('/auth_registr')
async def auth_post(auth: AuthPy):
    result = await FuncAutho.input_autho(auth.login,auth.passw)
    return result

@route.post('/auth_check')
async def auth_check(autho: AuthPy,responce: Response):
    result = await FuncAutho.check_autho(autho.login,autho.passw)
    if result:
        auth.create_access(autho.login)
        auth.create_refresh(autho.login)
        responce.headers['Authorization'] = auth.ACCESS
        res = await FuncAutho.set_refresh(autho.login,auth.REFRESH)
        return res
    return 'Неверный логин или пароль!'


@route_test.get('/endpoint',dependencies=[Depends(auth.TOKEN.access_token_required)])
async def test_func():
    return 'Всем привет!'
