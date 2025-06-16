# CAMO Basic

This example provides a minimal FastAPI backend with a simple HTML frontend.

## Backend

- `backend/app/main.py` - FastAPI application exposing REST endpoints.
- `backend/app/models.py` - SQLAlchemy models.

Start the API with:

```bash
uvicorn backend.app.main:app --reload
```

Set `DATABASE_URL` to connect to PostgreSQL.

## Frontend

Static files are in `frontend/`.
Open `frontend/index.html` in a browser.
