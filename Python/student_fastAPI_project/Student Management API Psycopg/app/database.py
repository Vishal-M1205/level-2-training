import psycopg
from fastapi import Request
from psycopg_pool import AsyncConnectionPool
from app.core.config import config
from psycopg.rows import dict_row
from collections.abc import AsyncGenerator

#! By default psycopg returns a tuple / list[tuple]
# * In the case we can use row_factory = dict_row
# ! the psycopg will return this as a dictionary instead of tuple

"""
AsyncConnection where the connection() starts when the application run , 
and the connection get closed when the app closes.
No connectuion is closed after a specific request (repository request) , either it stays idle until other request comes

conninfo takes db string 

wait = True - app starts only when (min_sizze refers to the) connnection 
get started

connection grows until max_size 

open = False - means we  use open(wait=True) , for that the connection need not be init when the pool
object is created 
"""
pool = AsyncConnectionPool(
    conninfo="",
    kwargs={
        "host": config.database_host,
        "port": config.database_port,
        "dbname": config.database_name,
        "user": config.database_user,
        "password": config.database_password,
        "row_factory": dict_row,
    },
    min_size=2,
    max_size=10,
    open=False,
)


# def get_connection():
#     """Takes the connection params required by the postgre sql ConnParams : *kwargs and
#     returns the connection object  -
#     since it is a AsyncConnection it return a awaitable coroutine"""
#     return psycopg.AsyncConnection.connect(
#         host=config.database_host,
#         port=config.database_port,
#         dbname=config.database_name,
#         user=config.database_user,
#         password=config.database_password,
#         row_factory=dict_row,
#     )


#! AsyncGenerator - a generator for the async functions , as a generator function won't terninate
# ! by returning its all value use yeild to preserve the state and pauses the execution


# async def get_db_connection() -> AsyncGenerator[psycopg.AsyncConnection, None]:
#     async with await get_connection() as connection:
#         yield connection

#! How this normal function access the request actually ?
# * Answer -Depends() the chain route-service-repo- and repo depends the get_db_connection()
# * So fastapi resove the param of this get_db_connection first


async def get_db_connection(
    request: Request,
) -> AsyncGenerator[psycopg.AsyncConnection, None]:
    #! No need for await bbecause it gets the async contextmanager which borrows the
    #! connection from the pool , not creating a connection
    async with request.app.state.db_pool.connection() as connection:
        yield connection
