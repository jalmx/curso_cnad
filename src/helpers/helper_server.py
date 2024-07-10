from src.model.controller import ManageData
from src.model.model import Data


class HelperDBParse:
    _db = ManageData()

    def _data_base_dict(self):
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

    def _change_data(self, data_raw:dict, data_frontend:dict):
        
        print(f"data base: {data_raw}")
        print(f"data fronted: {data_frontend}")
        
        data_raw[data_frontend["key"]] = data_frontend["value"]
        
        return data_raw
    
    def _dict_to_data(self,data_dict: dict):
        return Data(
            sensor_1=data_dict["sensor_1"],
            sensor_2=data_dict["sensor_2"],
            btn_1=data_dict["btn_1"],
            btn_2=data_dict["btn_2"],
            led_1=data_dict["led_1"],
            led_2=data_dict["led_2"],
            modify_by=data_dict["modify_by"],
        )

    def insert_data_fronted(self, data_fronted: dict):
        data_base = self._data_base_dict()
        new_data = self._change_data( data_base, data_fronted)
        print(f"data like dict from fronted: {new_data}")
        
        data_to_insert = self._dict_to_data(new_data)
        self._db.insert_data(data_to_insert)
    
    
    def insert_data_board(self, data: dict):
        print(f"data like dict from board: {data}")
        data_to_insert = self._dict_to_data(data)
        self._db.insert_data(data_to_insert)


    def get_data(self):
        return self._db.get_last_data()
