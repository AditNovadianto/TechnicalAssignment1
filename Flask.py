from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=['POST','GET'])
def receive_data():
    print("Received request with headers:")
    print(request.headers)
    
    if request.is_json:
        data = request.json
        print("Received JSON data:")
        print(data)
        
        temperature = data.get('temperature')
        humidity = data.get('humidity')

        if temperature is not None and humidity is not None:
            response = {
                "status": "success",
                "temperature": temperature,
                "humidity": humidity,
                "message": "Data Diterima"
            }
            return jsonify(response), 200
        else:
            response = {
                "status": "error",
                "message": "Invalid data"
            }
            return jsonify(response), 400
    else:
        response = {
            "status": "error",
            "message": "Unsupported Media Type"
        }
        return jsonify(response), 415

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
