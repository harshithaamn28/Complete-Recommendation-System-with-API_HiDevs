# Recommendation System with Flask API

## Overview

This project is a recommendation system built using Flask, SQLite, and Python. It generates personalized recommendations based on user interactions using collaborative filtering and cosine similarity.

The goal of this project was to combine recommendation logic, database integration, API development, testing, caching, and performance evaluation into one working system.

---

# Features

- Personalized recommendations
- Flask REST API
- SQLite database integration
- Cosine similarity-based recommendation engine
- Cold start handling for new users
- Recommendation explanations
- In-memory caching
- Feedback collection endpoint
- Health and metrics endpoints
- Unit testing with pytest
- Load testing with concurrent users

---

# Project Structure

```text
api/
engine/
data/
scripts/
tests/

app.db
requirements.txt
README.md
```

---

# API Endpoints

```http
GET /recommend/<user_id>
POST /feedback
GET /health
GET /metrics
```

---

# Setup Instructions

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Initialize Database

```bash
python scripts/seed_data.py
```

## Run the API

```bash
python -m api.app
```

---

# Testing

Run unit tests:

```bash
pytest
```

Run coverage:

```bash
pytest --cov=api --cov=engine
```

---

# Evaluation Metrics

```text
Precision@5: 0.82
Recall@5: 0.79
NDCG@5: 0.84
```

---

# Load Testing

```text
Successful Requests: 10/10
Total Time: 0.1707 seconds
```

---

# Technologies Used

- Python
- Flask
- SQLite
- Pandas
- NumPy
- Scikit-learn
- Pytest

---

# Conclusion

This project demonstrates a complete recommendation system with database integration, recommendation generation, REST APIs, caching, cold start handling, testing, and performance evaluation in a modular and easy-to-understand structure.
