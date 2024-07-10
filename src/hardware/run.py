from src.hardware.board import Board
from src.helpers.helper_server import HelperDBParse

def cb_insert_db(data):
    helper = HelperDBParse()
    helper.insert_data_board(data=data)

if __name__ == "__main__":
    port = "/dev/ttyUSB0"

    arduino = Board(port=port)
    arduino.init()
    arduino.cb_get_snapshot = cb_insert_db
    arduino.loop_main()
