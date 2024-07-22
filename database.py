from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from config import DATABASE_URL


engine = create_async_engine(DATABASE_URL, echo=True)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)



async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


# def test_insert_or_update():
#     insert_stmt = insert(the_table).values(
#         id = 'xxx',
#         col1 = 'insert value',
#     )
#     on_duplicate_key_stmt = insert_stmt.on_duplicate_key_update(
#         # col1 = insert_stmt.inserted.data,
#         col1 = 'update value',
#         col2 = 'mark'
#     )
#     print(on_duplicate_key_stmt)
#     session.execute(on_duplicate_key_stmt)
#     session.commit()