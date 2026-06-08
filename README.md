# 🚀 Intelligent Route Planner Using Graph Algorithms

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![React](https://img.shields.io/badge/React-Frontend-61DAFB)
![OpenStreetMap](https://img.shields.io/badge/OpenStreetMap-Geospatial-orange)
![Graph Algorithms](https://img.shields.io/badge/Algorithms-Dijkstra%20%7C%20A*%20%7C%20BFS%20%7C%20DFS%20%7C%20Yen's-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

### Real-Time Route Optimization and Navigation System Using Graph Algorithms, FastAPI, React and OpenStreetMap

</div>

---

## 📌 Overview

Intelligent Route Planner Using Graph Algorithms is a full-stack route optimization platform that leverages real-world road network data from OpenStreetMap to calculate efficient travel routes between locations.

The system integrates advanced graph algorithms, geospatial processing, traffic estimation, fuel cost prediction, and interactive route visualization to provide optimized navigation and route analytics.

---

## ✨ Features

### 🗺 Route Planning

* Real-world OpenStreetMap road network
* Source and destination search
* Route optimization
* Interactive route visualization

### ⚡ Graph Algorithms

* Dijkstra's Algorithm
* A* Search Algorithm
* Breadth First Search (BFS)
* Depth First Search (DFS)
* Yen’s K-Shortest Path Algorithm

### 🚦 Traffic Analysis

* Traffic-aware ETA prediction
* Route congestion simulation
* Alternative route exploration
* Route efficiency analysis

### ⛽ Fuel Cost Estimation

* Distance-based fuel calculation
* Travel expense prediction
* Fuel cost estimation in INR

### 📊 Route Analytics

* Total distance
* Estimated travel time
* Traffic-adjusted ETA
* Fuel cost analysis
* Path node statistics

### 📜 Search History

* Recent route searches
* Local storage persistence
* Quick route lookup

### 🌐 REST API

* FastAPI backend
* Swagger documentation
* JSON responses
* Health monitoring endpoint

---

## 🏗 System Architecture

![Architecture](project-assets/architecture/architecture.png)

---

## 📸 Project Screenshots

### Homepage

![Homepage](project-assets/screenshots/homepage.png)

### Route Result

![Route Result](project-assets/screenshots/route_result.png)

### Route History

![Route History](project-assets/screenshots/route_history.png)

### Interactive Route Map

![Route Map](project-assets/screenshots/route_map.png)

### Swagger API Documentation

![Swagger Docs](project-assets/screenshots/swagger_docs.png)

---

## 🛠 Tech Stack

### Frontend

* React.js
* Vite
* Tailwind CSS
* Axios
* Leaflet

### Backend

* FastAPI
* Uvicorn

### Geospatial Processing

* OpenStreetMap
* OSMnx
* NetworkX
* Geopy

### Algorithms

* Dijkstra Algorithm
* A* Search Algorithm
* BFS
* DFS
* Yen’s Algorithm

### Languages

* Python
* JavaScript

---

## 📂 Project Structure

```text
Intelligent-Route-Planner-Using-Graph-Algorithms
│
├── api/
├── frontend/
├── src/
├── data/
├── outputs/
│
├── images/
│
├── project-assets/
│   ├── architecture/
│   └── screenshots/
│
├── requirements.txt
├── README.md
├── LICENSE
├── render.yaml
└── .gitignore
```

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/VaishnavaDevi-R/Intelligent-Route-Planner-Using-Graph-Algorithms.git

cd Intelligent-Route-Planner-Using-Graph-Algorithms
```

### Backend Setup

```bash
python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

### Run Backend

```bash
uvicorn api.app:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

### Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

---

## 📡 API Endpoint

### Route Calculation

```http
GET /route
```

### Example Request

```http
GET /route?source=Meenakshi Amman Temple, Madurai&destination=Madurai Junction Railway Station
```

### Sample Response

```json
{
  "source": "Meenakshi Amman Temple, Madurai",
  "destination": "Madurai Junction Railway Station",
  "distance_km": 1.7,
  "eta_minutes": 3.41,
  "traffic_eta_minutes": 4.43,
  "fuel_cost": 4.34,
  "path_nodes": 24
}
```

---

## 🎯 Future Enhancements

* Live Traffic API Integration
* Multi-City Support
* Route Sharing
* Voice Navigation
* Mobile Application
* AI-Based Route Prediction
* User Authentication
* Saved Routes

---

## 📚 Learning Outcomes

* Graph Theory Fundamentals
* Route Optimization Techniques
* Geospatial Data Processing
* OpenStreetMap Integration
* FastAPI Backend Development
* React Frontend Development
* REST API Design
* Full Stack Development

---

## 👩‍💻 Author

**Vaishnava Devi**

---

## ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the repository

📢 Share the project

---

## 📄 License

This project is licensed under the MIT License.

---

<div align="center">

### 🚀 Building Smarter Navigation Systems with Graph Algorithms

</div>
