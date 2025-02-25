from fastapi import FastAPI
from app.api.routes import router  # Import API router from routes.py

app = FastAPI(title="FastAPI Bulletin Board", description="A simple bulletin board API", version="1.0.0")

# Register API endpoints defined in routes.py
app.include_router(router)

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI Bulletin Board."}
