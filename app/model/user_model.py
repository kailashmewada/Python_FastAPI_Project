from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List

class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, description="Username of the user")
    email: EmailStr = Field(..., description="Email address of the user")
    full_name: Optional[str] = Field(default=None, max_length=100, description="Full name of the user")
    is_active: bool = Field(default=True, description="Indicates if the user is active")

class UserCreateRequest(User):
    username: str = Field(..., min_length=3, max_length=50, description="Username for the user account")
    email: EmailStr = Field(..., description="Email address for the user account")
    full_name: Optional[str] = Field(default=None, max_length=100, description="Full name of the user")
    password: str = Field(..., min_length=8, description="Password for the user account")
   

class UserUpdateRequest(BaseModel):
    full_name: Optional[str] = Field(default=None, max_length=100, description="Full name of the user")
    is_active: Optional[bool] = Field(default=None, description="Indicates if the user is active") 

class UserResponse(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    is_active: bool

    class Config:
        from_attributes = True  # Allows Pydantic to work with ORM models
        json_schema_extra = {
            "example": {
                "username": "johndoe",
                "email": "kailash.mewada@encoresky.com",
                "full_name": "John Doe",
                "is_active": True
            }
        }
class UserLoginRequest(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, description="Username for login")
    password: str = Field(..., min_length=8, description="Password for login")

class UserLoginResponse(BaseModel):
    access_token: str = Field(..., description="JWT access token for the user")
    token_type: str = Field(default="bearer", description="Type of the token, usually 'bearer'")
    username: str = Field(..., description="Username of the logged-in user")
    email: EmailStr = Field(..., description="Email address of the logged-in user")