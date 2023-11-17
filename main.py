from fastapi import FastAPI
from app.api.album_routes import router as album_router

app = FastAPI()
app.include_router(album_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
