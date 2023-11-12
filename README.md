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

```bash
python run_commands.py
```

## API Endpoints

In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using HTTP methods (GET, POST, PUT, DELETE). Endpoints should be logically organized around collections and elements, both of which are resources.

| Endpoint       | HTTP Method | CRUD Method | Result              |
| -------------- | ----------- | ----------- | ------------------- |
| `books/list/`  | GET         | READ        | Get all books       |
| `books/`       | POST        | CREATE      | Create a new book   |
| `books/:id`    | GET         | READ        | Get a target book   |
| `books/:id`    | PUT         | UPDATE      | Update a target book|
| `books/:id`    | DELETE      | DELETE      | Delete a target book|
