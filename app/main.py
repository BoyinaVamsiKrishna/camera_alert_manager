from fastapi import FastAPI
from redis import RedisError
from app.config.redis_config import redis_client
from app.routers.camera import camera_router
app = FastAPI()
app.include_router(camera_router)
@app.get('/')
def redis_home():
    try:
        status = redis_client.ping()
        if status: 
            return {"message": "Redis project running successfully" }
    except RedisError:
         return {"message": "Error in establishing connection with redis"}