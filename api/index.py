from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

URL = "https://apis.evotopup.com/api/game-id-checker"

HEADERS = {
    "accept": "application/json",
    "content-type": "application/json",
    "Origin": "https://evotopup.com",
    "Referer": "https://evotopup.com/",
    "User-Agent": "Mozilla/5.0"
}


@app.route("/", methods=["GET"])
def check_uid():
    uid = request.args.get("uid")

    if not uid:
        return jsonify({
            "status": False,
            "message": "Missing uid parameter"
        }), 400

    payload = {
        "playerid": uid
    }

    try:
        response = requests.post(
            URL,
            json=payload,
            headers=HEADERS,
            timeout=15
        )

        return jsonify(response.json()), response.status_code

    except Exception as e:
        return jsonify({
            "status": False,
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
