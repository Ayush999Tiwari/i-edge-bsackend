from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routers import auth

app = FastAPI(title="i-Edge Enterprise API", version="2.0")

# ✅ HARDCODED ORIGINS - NO DYNAMIC CONFIG TO AVOID CACHING ISSUES
origins = [
    "http://localhost:5173",
    "https://i-edge-frontend-as9p.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/")
def read_root():
    return {"message": "i-Edge API is running"}