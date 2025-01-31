from fastapi import FastAPI
from api.v1.views import routes


def create_app():
    app = FastAPI(title='Hatiko Test Task')
    app.include_router(routes)
    return app
