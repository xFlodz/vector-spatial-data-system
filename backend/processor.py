
from models import db, Building, Road
from geoalchemy2.shape import from_shape
from shapely.geometry import Polygon, LineString

def save_buildings(data):
    for element in data.get("elements", []):
        if "geometry" not in element:
            continue

        coords = [(p["lon"], p["lat"]) for p in element["geometry"]]

        try:
            polygon = Polygon(coords)

            building = Building(
                name=element.get("tags", {}).get("name", "Unknown"),
                geometry=from_shape(polygon, srid=4326)
            )

            db.session.add(building)

        except Exception:
            continue

    db.session.commit()

def save_roads(data):
    for element in data.get("elements", []):
        if "geometry" not in element:
            continue

        coords = [(p["lon"], p["lat"]) for p in element["geometry"]]

        try:
            line = LineString(coords)

            road = Road(
                name=element.get("tags", {}).get("name", "Unknown"),
                geometry=from_shape(line, srid=4326)
            )

            db.session.add(road)

        except Exception:
            continue

    db.session.commit()
