from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from backend.api.v1.api import api_router as api_router_v1

from backend.api.v1.endpoints import tasks as task_router
from backend.db.session import engine
from backend.db.base_class import Base
import backend.models.user
import backend.models.task

app = FastAPI(
    title="HackRice 15 Starter Code",
    description="A solid foundation for your hackathon project.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health")
def health():
    return {"status": "ok"}

# Add routers
from backend.api.v1.api import api_router as api_router_v1

app.include_router(api_router_v1, prefix="/api/v1")

templates = Jinja2Templates(directory="frontend")

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Serve frontend
app.mount("/static", StaticFiles(directory="frontend/static", html=True), name="static")

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)