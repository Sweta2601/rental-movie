# rental-movie

A RESTful API built with Flask and SQLAlchemy for managing a movie rental system. This project allows for the management of content providers, movies, users, rentals, and movie ratings.

## Features

- **Providers**: Create and list movie providers.
- **Users**: Register and manage user accounts.
- **Movies**: Add new movies and browse the catalog.
- **Rentals**: Checkout and return movies, view rental history.
- **Ratings**: Add and view ratings/reviews for movies.
- **Bulk Data Loading**: Utility script to efficiently load data from CSV files.

## Tech Stack

- **Language**: Python 3
- **Framework**: Flask
- **ORM**: SQLAlchemy
- **Database**: MySQL

## Setup & Installation

1. **Install Dependencies**
   ```bash
   pip install flask sqlalchemy mysqlclient
   ```

2. **Configuration**
   Configure your database connection settings in `config.py`.

3. **Load Initial Data**
   ```bash
   python scripts/load_csv_data.py
   ```

## API Endpoints

### Providers

- **Create Provider**
  - `POST /providers`
- **List Providers**
  - `GET /providers` (Optional query param: `?name=` to filter by name)
- **Get Provider Details**
  - `GET /providers/<id>` (Returns provider details and their list of movies)

### Users

- **Register User**
  - `POST /users`
- **List Users**
  - `GET /users` (Optional query param: `?name=` to filter by name)
- **Get User Details**
  - `GET /users/<id>`

### Movies

- **Add Movie**
  - `POST /movies`
- **List Movies**
  - `GET /movies` (Optional query param: `?search=` to filter by title)
- **Get Movie Details**
  - `GET /movies/<id>`

### Rentals

- **Checkout Movie**
  - `POST /rentals/checkout`
  - Body: `{"user_id": <int>, "movie_id": <int>, "provider_id": <int>, "price": <float>}`
- **Return Movie**
  - `POST /rentals/return/<rental_id>`
  - Returns: Late fee and total price details.
- **List All Rentals**
  - `GET /rentals`
- **Get Rental Details**
  - `GET /rentals/<rental_id>`
- **Get Rentals by User**
  - `GET /rentals/user/<user_id>`
- **Get Rentals by Movie**
  - `GET /rentals/movie/<movie_id>`

### Ratings

- **Add Rating**
  - `POST /movies/<movie_id>/ratings`
  - Body: `{"user_id": <int>, "rating": <int>, "review": "<string>"}`
- **Get Movie Ratings**
  - `GET /movies/<movie_id>/ratings`
