from api.route import route,route_test
from fastapi import FastAPI
from auth.configtoken import auth
from db.functions import Setup
import uvicorn
import asyncio

app = FastAPI()
auth.TOKEN.handle_errors(app=app)
app.include_router(router=route)
app.include_router(router=route_test)


# async def main():
#     await asyncio.gather(Setup.setup_db())


if __name__ == "__main__":
    # asyncio.run(main())
    uvicorn.run('main:app',host='127.0.0.1')