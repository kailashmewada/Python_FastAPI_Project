from fastapi import APIRouter
from app.controllers.auth import user_response, signup, login, get_user, forget_password, reset_password
from app.model.user_model import UserCreateRequest, User,UserLoginRequest  # ✅ Import your models


router = APIRouter()

@router.post("/signup", response_model=dict)
async def create_user(user: UserCreateRequest):
    """
    Create a new user account.
    """
    return await signup(user)

@router.post("/login", response_model=dict)
async def user_login(user: UserLoginRequest):
    """
    User login endpoint.
    """
    return await login(user)

@router.get("/user/{username}", response_model=dict)
async def read_user(username: str):
    """
    Get user details by username.
    """
    return await get_user(username)

@router.post("/forget-password", response_model=dict)
async def forget_password_endpoint(token: str) -> dict:
    """
    Endpoint to handle forget password functionality.
    """
    return await forget_password(token)

@router.post("/reset-password", response_model=dict)
async def reset_password_endpoint(token:str, new_password: str) -> dict:
    """
    Endpoint to reset the user's password.
    """
    return await reset_password(token, new_password)

@router.get('/', response_model=dict)
async def health_check() -> dict:
    """
    Health check endpoint to verify if the service is running.
    """
    return {"status": "ok", "message": "Service is running"}