from sqlalchemy.ext.asyncio import async_sessionmaker,create_async_engine
from db.setting import setting

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

engine = create_async_engine(setting.connect())
session = async_sessionmaker(engine)

# engine_sync = create_engine(con.connect())
# session_sync = sessionmaker(engine_sync)


            