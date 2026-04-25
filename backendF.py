from flask import Flask, jsonify
import csv

app = Flask(__name__)

def load_incidents():
    incidents = []
    with open("incidents.csv", newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            incidents.append({
                "type": row["IncidentType"],
                "location": row["Location"],
                "severity": row["Severity"],
                "resource": row["AssignedResource"],
                "coords": [float(row["Latitude"]), float(row["Longitude"])]
            })
    return incidents

@app.route("/incidents", methods=["GET"])
def get_incidents():
    return jsonify(load_incidents())

if __name__ == "__main__":
    app.run(debug=True)
