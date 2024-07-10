from src.hardware.connection import Board


if __name__ == "__main__":
    port = "/dev/ttyUSB0"

    arduino = Board(port=port)
    arduino.init()
    arduino.loop_main()
