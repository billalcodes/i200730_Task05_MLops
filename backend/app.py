from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

# MongoDB configuration
app.config['MONGO_URI'] = 'mongodb://mongodb:27017/mydatabase'  # Replace 'mydatabase' with your database name
mongo = PyMongo(app)

# Endpoint to store information in MongoDB
@app.route('/store-info', methods=['POST'])
def store_info():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    if name and email:
        db = mongo.db.users
        db.insert_one({'name': name, 'email': email})
        return jsonify({'message': 'Information stored successfully'}), 200
    else:
        return jsonify({'error': 'Invalid data format'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
