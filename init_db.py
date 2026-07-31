import asyncio
from app.database import async_session, Base, engine
from app.models import User
from app.auth import get_password_hash

async def init():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        
    async with async_session() as db:
        existing = await db.execute(
            __import__('sqlalchemy').select(User).where(User.email == "admin@iedge.com")
        )
        if not existing.scalar_one_or_none():
            admin = User(
                email="admin@iedge.com",
                hashed_password=get_password_hash("Admin@123"),
                full_name="System Administrator",
                services_access=["egg_counting", "igrid", "surveillance", "face_rec", "body_weight", "erp_config"]
            )
            db.add(admin)
            await db.commit()
            print("✅ Admin user created successfully!")
        else:
            print("ℹ️ Admin user already exists.")

if __name__ == "__main__":
    asyncio.run(init())