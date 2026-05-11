# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API using the FastAPI framework. You will practice defining endpoints, working with JSON data, validating request bodies, and handling common API responses in Python.

## 📝 Tasks

### 🛠️ Create the FastAPI App and Read Endpoints

#### Description
Set up a FastAPI application for a simple inventory system. Create routes that return JSON responses and allow users to view all items or a single item by ID.

#### Requirements
Completed program should:

- Create a FastAPI app instance
- Add a root endpoint that returns a welcome message as JSON
- Add a `GET /items` endpoint that returns all items from an in-memory list
- Add a `GET /items/{item_id}` endpoint that returns one item by ID
- Return a clear error response when an item ID is not found


### 🛠️ Add Create, Update, and Delete Endpoints

#### Description
Extend the API so users can add new items, update existing items, and delete items. Use a Pydantic model to validate incoming data.

#### Requirements
Completed program should:

- Define a Pydantic model for item data
- Add a `POST /items` endpoint to create a new item
- Add a `PUT /items/{item_id}` endpoint to update an existing item
- Add a `DELETE /items/{item_id}` endpoint to remove an item
- Return appropriate JSON responses for successful and unsuccessful operations