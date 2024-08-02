from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def handle_post():
    try:
        data = request.get_json()

        # Extracting the data
        full_name = data.get("full_name")
        dob = data.get("dob")  # Expecting dob in ddmmyyyy format
        numbers = [int(n) for n in data.get("numbers", [])]
        alphabets = [char for char in data.get("alphabets", [])]

        user_id = f"{full_name.replace(' ', '_').lower()}_{dob}"
        is_success = True

        response = {
            "user_id": user_id,
            "is_success": is_success,
            "numbers": numbers,
            "alphabets": alphabets
        }
    except Exception as e:
        response = {
            "user_id": None,
            "is_success": False,
            "error": str(e)
        }

    return jsonify(response)

@app.route('/bfhl', methods=['GET'])
def handle_get():
    response = {
        "operation_code": 1
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
