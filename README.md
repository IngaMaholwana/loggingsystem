# README.md

# Logging System

This project is a FastAPI application designed to manage user authentication and provide user-related functionalities. It follows a modular architecture, separating concerns into different components for better maintainability and scalability.

## Project Structure

- **app/**: Contains the main application code.
  - **api/**: Contains the API endpoints.
    - **endpoints/**: Individual files for different API functionalities.
      - **auth.py**: Authentication-related endpoints (login).
      - **users.py**: User-related endpoints (retrieve current user, list users).
  - **core/**: Core functionalities and configurations.
    - **config.py**: Configuration settings for the application.
    - **security.py**: Security-related functions (password hashing, token creation).
  - **db/**: Database-related code.
    - **base.py**: Base model for the database.
    - **session.py**: Database session management.
  - **models/**: Database models.
    - **user.py**: User model definition.
  - **repositories/**: Data access layer.
    - **user_repository.py**: User repository for database interactions.
  - **schemas/**: Pydantic models for data validation and serialization.
    - **user.py**: User schema definition.
  - **services/**: Business logic layer.
    - **user_service.py**: User service for handling user operations.
  - **middlewares/**: Middleware components.
    - **timing_middleware.py**: Middleware for tracking request processing time.
  - **main.py**: Entry point of the application.

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Usage

To start the application, run:

```
uvicorn app.main:app --reload
```

This will start the FastAPI application in development mode.

## API Endpoints

- **POST /token**: Authenticate a user and return a JWT token.
- **GET /users/me**: Retrieve the current authenticated user's information.
- **GET /admin/users/**: List users (admin access required).

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License.