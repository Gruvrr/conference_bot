from environs import Env
from dataclasses import dataclass


@dataclass
class DBSettings:
    host: str
    password: str
    user: str
    db_name: str


def create_database_url(path: str):
    env = Env()
    env.read_env(path)

    user = env.str("MYBOTUSER")
    password = env.str("MYPASSWORD")
    host = env.str("LOCALHOST", default="localhost")  # Устанавливаем localhost как значение по умолчанию
    dbname = env.str("MYNAMEDB")
    return DBSettings(host=host, user=user, password=password, db_name=dbname)

@dataclass
class Bots:
    bot_token: str
    admin_id: int


@dataclass
class Settings:
    bots: Bots


def get_settings(path: str):
    env = Env()
    env.read_env(path)

    return Settings(
        bots=Bots(
            bot_token=env.str("TOKEN"),
            admin_id=env.str("ADMIN_ID")
        )
    )


get_settings = get_settings('input')
db_settings = create_database_url('input')
print(get_settings)
