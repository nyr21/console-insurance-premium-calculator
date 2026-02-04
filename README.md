# Insurance Premium Calculator API

A FastAPI-based REST API for calculating insurance premiums based on age, risk level, and coverage amount.

## 🎯 Formula

```
Premium = Base × (1 + AgeFactor) × (1 + RiskLoading)
```

## 📚 Documentation

Comprehensive documentation is available in the [`docs/`](docs/) folder:

- **[FILE_EXPLANATIONS.md](docs/FILE_EXPLANATIONS.md)** - Non-technical guide to all project files
- **[API_DOCUMENTATION.md](docs/technical/API_DOCUMENTATION.md)** - Technical API documentation
- **[Architecture Decision Records](docs/adr/)** - Why we made specific technical choices

## 🚀 Quick Start

### Installation
```bash
pip install -r requirements.txt
```

### Run Server
```bash
uvicorn main:app --reload
```

### Access API
- **API:** http://localhost:8000
- **Interactive Docs:** http://localhost:8000/docs
- **API Schema:** http://localhost:8000/openapi.json

## 📡 API Endpoints

### POST /calculate
Calculate insurance premium

**Request:**
```json
{
  "age": 35,
  "risk_level": "medium",
  "coverage": 100000
}
```

**Response:**
```json
{
  "base_premium": 1000.0,
  "age_factor": 0.1,
  "risk_loading": 0.2,
  "final_premium": 1320.0,
  "coverage": 100000.0,
  "breakdown": "Base: $1,000.00 × (1 + 0.10) × (1 + 0.20) = $1,320.00"
}
```

## 🧪 Testing

Import `Insurance_Premium_Calculator.postman_collection.json` into Postman for 22 pre-configured test cases.

## 📁 Project Structure

```
project/
├── main.py                          # Main API application
├── requirements.txt                 # Python dependencies
├── export_openapi.py                # OpenAPI schema generator
├── openapi.json                     # Generated API specification
├── Insurance_Premium_Calculator.postman_collection.json
├── docs/                            # Documentation
│   ├── README.md
│   ├── FILE_EXPLANATIONS.md
│   ├── technical/
│   │   └── API_DOCUMENTATION.md
│   └── adr/                         # Architecture Decision Records
└── __pycache__/                     # Python cache (auto-generated)
```

## 🛠️ Tech Stack

- **FastAPI** - Modern, fast web framework
- **Pydantic** - Data validation using Python type hints
- **Uvicorn** - ASGI server

## 📖 Learn More

- [What do all these files do?](docs/FILE_EXPLANATIONS.md) (Non-technical)
- [API Technical Documentation](docs/technical/API_DOCUMENTATION.md)
- [Why FastAPI?](docs/adr/001-use-fastapi-framework.md)
- [Why Pydantic?](docs/adr/002-use-pydantic-validation.md)

---

*Version 1.0.0 | Last updated: 2026-02-03*
