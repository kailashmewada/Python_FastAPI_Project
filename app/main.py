from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.urls import router as auth_router


app = FastAPI()
# CORS configuration

app.add_middleware( CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])

# Include the authentication router
app.include_router(auth_router, prefix="/api/v1/auth", tags=["auth"])