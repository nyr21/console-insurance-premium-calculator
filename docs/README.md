# Insurance Premium Calculator - Documentation

Welcome to the Insurance Premium Calculator API documentation!

## 📚 Documentation Structure

```
docs/
├── FILE_EXPLANATIONS.md          # Non-technical guide to all project files
├── technical/
│   └── API_DOCUMENTATION.md      # Technical API documentation
└── adr/                          # Architecture Decision Records
    ├── README.md
    ├── 001-use-fastapi-framework.md
    └── 002-use-pydantic-validation.md
```

---

## 🎯 Quick Start

**For Non-Technical Users:**
- Start with [FILE_EXPLANATIONS.md](FILE_EXPLANATIONS.md) to understand what each file does

**For Developers:**
- Read [API_DOCUMENTATION.md](technical/API_DOCUMENTATION.md) for technical details
- Check [ADRs](adr/) to understand architectural decisions

**For Testers:**
- Import `Insurance_Premium_Calculator.postman_collection.json` into Postman
- See [API_DOCUMENTATION.md](technical/API_DOCUMENTATION.md#testing) for testing guide

---

## 📖 Documentation Files

### [FILE_EXPLANATIONS.md](FILE_EXPLANATIONS.md)
**Audience:** Non-technical stakeholders, business users, project managers

**Contents:**
- What is `__pycache__` and why it exists
- Purpose of `requirements.txt`
- Understanding `openapi.json`
- How `export_openapi.py` works
- Using the Postman collection
- Real-world analogies for each file

### [technical/API_DOCUMENTATION.md](technical/API_DOCUMENTATION.md)
**Audience:** Developers, technical leads, DevOps engineers

**Contents:**
- API architecture and technology stack
- Endpoint specifications (GET /, GET /health, POST /calculate)
- Data models (PremiumRequest, PremiumResponse)
- Business logic and calculation formulas
- Error handling and validation
- Development setup and deployment
- Testing strategies
- Performance benchmarks

### [adr/](adr/)
**Audience:** Architects, technical decision makers, senior developers

**Contents:**
- ADR 001: Why we chose FastAPI
- ADR 002: Why we use Pydantic for validation
- Decision context, rationale, and consequences
- Alternatives considered

---

## 🚀 Getting Started

### 1. Installation
```bash
pip install -r requirements.txt
```

### 2. Run the Server
```bash
uvicorn main:app --reload
```

### 3. Access Documentation
- **Interactive API Docs:** http://localhost:8000/docs
- **Alternative Docs:** http://localhost:8000/redoc
- **OpenAPI Schema:** http://localhost:8000/openapi.json

### 4. Test the API
Import `Insurance_Premium_Calculator.postman_collection.json` into Postman

---

## 📋 Project Files Overview

| File | Purpose | Audience |
|------|---------|----------|
| `main.py` | Main API application | Developers |
| `requirements.txt` | Python dependencies | Developers, DevOps |
| `export_openapi.py` | Generate API schema | Developers |
| `openapi.json` | API specification | All (machine-readable) |
| `Insurance_Premium_Calculator.postman_collection.json` | Test collection | Testers, Developers |
| `__pycache__/` | Python cache (auto-generated) | N/A (ignore) |

---

## 🔗 Quick Links

- **API Docs:** [technical/API_DOCUMENTATION.md](technical/API_DOCUMENTATION.md)
- **File Guide:** [FILE_EXPLANATIONS.md](FILE_EXPLANATIONS.md)
- **Architecture Decisions:** [adr/](adr/)
- **Interactive Swagger UI:** http://localhost:8000/docs (when server is running)

---

## 📝 Contributing

When making changes to the project:

1. **Update documentation** if you change APIs or architecture
2. **Create ADRs** for significant architectural decisions
3. **Update Postman collection** if you add/modify endpoints
4. **Regenerate OpenAPI schema:** `python export_openapi.py`

---

## 🆘 Support

**For questions about:**
- **File purposes:** See [FILE_EXPLANATIONS.md](FILE_EXPLANATIONS.md)
- **API usage:** See [API_DOCUMENTATION.md](technical/API_DOCUMENTATION.md)
- **Architecture decisions:** See [adr/](adr/)

---

*Last updated: 2026-02-03*  
*Project Version: 1.0.0*
