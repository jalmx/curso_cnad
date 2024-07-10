from pyfirmata2 import Arduino
from time import sleep


class Board:

    _BTN_1 = 2
    _BTN_2 = 3
    _LED_1 = 8
    _LED_2 = 9
    _SENSOR_1 = 0
    _SENSOR_2 = 1

    def __init__(self, port) -> None:
        self.board = Arduino(port)

    def _set_reporting(self):
        self.btn_1.enable_reporting()
        self.btn_2.enable_reporting()

    def _define_input(self): 
        self.btn_1 = self.board.get_pin(f"d:{self._BTN_1}:i")
        self.btn_2 = self.board.get_pin(f"d:{self._BTN_2}:i")

        self._set_reporting()
        print("config inputs")

    def _define_output(self):
        self.led_1 = self.board.get_pin(f"d:{self._LED_1}:o")
        self.led_2 = self.board.get_pin(f"d:{self._LED_2}:o")
        print("config outputs")

    def init(self):
        self.board.samplingOn(500)
        self._define_input()
        self._define_output()
        self._init_adc()

    def toggle_led(self, led_number: int):
        if led_number == 1:
            self.led_1.write(not self.led_1.read())
        elif led_number == 2:
            self.led_2.write(not self.led_2.read())

    def led_on(self, led_number: int):
        if led_number == 1:
            self.led_1.write(True)
        elif led_number == 2:
            self.led_2.write(True)

    def led_off(self, led_number: int):
        if led_number == 1:
            self.led_1.write(False)
        elif led_number == 2:
            self.led_2.write(False)

    def _init_adc(self):
        self.board.analog[self._SENSOR_1].enable_reporting()
        self.board.analog[self._SENSOR_2].enable_reporting()

    def close(self):
        self.board.exit()

    def loop_main(self, loop: bool = True):
        self.btn_1.register_callback(self.cb_btn_1)
        self.btn_2.register_callback(self.cb_btn_2)
        self.btn_1.enable_reporting()
        self.btn_2.enable_reporting()
        self.board.analog[self._SENSOR_1].register_callback(self.cb_analog_0)
        self.board.analog[self._SENSOR_2].register_callback(self.cb_analog_0)
        while loop:
            pass

    def cb_btn_1(self, value):

        if value:
            print("se presiono btn 1")
            self.led_1.write(not self.led_1.read())
            self.btn_1.disable_reporting()
            sleep(0.25)
            self._set_reporting()

    def cb_btn_2(self, value):

        if value:
            print("se presiono btn 2")
            self.led_2.write(not self.led_2.read())
            self.btn_2.disable_reporting()
            sleep(0.25)
            self._set_reporting()

    def cb_analog_0(self, data):
        print("valor:", (data))


