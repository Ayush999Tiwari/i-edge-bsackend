from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from ..database import get_db
from ..models import User
from ..schemas import UserLogin, Token, UserData
from ..auth import verify_password, create_access_token

router = APIRouter(prefix="/api/v1/auth", tags=["Authentication"])

@router.post("/login", response_model=Token)
async def login(credentials: UserLogin, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.email == credentials.email))
    user = result.scalar_one_or_none()
    
    if not user or not verify_password(credentials.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    token_data = {
        "sub": user.email, 
        "id": user.id, 
        "services": user.services_access
    }
    access_token = create_access_token(data=token_data)
    
    return {"access_token": access_token}