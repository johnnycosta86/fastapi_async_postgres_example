from fastapi import FastAPI
import uvicorn
from app.src.api.api_v1.api import api_router
from app.src.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)