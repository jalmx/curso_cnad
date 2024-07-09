from .Dao import Dao
from .model import Data


class ManageData(Dao):

    db = Data()

    def __init__(self) -> None:
        super().__init__()
        self._create_table()

    def _create_table(self):
        if not self.db.table_exists():
            self.db.create_table()

    def insert_data(self, data: Data):
        data.save()

    def get_last_data(self):
        try:
            return [e for e in self.db.select()][-1]
        except:
            return None

    def get_all(self):
        return self.db.select()
