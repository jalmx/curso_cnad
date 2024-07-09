from peewee import *
from datetime import datetime
from dotenv import dotenv_values

name_db = config = dotenv_values("../.env").get("DATABASE")

print(f"dir db: {name_db}")

db = SqliteDatabase(
    name_db,
    pragmas={
        "journal_mode": "wal",  # WAL-mode.
        "cache_size": -64 * 1000,  # 64MB cache.
        "synchronous": 0,
    },
)


class Data(Model):
    id = AutoField()
    sensor_1 = DoubleField(default=0)
    sensor_2 = DoubleField(default=0)
    btn_1 = BooleanField(default=False)
    btn_2 = BooleanField(default=False)
    led_1 = BooleanField(default=False)
    led_2 = BooleanField(default=False)
    time_insert = DateTimeField(default=datetime.now)
    modify_by = CharField()

    class Meta:
        database = db
