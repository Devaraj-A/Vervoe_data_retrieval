# Vervoe Data Retrieval and Processing Application

## Description
This Flask application simulates a simplified version of a data retrieval and processing system.

## Features
1. **API Endpoint for Data Retrieval**: Fetches mock data from an external service and processes it.
2. **Data Processing**: Converts all text in the fetched data to uppercase.
3. **Data Storage**: Stores the processed data in temporary in-memory storage.
4. **API Endpoint for Data Retrieval**: Retrieves the processed data stored in memory.

## Requirements
- Python 3.8+
- Flask 2.1.2

## Setup and Running

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Devaraj-A/Vervoe_data_retrieval.git
    cd flask_data_retrieval
    ```

2. **Set up a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Flask application**:
    ```bash
    python run.py
    ```

## Usage
- **Fetch Data**: Make a GET request to `/fetch-data`.
- **Get Processed Data**: Make a GET request to `/get-processed-data`.

## Example Requests
1. **Fetch Data**:
    ```bash
    curl http://127.0.0.1:5000/fetch-data
    ```

2. **Get Processed Data**:
    ```bash
    curl http://127.0.0.1:5000/get-processed-data
    ```

## Notes
- Ensure that the virtual environment is activated before running the application.
