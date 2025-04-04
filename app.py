from flask import Flask, request, jsonify

app = Flask(__name__)

# Home route (GET request)
@app.route('/')
def home():
    return "Hello from Flask!"

# GET route with query parameters
@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'stranger')
    return f"Hello, {name}!"

# POST route with JSON body
@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({
        "you_sent": data
    })

# POST route with form data
@app.route('/submit-form', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    email = request.form.get('email')
    return f"Received form submission: {name}, {email}"

if __name__ == '__main__':
    app.run(debug=True)
