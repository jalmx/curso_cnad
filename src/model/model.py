from peewee import *
from datetime import datetime
from dotenv import dotenv_values
from src.config import path_env

name_db = dotenv_values(path_env).get("DATABASE")


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
    btn_1 = IntegerField(default=0)
    btn_2 = IntegerField(default=0)
    led_1 = IntegerField(default=0)
    led_2 = IntegerField(default=0)
    time_insert = DateTimeField(default=datetime.now)
    modify_by = CharField()

    def __str__(self) -> str:
        return f"id: {self.id} - sensor 1: {self.sensor_1} - sensor 2: {self.sensor_2} - btn 1: {self.btn_1} - btn 2: {self.btn_2} - led 1: {self.led_1} - led 2: {self.led_2}"
    class Meta:
        database = db
