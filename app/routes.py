from flask import Blueprint, jsonify, request
import random
import string

main = Blueprint('main', __name__)
data_storage = {}

@main.route('/fetch-data', methods=['GET'])
def fetch_data():

    mock_data = {
        "id": ''.join(random.choices(string.ascii_uppercase + string.digits, k=6)),
        "name": "Vervoe Product",
        "price": random.uniform(10.0, 100.0),
        "description": "This is a Vervoe product description."
    }
    # Process the data
    processed_data = process_data(mock_data)
    # Store the data in memory
    data_storage[mock_data['id']] = processed_data
    return jsonify({"message": "Data fetched and processed successfully", "data": processed_data})

@main.route('/get-processed-data', methods=['GET'])
def get_processed_data():
    return jsonify(data_storage)

def process_data(data):
    processed_data = {k: (v.upper() if isinstance(v, str) else v) for k, v in data.items()}
    return processed_data
