from flask import gcpFlask, jsonify, requester

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return "Welcome to the Sample Flask App! Changed in local repo"

time.sleep(20)

# Route for a sample API endpoint
@app.route('/api/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'World')
    return jsonify({"message": f"Hello, {name}!"})

# Start the Flask development server
if __name__ == '__main__':
    app.run(debug=True)

