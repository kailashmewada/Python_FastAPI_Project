from app.model.user_model import User, UserCreateRequest, UserUpdateRequest, UserResponse
from app.core.security import create_access_token, verify_password, hash_password, decode_token
from fastapi import APIRouter, Depends, HTTPException, status
from app.database.db import users_collection
from fastapi.security import OAuth2PasswordBearer
import re


def user_response(user)->dict:
    data = {
        "username": user["username"],
        "email": user["email"],
        "full_name": user.get("full_name"),
        "is_active": user.get("is_active", True)
    }
    
    return (
            {
            "status": "success",
            "data": data,
            "message": "User retrieved successfully"
        })


async def signup(user: UserCreateRequest):
    if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", user.email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid email format")
    
    existing_user = await users_collection.find_one({"username": user.username, "email": user.email})
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")
    
    hashed_password = hash_password(user.password)
    new_user = {
        "username": user.username,
        "email": user.email,
        "full_name": user.full_name,
        "password": hashed_password,
        "is_active": True
    }
    
    await users_collection.insert_one(new_user)
    
    return {
        "status": "success",
        "message": "User created successfully"
    }
async def login(user: UserCreateRequest):
    existing_user = await users_collection.find_one({"username": user.username})
    if not existing_user or not verify_password(user.password, existing_user["password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")
    access_token = create_access_token(data={"sub": existing_user["username"]})
    return {
        "status": "success",
        "access_token": access_token,
        "token_type": "bearer",
        "message": "Login successful",
        "username": existing_user["username"],
        "email": existing_user["email"],
        "is_active": existing_user.get("is_active", True)   
    }

async def get_user(username: str):
    user = await users_collection.find_one({"username": username})
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    return user_response(user)

async def update_user(username: str, user_update: UserUpdateRequest) -> dict:
    user = await users_collection.find_one({"username": username})
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    update_data = user_update.model_dump(exclude_unset=True)
    if "password" in update_data:
        update_data["password"] = hash_password(update_data["password"])
    
    await users_collection.update_one({"username": username}, {"$set": update_data})
    
    updated_user = await users_collection.find_one({"username": username})
    
    return user_response(updated_user)

async def forget_password(token:str) -> dict:
    try:
        payload = decode_token(token)
        username = payload.get("sub")
        if not username:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        
        user = await users_collection.find_one({"username": username})
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        
        token = create_access_token(data={"sub": user["username"]})
        return {
            "status": "success",
            "message": "Password reset token generated successfully",
            "token": token
        }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token") from e
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token") from e
    
async def reset_password(token: str, new_password: str) -> dict:
        try:
            payload = decode_token(token)
            username = payload.get("sub")
            if not username:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
            
            user = await users_collection.find_one({"username": username})
            if not user:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
            
            hashed_password = hash_password(new_password)
            await users_collection.update_one({"username": username}, {"$set": {"password": hashed_password}})
            
            return {
                "status": "success",
                "message": "Password reset successfully"
            }
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token") from e