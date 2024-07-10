from pyfirmata2 import Arduino
from time import sleep


class Board:

    _BTN_1 = 2
    _BTN_2 = 3
    _LED_1 = 8
    _LED_2 = 9
    _SENSOR_1 = 0
    _SENSOR_2 = 1

    _value_sensor_1 = 0
    _value_sensor_2 = 0
    _value_led_1 = 0
    _value_led_2 = 0
    _value_btn_1 = 0
    _value_btn_2 = 0

    cb_get_snapshot = None

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
        self.board.samplingOn(800)
        self._define_input()
        self._define_output()
        self._init_adc()

    def _set_value_led(self, led, led_number: int):
        if led_number == 1:
            self._value_led_1 = led.read()
        elif led_number == 2:
            self._value_led_2 = led.read()

    def toggle_led(self, led_number: int):
        if led_number == 1:
            self.led_1.write(not self.led_1.read())
            self._set_value_led(self.led_1, led_number=led_number)
        elif led_number == 2:
            self.led_2.write(not self.led_2.read())
            self._set_value_led(self.led_2, led_number=led_number)

    def led_on(self, led_number: int):
        if led_number == 1:
            self.led_1.write(True)
            self._set_value_led(self.led_1, led_number=led_number)
        elif led_number == 2:
            self.led_2.write(True)
            self._set_value_led(self.led_2, led_number=led_number)

    def led_off(self, led_number: int):
        if led_number == 1:
            self.led_1.write(False)
            self._set_value_led(self.led_1, led_number=led_number)
        elif led_number == 2:
            self.led_2.write(False)
            self._set_value_led(self.led_2, led_number=led_number)

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
            self._value_btn_1 = value
            self._get_snapshot()
            self._value_btn_1 = 0
            self.btn_1.disable_reporting()
            sleep(0.25)
            self._set_reporting()

    def cb_btn_2(self, value):

        if value:
            print("se presiono btn 2")
            self.led_2.write(not self.led_2.read())
            self._value_btn_2 = value
            self._get_snapshot()
            self._value_btn_2 = 0
            self.btn_2.disable_reporting()
            sleep(0.25)
            self._set_reporting()

    def _fix_number(self,value: float):
        number = str(value)
        
        if len(number) < 5:
            return value
        else:
            return float( number[0:5])

    def cb_analog_0(self, data):
        self._value_sensor_1 = self._fix_number(data)
        self._get_snapshot()
        print("sensor 1:", data)

    def cb_analog_1(self, data):
        self._value_sensor_2 = self._fix_number(data)
        self._get_snapshot()
        print("sensor 2:", data)

    def _generate_snapshot(self):
        return {
            "sensor_1": self._value_sensor_1,
            "sensor_2": self._value_sensor_2,
            "led_1": self._value_led_1,
            "led_2": self._value_led_2,
            "btn_1": self._value_btn_1,
            "btn_2": self._value_btn_2,
            "modify_by": "board",
        }

    def _get_snapshot(self):
        if self.cb_get_snapshot:
            return self.cb_get_snapshot(self._generate_snapshot())
        return None
