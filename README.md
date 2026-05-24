
# Vector Spatial Data Collection System

Система сбора, обработки и визуализации векторных пространственных данных.

## Возможности

- Сбор данных из OpenStreetMap через Overpass API
- Обработка GeoJSON
- Хранение в PostgreSQL/PostGIS
- REST API на Flask
- Веб-карта на Leaflet
- Docker Compose

## Архитектура

OpenStreetMap API -> Collector -> Processor -> PostgreSQL/PostGIS -> Flask API -> Leaflet Frontend

## Запуск

```bash
docker-compose up --build
```

Наполеннеие БД:
- http://localhost:5000/init

API:
- http://localhost:5000/api/buildings
- http://localhost:5000/api/roads

Frontend:
- http://localhost:5000
