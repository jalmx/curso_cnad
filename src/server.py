from flask import Flask, request, render_template

from helpers.helper_server import HelperDBParse

app = Flask(__name__)


@app.route("/")
@app.route("/*")
def home():
    helper = HelperDBParse()
    if request.method == "GET":
        key = request.args.get("key")
        value = request.args.get("value")

        if key and value:
            value = int(value)
            print(f"value to insert => key:{key} - value= {value}")
            helper.insert_data_fronted({"key": key, "value": value})

    data = helper.get_data()
    print(data)
    return render_template("index.jinja", data={"data": data})


app.run(host="0.0.0.0", port=3000, debug=True)
