from model.controller import ManageData
from model.model import Data


class HelperServer:
    _db = ManageData()

    def _data_to_dict(self):
        data = self._db.get_last_data()
        return {
            "sensor_1": data.sensor_1,
            "sensor_2": data.sensor_2,
            "btn_1": data.btn_1,
            "btn_2": data.btn_2,
            "led_1": data.led_1,
            "led_2": data.led_2,
            "modify_by": "dashboard",
        }

    def _dict_to_data(data_dict: dict):
        return Data(
            sensor_1=data_dict["sensor_1"],
            sensor_2=data_dict["sensor_2"],
            btn_1=data_dict["btn_1"],
            btn_2=data_dict["btn_2"],
            led_1=data_dict["led_1"],
            led_2=data_dict["led_2"],
            modify_by=data_dict["modify_by"],
        )

    def insert_data(self, data_fronted: dict):
        data = self._data_to_dict(data_fronted)
        data[data_fronted["key"]] = data_fronted["value"]
        new_data = self._dict_to_data(data)
        self._db.insert_data(new_data)

        print(data_fronted)

    def get_data(self):
        return self._db.get_last_data()
