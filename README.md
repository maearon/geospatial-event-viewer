# Geospatial Event Viewer

A fullstack web application to visualize geospatial intelligence events on an interactive map. Built as a take-home assignment for the Fullstack Developer role at Aetosky.

## 🗺️ Features

- Interactive world map using **MapboxGL**
- Backend API built with **Django** and SQLite
- Frontend app built with **Vue.js**
- Fetches and displays mock event data from a JSON file
- Clickable markers showing event details
- [Bonus] Filter events by severity
- [Bonus] Severity-based marker styling
- [Bonus] Dockerized backend and frontend

---

## 📸 Screenshots

> *(Add screenshots here if available, such as full map UI and popup details)*

---

## 🏗️ Tech Stack

- **Frontend**: Vue.js, MapboxGL
- **Backend**: Django (Python), SQLite
- **Containerization**: Docker, Docker Compose

---

## 📂 Project Structure

geospatial-event-viewer/
├── backend/
│ ├── manage.py
│ ├── events/
│ ├── events.json
│ └── Dockerfile
├── frontend/
│ ├── src/
│ ├── public/
│ └── Dockerfile
├── docker-compose.yml
└── README.md

```

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.10+
- Node.js 18+
- (Optional) Docker & Docker Compose

---

### 🐍 Backend (Django)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

# Load mock data into DB (optional if using fixtures)
python manage.py migrate
python manage.py loaddata events.json

# Run server
python manage.py runserver
```
API available at: http://localhost:8000/api/events

🌐 Frontend (Vue.js)
```
cd frontend
npm install
npm run dev
```
Frontend available at: http://localhost:5173

🐳 Docker Setup (Optional)
```
docker-compose up --build
```
Frontend: http://localhost:5173

Backend API: http://localhost:8000/api/events

✅ API Endpoints
GET /api/events: Returns list of all events

GET /api/events?severity=high: [Bonus] Filter by severity (high, medium, low)

Example Response:

```
[
  {
    "id": 1,
    "timestamp": "2025-06-10T14:32:00Z",
    "latitude": 21.0278,
    "longitude": 105.8342,
    "severity": "high",
    "description": "Unauthorized drone activity detected."
  },
  ...
]
```
⚙️ Design Decisions
Chose MapboxGL for smooth, responsive map rendering.

Used Vue 3 Composition API for cleaner logic separation.

Event filtering done both client-side and server-side for flexibility.

Dockerized setup to simplify cross-environment development.

🧠 Challenges Faced
Aligning map rendering with real-time API data.

Managing reactive state between filters and markers.

Ensuring cross-origin API calls worked correctly in local dev.

📬 Submission
This project is submitted as part of the Fullstack Developer Take-Home Assessment for Aetosky.

📄 License
This project is for evaluation purposes only and is not intended for commercial use.