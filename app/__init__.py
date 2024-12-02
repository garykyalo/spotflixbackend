from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import router as app_router


origins = [
    "http://localhost:5173",
    "https://academy.garrytek.com"
]

def create_app() -> FastAPI:
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware, 
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"]
    )



    app.include_router(app_router)

    return app
