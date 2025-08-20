
## SuperTask app:
- application for managing a task list with user authentication

### The project includes:
- FastAPI
- SQLAlchemy 2
- Alembic
- PostreSQL
- Nuxt3
- Docker
- Feature Based Project Structure like Django's

## How to use this starter

+ git clone -b zadanie2-problem https://github.com/marcin86junior/FastAPI-minimum.git .
+ .env.template -> .env

Docker for backend: (front still not dockerized correctly)
+ docker-compose up --build
+ run again if its first time "docker-compose up --build" 
+ http://127.0.0.1:8000/docs#/

Frontend:
+ cd frontend
+ npm install nuxt
+ npm run dev
+ http://localhost:3000/

## Problem hydration error w komponencie Vue


Problem hydration error w komponencie Vue

Problem z podanym kodem polega na niezgodności między tym, co renderuje serwer (SSR), a tym, co generuje JavaScript po stronie klienta. Główne problemy:  

## Różne wartości czasu: 

currentTime i onlineTime są inicjalizowane z new Date().toLocaleTimeString()

Czas po stronie serwera będzie inny niż czas, gdy kod uruchomi się ponownie w przeglądarce

Powoduje to niezgodność HTML z serwera i klienta

## Dostęp do danych zadań:

Composable useTasks() może zwracać różne dane na serwerze i kliencie

Wartości completedTasks i totalTasks mogą się różnić
