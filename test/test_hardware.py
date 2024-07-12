from src.hardware.board import Board


if __name__ == "__main__":
    port = "/dev/ttyUSB0"

    arduino = Board()
    arduino.init()
    arduino.loop_main()
