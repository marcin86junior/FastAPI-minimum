from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from core.config_loader import settings

from auth.routes.auth_router import auth_router
from user.routes.user_router import user_router
from kot.routes.kot_router import kot_router
from products.routes.products_router import product_router
from products.routes.tag_router import tag_router

openapi_tags = [
    {
        "name": "Users",
        "description": "User operations",
    },
    {
        "name": "Health Checks",
        "description": "Application health checks",
    }
]

app = FastAPI(openapi_tags=openapi_tags)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            str(origin).strip("/") for origin in settings.BACKEND_CORS_ORIGINS
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(auth_router, prefix='/api')
app.include_router(user_router, prefix='/api', tags=['Users'])
app.include_router(kot_router, prefix='/api', tags=['Koty'])
app.include_router(product_router, prefix='/api', tags=['Products'])
app.include_router(tag_router, prefix='/api', tags=['Tags'])

@app.get("/health", tags=['Health Checks'])
def read_root():
    return {"health": "true"}

