
## SuperTasks - an application for managing a task list with user authentication.

### The project includes:
- FastAPI
- SQLAlchemy 2
- Alembic
- PostreSQL
- Nuxt3
- Docker
- Type Safe Environment Variables
- Feature Based Project Structure like Django's

This is a starter template for creating API's with FastAPI, SQLAlchemy 2, Alembic and Postgresql

The project has env setup. You can view how the config works inside the `/core/config.py` directory, adding new env variables is trivial.

The project is also has a feature based architecture setup for you so that you have a clear idea on how to continue building and adding new features.

## How to use this starter

Docker for backend: (front still not dockerized correctly)
+ docker-compose up --build

Front:
+ npm run dev
