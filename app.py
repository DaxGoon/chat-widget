"""
app.py the main app file for Flask.
"""


# imports
from flask import Flask, render_template, request, jsonify, make_response, json
from flask_cors import CORS
from pusher import pusher
import simplejson


# initiate the app
app = Flask(__name__)
cors = CORS(app)
app.config["CORSHEADERS"] = "content-Type"

# configure the pusher object
pusher = pusher.Pusher(
    app_id="757974",
    key="KEY",
    secret="SECRET",
    cluster="eu",
    ssl=True
)


# define routes
@app.route("/new/guest", methods=["POST"])
def guestUser():
    data = request.json
    pusher.trigger(u"general-channel", u"new-guest-details", {
        "name": data["name"],
        "email": data["email"]
    })
    return json.dumps(data)


@app.route("/pusher/auth", methods=["POST"])
def pusher_authentication():
    auth = pusher.authenticate(channel=request.form["channel_name"], socket_id=request.form["socket_id"])
    return json.dumps(auth)


# run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
