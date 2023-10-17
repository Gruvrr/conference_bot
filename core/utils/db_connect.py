import asyncpg
from core import settings

DATABASE_URL = settings.db_settings.db_url
print(f"This is url - {DATABASE_URL}")

async def create_pool():
    return await asyncpg.create_pool(DATABASE_URL)


async def add_user(pool, user_id, username, first_name, last_name):
    async with pool.acquire() as connection:
        await connection.execute("""
            INSERT INTO users (user_id, username, first_name, last_name) VALUES ($1, $2, $3, $4)
            ON CONFLICT (user_id) DO NOTHING
        """, user_id, username, first_name, last_name)


async def get_all_users(pool):
    async with pool.acquire() as connection:
        return await connection.fetch("SELECT * FROM users")