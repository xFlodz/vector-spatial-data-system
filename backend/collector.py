import requests

OVERPASS_URL = "https://overpass.kumi.systems/api/interpreter"


def safe_request(query):
    try:
        response = requests.get(
            OVERPASS_URL,
            params={"data": query},
            timeout=60
        )

        print("STATUS:", response.status_code)

        if response.status_code != 200:
            print("ERROR RESPONSE:")
            print(response.text)
            return {"elements": []}

        try:
            return response.json()
        except Exception:
            print("INVALID JSON:")
            print(response.text)
            return {"elements": []}

    except Exception as e:
        print("REQUEST ERROR:", e)
        return {"elements": []}


def fetch_buildings():
    query = """
    [out:json][timeout:25];

    (
      way["building"](55.75,37.80,55.85,37.95);
      way["building:part"](55.75,37.80,55.85,37.95);
      relation["building"](55.75,37.80,55.85,37.95);
    );

    out geom;
    """
    return safe_request(query)


def fetch_roads():
    query = """
    [out:json][timeout:25];

    (
      way["highway"](55.75,37.80,55.85,37.95);
    );

    out geom;
    """
    return safe_request(query)