from flask import Flask, request, jsonify
from geopy.distance import geodesic
import datetime

app = Flask(__name__)

# Store locations and logs (temporary storage for demo purposes)
locations = []

@app.route('/update_location', methods=['POST'])
def update_location():
    data = request.json
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    timestamp = datetime.datetime.now()

    # Save to locations log
    location_entry = {
        'latitude': latitude,
        'longitude': longitude,
        'timestamp': timestamp
    }
    locations.append(location_entry)

    return jsonify({"status": "Location updated", "timestamp": timestamp}), 200

@app.route('/get_locations', methods=['GET'])
def get_locations():
    return jsonify(locations), 200

@app.route('/calculate_distance', methods=['GET'])
def calculate_distance():
    if len(locations) < 2:
        return jsonify({"error": "Not enough data to calculate distance"}), 400
    
    start = locations[0]
    end = locations[-1]
    distance = geodesic((start['latitude'], start['longitude']), (end['latitude'], end['longitude'])).meters
    return jsonify({"distance_meters": distance}), 200

if __name__ == '__main__':
    app.run(debug=True)
