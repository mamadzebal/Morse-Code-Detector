from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# Variable to store the sending state
sending_data = False

@app.route('/string', methods=['GET'])
def receive_string():
    # Get the string from the query parameters
    string_data = request.args.get('data')
    
    # Write the string to a file
    with open('output.txt', 'a') as file:
        file.write(string_data)
    
    return 'String received and saved to file successfully!\n'


@app.route('/clear', methods=['GET'])
def clear_string():
    # Get the string from the query parameters
    # string_data = request.args.get('data')
    
    # Write the string to a file
    with open('output.txt', 'w') as file:
        file.write("")
    
    return 'String received and saved to file successfully!\n'


@app.route('/cursor', methods=['GET'])
def send_string():
    global sending_data
    data = request.args.get('data')
    sending_data = data

    return "Sending data"


@app.route('/status', methods=['GET'])
def check_status():
    global sending_data
    return jsonify({'sending': sending_data})

if __name__ == '__main__':
    app.run(host='192.168.137.1', port=5000, debug=True)
    # app.run(debug=True)