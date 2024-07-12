from pyfirmata2 import Arduino
from time import sleep


class Board:

    _value_sensor_1 = 0
    _value_sensor_2 = 0
    _value_led_1 = False
    _value_led_2 = False
    _value_btn_1 = False
    _value_btn_2 = False
    _status = False
    cb_get_snapshot = None

    def __init__(
        self,
        port=None,
        pinLed1=8,
        pinLed2=9,
        pinBtn1=2,
        pinBtn2=3,
        pinSensor1=0,
        pinSensor2=1,
    ) -> None:
        port = port or Arduino.AUTODETECT
        self.board = Arduino(port)
        self._PIN_LED_1 = pinLed1
        self._PIN_LED_2 = pinLed2
        self._PIN_BTN_1 = pinBtn1
        self._PIN_BTN_2 = pinBtn2
        self._PIN_SENSOR_1 = pinSensor1
        self._PIN_SENSOR_2 = pinSensor2
        print("init board")

    def get_pin_led_1(self):
        return self._PIN_LED_1

    def get_pin_led_2(self):
        return self._PIN_LED_2

    def get_pin_btn_1(self):
        return self._PIN_BTN_1

    def get_pin_btn_2(self):
        return self._PIN_BTN_2

    def is_running(self) -> bool:
        return self._status

    def _set_reporting(self):
        self.btn_1.enable_reporting()
        self.btn_2.enable_reporting()

    def _define_input(self):
        self.btn_1 = self.board.get_pin(f"d:{self._PIN_BTN_1}:i")
        self.btn_2 = self.board.get_pin(f"d:{self._PIN_BTN_2}:i")

        self._set_reporting()
        print("config inputs")

    def _define_output(self):
        self.led_1 = self.board.get_pin(f"d:{self._PIN_LED_1}:o")
        self.led_2 = self.board.get_pin(f"d:{self._PIN_LED_2}:o")
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

    def led_toggle(self, led_number: int):
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
        self.board.analog[self._PIN_SENSOR_1].enable_reporting()
        self.board.analog[self._PIN_SENSOR_2].enable_reporting()

    def close(self):
        self.board.exit()

    def loop_main(self, loop: bool = True):
        self.btn_1.register_callback(self.cb_btn_1)
        self.btn_2.register_callback(self.cb_btn_2)
        self.btn_1.enable_reporting()
        self.btn_2.enable_reporting()
        self.board.analog[self._PIN_SENSOR_1].register_callback(self.cb_analog_0)
        self.board.analog[self._PIN_SENSOR_2].register_callback(self.cb_analog_1)
        self._status = True
        while loop:
            pass

    def cb_btn_1(self, value):

        if value:
            print("Pressed btn 1")
            self.led_toggle(1)
            self._value_btn_1 = value
            self._get_snapshot()
            self._value_btn_1 = 0
            self.btn_1.disable_reporting()
            sleep(0.25)
            self._set_reporting()

    def cb_btn_2(self, value):

        if value:
            print("Pressed btn 2")
            self.led_toggle(2)
            self._value_btn_2 = value
            self._get_snapshot()
            self._value_btn_2 = 0
            self.btn_2.disable_reporting()
            sleep(0.25)
            self._set_reporting()

    def _fix_number(self, value: float):
        number = str(value)

        if len(number) < 5:
            return value
        else:
            return float(number[0:5])

    def cb_analog_0(self, data):
        self._value_sensor_1 = self._fix_number(data * 100)
        self._get_snapshot()
        # print("sensor 1:", data)

    def cb_analog_1(self, data):
        self._value_sensor_2 = self._fix_number(data * 100)
        self._get_snapshot()
        # print("sensor 2:", data)

    def _generate_snapshot(self):
        return {
            "sensor_1": self._value_sensor_1 or 0.0,
            "sensor_2": self._value_sensor_2 or 0.0,
            "led_1": 1 if self._value_led_1 else 0,
            "led_2": 1 if self._value_led_2 else 0,
            "btn_1": 1 if self._value_btn_1 else 0,
            "btn_2": 1 if self._value_btn_2 else 0,
            "modify_by": "board",
        }

    def _get_snapshot(self):
        if self.cb_get_snapshot:
            return self.cb_get_snapshot(self._generate_snapshot())
        return None

    def __str__(self) -> str:
        return self.board.__str__()
