# Shapes API

A RESTful API for managing geometric shapes — create, read, update, and delete circles, squares, and rectangles. Built with **FastAPI** and persisted to a local JSON file.

---

## Features

- Full CRUD operations on geometric shapes
- Supports **Circle**, **Square**, and **Rectangle**
- Auto-incremented shape IDs
- Per-shape logging to dedicated log files
- JSON file-based persistence (no database required)
- Auto-generated interactive docs via FastAPI (`/docs`)

---

## Project Structure

```
shapes_project_kodkod/
├── server.py          # FastAPI app — all HTTP endpoints
├── shape_manager.py   # Business logic layer (CRUD + persistence)
├── shape.py           # Abstract base class for shapes
├── circle.py          # Circle shape implementation
├── square.py          # Square shape implementation
├── rectangle.py       # Rectangle shape implementation
├── logger.py          # Logging factory
├── shapes.json        # Persistent shape storage
└── *.log              # Per-shape log files
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- `fastapi` and `uvicorn`

### Install dependencies

```bash
pip install fastapi uvicorn
```

### Run the server

```bash
uvicorn server:app --reload
```

The API will be available at `http://127.0.0.1:8000`.  
Interactive docs: `http://127.0.0.1:8000/docs`

---

## API Reference

### Create a Shape
```
POST /shapes
```
**Body:**
```json
{
  "shape_type": "circle",
  "length_radius": 5,
  "width": null
}
```
| Field | Type | Required | Description |
|---|---|---|---|
| `shape_type` | `string` | Yes | `"circle"`, `"square"`, or `"rectangle"` |
| `length_radius` | `int` | Yes | Radius (circle) or side length (square/rectangle) |
| `width` | `int` | No | Required for `rectangle` only |

**Response `201`:**
```json
{ "shape id": 1 }
```

---

### Get All Shapes
```
GET /shapes/
```
**Response `200`:**
```json
{
  "message": {
    "1": { "shape type": "circle", "radius": 5 },
    "2": { "shape type": "square", "length": 4 },
    "3": { "shape type": "rectangle", "length": 6, "width": 3 }
  }
}
```

---

### Get Shape by ID
```
GET /shapes/{id}
```
**Response `200`:**
```json
{ "message": { "id": 1, "type": "circle", "length/radius": 5 } }
```

---

### Get Shapes by Type
```
GET /shapes/type/{type}
```
`type` must be `circle`, `square`, or `rectangle`.

---

### Get Total Area
```
GET /shapes/total-area
```
**Response `200`:**
```json
{ "message": "78.54" }
```

---

### Get Shape Count
```
GET /shapes/count
```
**Response `200`:**
```json
{ "message": "there are: 3 shapes in total." }
```

---

### Update a Shape
```
PUT /shapes/{id}
```
**Body:**
```json
{
  "length_or_radius": 10,
  "width": 5
}
```
`width` is required only for rectangles.

---

### Delete a Shape
```
DELETE /shapes/{id}
```
**Response `200`:**
```json
{ "message": "shape deleted successfuly" }
```

---

## Shape Geometry

| Shape | Area | Perimeter |
|---|---|---|
| Circle | `π × r²` | `2 × π × r` |
| Square | `l²` | `4 × l` |
| Rectangle | `l × w` | `2l + 2w` |

---

## Logging

Each shape type writes events to its own log file:

| Logger | File |
|---|---|
| ShapeManager | `shape_logger_logs.log` |
| Circle | `circle_logger_logs.log` |
| Square | `square_logger_logs.log` |
| Rectangle | `rectangle_logger_logs.log` |

Log entries follow the format:
```
YYYY-MM-DD HH:MM:SS,ms, <logger_name>, <LEVEL>, <message>
```
