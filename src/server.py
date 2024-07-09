from flask import Flask, request, render_template

from helpers.helper_server import HelperServer

app = Flask(__name__)


@app.route("/")
@app.route("/*")
def home():
    helper = HelperServer()
    if request.method == "GET":

        if request.args.get("key"):
            key = request.args.get("key")
            value = request.args.get("value")
            print(f"value to insert => key:{key} - value= {value}")
            helper.insert_data(
                {"key": request.args.get("key"), "value": request.args.get("value")}
            )
    data = helper.get_data()
    return render_template("index.jinja", data={"data": data})


app.run(host="0.0.0.0", port=3000, debug=True)
