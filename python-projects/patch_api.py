from flask import Flask, request, jsonify

patch_api = Flask (__name__)

#fake in memory data

user = {"name": "Queen",
        "email": "queen@example.com"}

@patch_api.route("/user", methods=["GET"])
def get_user():
    return jsonify(user)

@patch_api.route("/user", methods=["PATCH"])
def update_user():
    data = request.json
    for key in data:
       if key in user:
          user[key] = data[key]
    return jsonify(user)


if __name__ == '__main__':
  patch_api.run(debug=True)

  