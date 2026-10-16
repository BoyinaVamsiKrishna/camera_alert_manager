# Camera Alert Manager

A Python FastAPI project that validates, stores, retrieves, updates, and deletes camera URLs using Redis.

## Technologies and Concepts Used

- Python: Regular expressions (`re.fullmatch`, `re.search`), conditional statements, functions, and string handling.
- FastAPI: REST API endpoints, HTTP methods, path parameters, query parameters, and JSON responses.
- Redis: Hash operations using `HSET`, `HGET`, `HGETALL`, `HEXISTS`, and `HDEL`.
- URL Validation: Validates camera URLs in the format `https://example.com/camera1`.

## API Documentation

### 1. List All Camera URLs
- Method: `GET`
- Endpoint: `/camera/url/list/`
- Input: No parameters.
- Output: Returns all camera IDs and their URLs.
- Redis: `HGETALL`

### 2. Get a Camera URL
- Method: `GET`
- Endpoint: `/camera/url/get/{cam_id}`
- Input: Path parameter — `cam_id` (e.g., `camera1`).
- Output: Returns the URL associated with the specified camera.
- Redis: `HGET`

### 3. Store a Camera URL
- Method: `POST`
- Endpoint: `/camera/url/store`
- Input: Query parameter — `url` (e.g., `https://example.com/camera1`).
- Processing: Validates the URL using regex and extracts the camera ID.
- Output: Returns the camera ID and stored URL, or a message if the URL is invalid.
- Redis: `HSET`, `HGET`

### 4. Update a Camera URL
- Method: `PUT`
- Endpoint: `/camera/url/update/{cam_id}`
- Input: Path parameter — `cam_id`; query parameter — `url` containing the new URL.
- Processing: Checks whether the camera_id exists, validates the new URL, and updates the existing entry.
- Output: Returns the camera ID and updated URL when successful.
- Redis: `HEXISTS`, `HSET`, `HGET`

### 5. Delete a Camera URL
- Method: `DELETE`
- Endpoint: `/camera/url/delete`
- Input: Query parameter — `cam_id` (e.g., `camera1`).
- Output: Returns HTTP `204 No Content` when the request completes.
- Redis: `HDEL`

## Run the Application

```bash
uvicorn app.main:app --reload
```

Interactive API documentation: `http://127.0.0.1:8000/docs`

Note: This project uses Redis as its data store and does not require a traditional database.