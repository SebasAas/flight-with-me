from flask import Flask, jsonify, request
from flask_pymongo import pymongo
from flask_cors import CORS

from bson import ObjectId

# Instantiation
app = Flask(__name__)

# DB Connection
CONNECTION_STRING = "mongodb+srv://adminFlightTrip:xKquf!gKej9QeEf@cluster0.ytwmp.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client["FlightTripDB"]
flight_collection = db["flights"]

# Settings
CORS(app)

# GET all flights
@app.route('/flights', methods=['GET'])
def getFlights():
    flights = []
    flights_collection = flight_collection.find({})

    for doc in flights_collection:
        flights.append({
            '_id': str(ObjectId(doc['_id'])),
            'destiny': doc['destiny'],
            'timeDeparture': doc['timeDeparture'],
            'timeArrival': doc['timeArrival'],
            'company': doc['company'],
            'airportDeparture': doc['airportDeparture'],
            'airportArrival': doc['airportArrival'],
            'price': doc['price'],
            'carryOn': doc['carryOn'],
            'image': doc['image'],
            'description': doc['description'],
        })

    return jsonify(flights);

# GET specific flight
@app.route('/flight/<id>', methods=['GET'])
def getFlight(id):
  flight = []
  flights_collection = flight_collection.find({'_id': ObjectId(id)})

  for doc in flights_collection:
      flight.append({
          '_id': str(ObjectId(doc['_id'])),
          'destiny': doc['destiny'],
          'timeDeparture': doc['timeDeparture'],
          'timeArrival': doc['timeArrival'],
          'company': doc['company'],
          'airportDeparture': doc['airportDeparture'],
          'airportArrival': doc['airportArrival'],
          'price': doc['price'],
          'carryOn': doc['carryOn'],
          'image': doc['image'],
          'description': doc['description'],
      })

  return jsonify(flight);


# CREATE flight
@app.route('/flight', methods=['POST'])
def createFlight():
  id = flight_collection.insert_one({
    'destiny': request.json['destiny'],
    'timeDeparture': request.json['timeDeparture'],
    'timeArrival': request.json['timeArrival'],
    'company': request.json['company'],
    'airportDeparture': request.json['airportDeparture'],
    'airportArrival': request.json['airportArrival'],
    'price': request.json['price'],
    'carryOn': request.json['carryOn'],
    'image': request.json['image'],
    'description': request.json['description']
  })

  return jsonify({'message': 'Flight Created'})

# DELETE Flight
@app.route('/flight/<id>', methods=['DELETE'])
def deleteFlight(id):
  flight_collection.delete_one({'_id': ObjectId(id)})
  return jsonify({'message': 'Flight Deleted'})

@app.route('/flight/<id>', methods=['PUT'])
def updateFlight(id):
  flight_collection.update_one({'_id': ObjectId(id)}, {"$set": {
    'destiny': request.json['destiny'],
    'timeDeparture': request.json['timeDeparture'],
    'timeArrival': request.json['timeArrival'],
    'company': request.json['company'],
    'airportDeparture': request.json['airportDeparture'],
    'airportArrival': request.json['airportArrival'],
    'price': request.json['price'],
    'carryOn': request.json['carryOn'],
    'image': request.json['image'],
    'description': request.json['description']
  }})
  return jsonify({'message': 'Flight Updated'})

if __name__ == "__main__":
    app.run(debug=True)
