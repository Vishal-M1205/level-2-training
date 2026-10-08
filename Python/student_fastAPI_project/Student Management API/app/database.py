import psycopg
from app.core.config import config
from psycopg.rows import dict_row

#! By default psycopg returns a tuple / list[tuple]
# * In the case we can use row_factory = dict_row
# ! the psycopg will return this as a dictionary instead of tuple


def get_connection():
    """Takes the connection params required by the postgre sql ConnParams : *kwargs and
    returns the connection object  -
    since it is a AsyncConnection it return a awaitable coroutine"""
    return psycopg.AsyncConnection.connect(
        host=config.database_host,
        port=config.database_port,
        dbname=config.database_name,
        user=config.database_user,
        password=config.database_password,
        row_factory=dict_row,
    )
