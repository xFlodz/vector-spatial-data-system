
from flask import Flask, jsonify, render_template
from config import Config
from models import db, Building, Road
from collector import fetch_buildings, fetch_roads
from processor import save_buildings, save_roads
import time
from sqlalchemy import text

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

for i in range(10):
    try:
        with app.app_context():
            db.engine.connect()
        break
    except Exception:
        time.sleep(5)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/init")
def init_database():
    with app.app_context():

        db.session.execute(db.text("CREATE EXTENSION IF NOT EXISTS postgis;"))
        db.session.commit()

        db.create_all()

        buildings_data = fetch_buildings()
        roads_data = fetch_roads()

        save_buildings(buildings_data)
        save_roads(roads_data)

    return jsonify({"message": "Database initialized"})

@app.route("/api/buildings")
def get_buildings():
    query = text(
        '''
        SELECT id, name, ST_AsGeoJSON(geometry) as geometry
        FROM building
        '''
    )

    result = db.session.execute(query)

    data = []

    for row in result:
        data.append({
            "id": row.id,
            "name": row.name,
            "geometry": row.geometry
        })

    return jsonify(data)

@app.route("/api/roads")
def get_roads():
    query = text(
        '''
        SELECT id, name, ST_AsGeoJSON(geometry) as geometry
        FROM road
        '''
    )

    result = db.session.execute(query)

    data = []

    for row in result:
        data.append({
            "id": row.id,
            "name": row.name,
            "geometry": row.geometry
        })

    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
