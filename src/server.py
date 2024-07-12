from flask import Flask, request, render_template

from helpers.helper_server import HelperDBParse
from src.hardware.board import Board

app = Flask(__name__)

board = Board()
# board = None


def init_board() -> None:

    def cb_insert_db(data):
        helper = HelperDBParse()
        helper.insert_data_board(data=data)

    if not board.is_running():
        board.init()
        board.cb_get_snapshot = cb_insert_db
        board.loop_main(False)


def action_led(ledToChange: dict) -> None:
    if board:
        if board.is_running() and ledToChange.get("key"):
            if ledToChange.get("key") == "led_1":
                board.led_on(1) if ledToChange.get("value") else board.led_off(1)
            elif ledToChange.get("key") == "led_2":
                board.led_on(2) if ledToChange.get("value") else board.led_off(2)
            elif ledToChange.get("key") == "btn_1":
                board.led_toggle(1)
            elif ledToChange.get("key") == "btn_2":
                board.led_toggle(2)


@app.route("/")
def home():

    init_board()
    helper = HelperDBParse()

    key = request.args.get("key")
    value = request.args.get("value")

    if key and value:
        value = int(value)
        action_led({"key": key, "value": value})
        helper.insert_data_fronted({"key": key, "value": value})

    data = helper.get_data()
    print(f"data to dashboard {data}")

    return render_template(
        "index.jinja",
        data={
            "data": data,
            "status": board,
        },
    )


@app.errorhandler(404)
def not_found(e):
    return '<h1>Not found back to home please</h1> <h2><a href="/">Back</a> </h2>'


app.run(host="0.0.0.0", port=3000, debug=True)
