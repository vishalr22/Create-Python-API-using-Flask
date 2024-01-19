from flask import Flask, request, jsonify

app = Flask(__name__)  # Create Flask App

# route is kind of endpoint location of an API
@app.route("/get_user/<user_id>")  # GET request
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "Vishal Rawat",
        "email": "vishal22rawat@gmail.com"
    }

    response_code = 200

    # Adding a query parameter to the url
    query = request.args.get("query")
    if query:
        user_data["query"] = query

    return jsonify(user_data), response_code


@app.route("/create-user", methods=["POST"])  # POST request
def create_user():
    data = request.get_json()
    response_code = 201
    return jsonify(data), response_code
# Test the POST API call using API platform like POSTMAN


if __name__ == "__main__":
    app.run(debug=True)  # Run flask server
