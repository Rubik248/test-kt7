import pytest
import aiopg
import asyncio

async def add_to_database(conn, value):
    async with conn.cursor() as cursor:
        await cursor.execute("INSERT INTO your_table_name (column_name) VALUES (%s)", (value,))
        await conn.commit()

async def test_database_interaction():
    dsn = 'dbname=database user=user password=password host=host port=port'
    value_to_insert = 'test_value'

    async with aiopg.create_pool(dsn) as pool:
        async with pool.acquire() as conn:
            await add_to_database(conn, value_to_insert)

            async with conn.cursor() as cursor:
                await cursor.execute("SELECT * FROM your_table_name WHERE column_name = %s", (value_to_insert,))
                result = await cursor.fetchone()

                assert result is not None
                assert result[0] == value_to_insert