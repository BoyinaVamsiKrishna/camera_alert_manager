from fastapi import APIRouter
from re import fullmatch, search
from app.config.redis_config import redis_client
camera_router = APIRouter()
@camera_router.get('/camera/url/list/')
def get_cam_urls():
    result = redis_client.hgetall('camera:id')
    return result

@camera_router.get('/camera/url/get/{cam_id:str}')
def get_cam_urls(cam_id: str):
    result = redis_client.hget('camera:id', cam_id)
    return {cam_id: result}

@camera_router.post('/camera/url/store')
def store_cam_url(url: str):
    result = bool(fullmatch(r'https://example\.com/camera\d+', url))
    if result:
        cam_id = search(r'\d+', url)
        redis_client.hset('camera:id', f"camera{cam_id.group()}", url)
        output = redis_client.hget('camera:id', f"camera{cam_id.group()}")
        return {f"camera{cam_id.group()}": output}
    else:
        return {"message": "Not a valid url"}



@camera_router.put('/camera/url/update/{cam_id:str}')
def get_cam_urls(cam_id: str, url):
    cam_status = redis_client.hexists('camera:id', cam_id)
    if bool(cam_status):
        result = bool(fullmatch(r'https://example\.com/camera\d+', url))
        if result:
            redis_client.hset('camera:id', cam_id, url)
            output = redis_client.hget('camera:id', cam_id)
            return {cam_id: output}
        else:
            return {"message": "Not a valid url"}

@camera_router.delete('/camera/url/delete', status_code=204)
def delete_cam_url(cam_id: str):
    redis_client.hdel('camera:id', cam_id)
