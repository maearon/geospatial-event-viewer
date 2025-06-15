# Geospatial Event Viewer

A fullstack web application to visualize geospatial intelligence events on an interactive map.  
Built as a take-home assignment for the Fullstack Developer role at Aetosky.

---

## 🗺️ Features

- Interactive world map using **MapboxGL**
- Backend API built with **Django** and SQLite
- Frontend app built with **Vue 3** + **Vuetify**
- Mock event data imported from `events.json`
- Clickable markers with popups
- Event list syncs with map and vice versa
- [Bonus] Severity filtering and marker styling
- Dockerized backend & frontend

---

## 📸 Screenshots

![thumbnail 7](https://github.com/maearon/geospatial-event-viewer/blob/main/backend/Screenshot%20From%202025-06-13%2020-20-02.png)

---

## 🏗️ Tech Stack

- **Frontend**: Vue 3, Vuetify, Pinia, MapboxGL
- **Backend**: Django, Django REST Framework
- **Database**: SQLite (default), can be swapped for PostgreSQL
- **Dev Tools**: Docker, Axios, Toastification

---

## 📁 Project Structure

```bash
geospatial-event-viewer/
├── backend/
│   ├── events/
│   ├── scripts/
│   │   ├── events.json
│   │   └── load_events.py
│   ├── manage.py
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── App.vue
│   │   ├── main.ts
│   │   └── views/
│   │       └── Home.vue
│   └── package.json
├── docker-compose.yml
└── README.md
```

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.10+
- Node.js 18+
- Mapbox token in `.env` or `import.meta.env.VITE_MAPBOX_TOKEN`
- (Optional) Docker & Docker Compose

---

## 🐍 Backend Setup (Django)

```bash
cd backend
python -m venv venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\activate        # Linux: source venv/bin/activate
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Load mock data (2 options below):
# Option 1: Using Django fixture
python manage.py loaddata scripts/events.json

# Option 2: Using custom script
python scripts/load_events.py

# Run dev server
python manage.py runserver
```

> API available at: http://localhost:8000/api/events/

---

## 🌐 Frontend Setup (Vue 3)

```bash
cd frontend
npm install
npm run dev
```

> Frontend available at: http://localhost:5173/

---

## 🐳 Dockerized Setup (Optional)

```bash
docker-compose up --build
```

- Frontend: http://localhost:5173  
- Backend API: http://localhost:8000/api/events/

---

## ✅ API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/events/` | Get all events |
| GET | `/api/events?severity=high` | Filter by severity |

Example Response:

```json
[
  {
    "id": 1,
    "timestamp": "2025-06-10T14:32:00Z",
    "latitude": 21.0278,
    "longitude": 105.8342,
    "severity": "high",
    "description": "Unauthorized drone activity detected."
  }
]
```

---

## 🧪 Development Tips

### 🔍 Useful Shell Commands

```bash
# List project structure
tree . -I "node_modules|__pycache__|.git|venv"

# Check environment variables
printenv | grep MAPBOX

# Run custom data script
python scripts/load_events.py
```

> Nếu `tree` chưa được cài:
```bash
sudo apt update && sudo apt install tree
```

---

## ⚙️ Design Decisions

- 🗺️ Chose MapboxGL for dynamic map and marker performance
- 🧠 Used Vue 3 + Composition API + Pinia for state logic
- 🔄 Marker popups sync with event list
- 📦 Docker ensures consistent setup across machines

---

## 🧠 Challenges Faced

- Syncing card clicks with marker fly-to
- Dynamically resizing map after load
- Styling markers and popups to match severity
- CORS and HTTP configs for frontend/backend integration

---

## 📬 Submission

This project is submitted as part of the Fullstack Developer Take-Home Assessment for **Aetosky**.

---

## 📄 License

This project is for **evaluation/demo purposes only**. Not intended for production or commercial use.
