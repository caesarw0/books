# Django REST API Book Project

## Description

This repository houses a Django RESTful API project designed for the retrieval of book-related data. Leveraging Django and the Django REST Framework, the API facilitates common CRUD (Create, Read, Update, Delete) operations, allowing users to interact with and manage book information through well-defined endpoints. The project provides a structured and scalable foundation for building applications that require book-related functionalities.

## Requirements

- Python 3.10.8
- Django 3.2.22
- Django REST Framework

## Installation

1. Clone the repository:

```bash
git clone https://github.com/caesarw0/books.git
```

2. Navigate to the `books` directory:

```bash
cd books
```

3. Install the required dependencies:
    
```bash
pip install -r requirements.txt
```

## Launch
Once the dependencies are installed, follow these steps to run the server for this API:

1. Apply database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

2. Load initial data into the database:

```bash
python manage.py loaddata initial_data.json
```

3. Run the development server:

```bash
python manage.py runserver
```

Alternatively, you can use the provided script to run all Django commands at once:

```python
python run_commands.py
```

## Deployment

This API endpoint is deployed on [render.com](https://render.com/) and is hosted on a web service.

The build command is:

```python
pip install -r requirements.txt
```

Since we are using the free-tier services, we are only allowed to write a single command for the start command. We encapsulate all the Django commands in a single Python script:

```python
python run_commands.py
```

This API endpoint is available at [https://caesar-library-api.onrender.com/books/list/](https://caesar-library-api.onrender.com/books/list/).

## API Endpoints

In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using HTTP methods (GET, POST, PUT, DELETE). Endpoints should be logically organized around collections and elements, both of which are resources.

| Endpoint       | HTTP Method | CRUD Method | Result              |
| -------------- | ----------- | ----------- | ------------------- |
| `books/list/`  | GET         | READ        | Get all books       |
| `books/`       | POST        | CREATE      | Create a new book   |
| `books/:id`    | GET         | READ        | Get a target book   |
| `books/:id`    | PUT         | UPDATE      | Update a target book|
| `books/:id`    | DELETE      | DELETE      | Delete a target book|

## API Usage

The following endpoints are available for interacting with the Book API:

### Get a List of All Books

To retrieve a list of all books, make a GET request to the following endpoint:

```bash
GET https://caesar-library-api.onrender.com/books/list/
```

Response:

```JSON
[
    {
        "id": 1,
        "description": "This book is called The Lion, the Witch, and the Wardrobe, it's 208 pages long.",
        "title": "The Lion, the Witch, and the Wardrobe",
        "number_of_pages": 208,
        "publish_date": "1950-01-01",
        "quantity": 10
    },
    {
        "id": 2,
        "description": "This book is called The Last Wish, it's 288 pages long.",
        "title": "The Last Wish",
        "number_of_pages": 288,
        "publish_date": "1993-01-01",
        "quantity": 20
    }
]
```

### Create a New Book

To create a new book, make a POST request to the following endpoint:

```bash
POST https://caesar-library-api.onrender.com/books/
```

Include the following JSON as the input in the request body:

```JSON
{
  "title": "The Lord of the Rings",
  "number_of_pages": 9250,
  "publish_date": "1986-01-01",
  "quantity": 20
}
```

### Get a Specific Book

To retrieve details of a specific book, make a GET request to the following endpoint:

```bash
GET https://caesar-library-api.onrender.com/books/1
```

Response:

```JSON
{
    "id": 1,
    "description": "This book is called The Lion, the Witch, and the Wardrobe, it's 208 pages long.",
    "title": "The Lion, the Witch, and the Wardrobe",
    "number_of_pages": 208,
    "publish_date": "1950-01-01",
    "quantity": 10
}
```

### Update a Book

To update details of a specific book, make a PUT request to the following endpoint:

```bash
PUT https://caesar-library-api.onrender.com/books/1/
```

Include the updated data for the book in the request body.

```JSON
{
    "title": "The Lion, the Witch, and the Wardrobe (2nd edition)",
    "number_of_pages": 250,
    "publish_date": "2023-01-01",
    "quantity": 30
}
```

### Delete a Book

To delete a specific book, make a DELETE request to the following endpoint:

```bash
DELETE https://caesar-library-api.onrender.com/books/3/
```

Note that, the initial books with id = 1 and id = 2 is not allowed to delete.

Please refer to the [API Endpoints](#API Endpoints) section for a more detailed overview of available CRUD operations.
