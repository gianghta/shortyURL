import logging

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.db.database import SessionLocal, engine
from app.models.models import Base
from app.api import url

Base.metadata.create_all(bind=engine)

log = logging.getLogger(__name__)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(url.router)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
    )

    return application

app = create_application()

@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")

@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")